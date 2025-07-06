### 1. Підготовка кластеру MicroK8s
Встановлено MicroK8s з усіма необхідними аддонами (dns, storage, metrics-server, dashboard тощо).
```aiignore
➜  k8s git:(HW-9) ✗ microk8s status --wait-ready

microk8s is running
high-availability: no
  datastore master nodes: 127.0.0.1:19001
  datastore standby nodes: none
addons:
  enabled:
    dashboard            # (core) The Kubernetes dashboard
    dns                  # (core) CoreDNS
    ha-cluster           # (core) Configure high availability on the current node
    helm                 # (core) Helm - the package manager for Kubernetes
    helm3                # (core) Helm 3 - the package manager for Kubernetes
    hostpath-storage     # (core) Storage class; allocates storage from host directory
    metrics-server       # (core) K8s Metrics Server for API access to service metrics
    registry             # (core) Private image registry exposed on localhost:32000
    storage              # (core) Alias to hostpath-storage add-on, deprecated
  disabled:
    cert-manager         # (core) Cloud native certificate management
    cis-hardening        # (core) Apply CIS K8s hardening
    community            # (core) The community addons repository
    host-access          # (core) Allow Pods connecting to Host services smoothly
    ingress              # (core) Ingress controller for external access
    kube-ovn             # (core) An advanced network fabric for Kubernetes
    mayastor             # (core) OpenEBS MayaStor
    metallb              # (core) Loadbalancer for your Kubernetes cluster
    minio                # (core) MinIO object storage
    observability        # (core) A lightweight observability stack for logs, traces and metrics
    prometheus           # (core) Prometheus operator for monitoring and logging
    rbac                 # (core) Role-Based Access Control for authorisation
    rook-ceph            # (core) Distributed Ceph storage using Rook
➜  k8s git:(HW-9) ✗ microk8s enable dns storage helm3 ingress

Infer repository core for addon dns
Infer repository core for addon storage
Infer repository core for addon helm3
Infer repository core for addon ingress
WARNING: Do not enable or disable multiple addons in one command.
         This form of chained operations on addons will be DEPRECATED in the future.
         Please, enable one addon at a time: 'microk8s enable <addon>'
Addon core/dns is already enabled
Addon core/storage is already enabled
Addon core/helm3 is already enabled
Enabling Ingress
ingressclass.networking.k8s.io/public created
ingressclass.networking.k8s.io/nginx created
namespace/ingress created
serviceaccount/nginx-ingress-microk8s-serviceaccount created
clusterrole.rbac.authorization.k8s.io/nginx-ingress-microk8s-clusterrole created
role.rbac.authorization.k8s.io/nginx-ingress-microk8s-role created
clusterrolebinding.rbac.authorization.k8s.io/nginx-ingress-microk8s created
rolebinding.rbac.authorization.k8s.io/nginx-ingress-microk8s created
configmap/nginx-load-balancer-microk8s-conf created
configmap/nginx-ingress-tcp-microk8s-conf created
configmap/nginx-ingress-udp-microk8s-conf created
daemonset.apps/nginx-ingress-microk8s-controller created
Ingress is enabled
```

### 2. Створено namespace monitoring для моніторинг-стека:

```bash
kubectl create namespace monitoring
````
### 3. Розгортання Prometheus
Створено:
- ServiceAccount, ClusterRole, ClusterRoleBinding 
- ConfigMap з кастомним prometheus.yml 
- PersistentVolumeClaim 
- Deployment та Service

В ConfigMap додано конфігурацію scrape для:

- Prometheus
- node-exporter
- demo-сервісу

До подів додано анотації:

```yaml
prometheus.io/scrape: "true"
prometheus.io/port: "5000"
```
### 4. Розгортання Grafana
Створено Deployment + Service

Після логіну (admin/admin), додано Data Source:

Prometheus: http://prometheus.monitoring.svc.cluster.local:9090
Loki: http://loki.monitoring.svc.cluster.local:3100

### 5. Розгортання Loki
Розгорнуто за допомогою офіційного loki-config.yaml

Створено Deployment + Service
Перевірено /ready та /metrics endpoints

### 6. Налаштування логування Promtail
Promtail розгорнуто як DaemonSet на кожній ноді

Ключові зміни в ConfigMap (promtail-configmap.yaml):

```yaml
relabel_configs:
- source_labels: [__meta_kubernetes_pod_name, __meta_kubernetes_namespace, __meta_kubernetes_container_name]
  separator: _
  target_label: __path__
  replacement: /var/log/containers/$1_$2_$3-*.log
  action: replace
 ```
Це дозволяє Promtail шукати логи в /var/log/containers/ за реальною схемою назв файлів

Після kubectl rollout restart daemonset promtail -n monitoring логування з demo-app запрацювало.

### 7. Тестування логування
### 🔍 Перевірка логів у Grafana
- Відкрито **Grafana → Explore**
- Обрано **Data Source**: `Loki`
- Виконано запит:
```logql
  {app="demo-app"}
```
![Screenshot 2025-07-06 at 16.32.35.png](Screenshot%202025-07-06%20at%2016.32.35.png)

![Screenshot 2025-07-06 at 16.58.11.png](Screenshot%202025-07-06%20at%2016.58.11.png)
```markdown
## ✅ Підсумок

| Компонент   | Статус     | Коментар                             |
|-------------|------------|--------------------------------------|
| Prometheus  | ✅ Готово   | Метрики збираються                   |
| Grafana     | ✅ Готово   | Дашборди працюють                    |
| Loki        | ✅ Готово   | Логи зберігаються                    |
| Promtail    | ✅ Готово   | Збирає логи з `demo-app`             |
| demo-app    | ✅ Працює   | Метрики й логи надходять до стеку   |
```

### 🐞 Проблеми та рішення

| Проблема                                 | Рішення                                                                 |
|------------------------------------------|--------------------------------------------------------------------------|
| Promtail не знаходив логи з `demo-app`   | Виправили `__path__` у `relabel_configs` на правильний формат `/var/log/containers/*.log` |
| Логи надходили з неправильним шляхом     | Врахували структуру файлів, які зберігаються `kubelet`’ом                |
| Loki повертав помилку `429 (rate limit)` | Проблема з інтенсивним логуванням — зменшено навантаження                |


```aiignore
➜  k8s git:(HW-9) ✗ kubectl apply -f grafana-service.yaml
service/grafana created
➜  k8s git:(HW-9) ✗ kubectl get svc grafana -n monitoring
NAME      TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
grafana   NodePort   10.152.183.58   <none>        3000:32001/TCP   16s
➜  k8s git:(HW-9) ✗ kubectl get svc -n monitoring 
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
grafana      NodePort    10.152.183.58    <none>        3000:32001/TCP   30s
loki         ClusterIP   10.152.183.81    <none>        3100/TCP         9m53s
prometheus   ClusterIP   10.152.183.111   <none>        9090/TCP         10m
➜  k8s git:(HW-9) ✗ kubectl apply -f k8s/promtail-configmap.yaml
kubectl apply -f k8s/promtail-rbac.yaml
kubectl apply -f k8s/promtail-daemonset.yaml
error: the path "k8s/promtail-configmap.yaml" does not exist
error: the path "k8s/promtail-rbac.yaml" does not exist
error: the path "k8s/promtail-daemonset.yaml" does not exist
➜  k8s git:(HW-9) ✗ kubectl apply -f promtail-configmap.yaml
kubectl apply -f promtail-rbac.yaml
kubectl apply -f promtail-daemonset.yaml
configmap/promtail-config created
serviceaccount/promtail created
clusterrole.rbac.authorization.k8s.io/promtail created
clusterrolebinding.rbac.authorization.k8s.io/promtail created
daemonset.apps/promtail created
➜  k8s git:(HW-9) ✗ kubectl get pods -n monitoring -l app=promtail

NAME             READY   STATUS    RESTARTS   AGE
promtail-vdsfh   1/1     Running   0          11s
➜  k8s git:(HW-9) ✗ kubectl get all -n monitoring
NAME                              READY   STATUS    RESTARTS   AGE
pod/grafana-c8f745d76-gh2h2       1/1     Running   0          4m22s
pod/loki-64c97d484-4zwmq          1/1     Running   0          6m4s
pod/prometheus-7b5d747766-fvnrk   1/1     Running   0          12m
pod/promtail-vdsfh                1/1     Running   0          25s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/grafana      NodePort    10.152.183.58    <none>        3000:32001/TCP   2m15s
service/loki         ClusterIP   10.152.183.81    <none>        3100/TCP         11m
service/prometheus   ClusterIP   10.152.183.111   <none>        9090/TCP         12m

NAME                      DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
daemonset.apps/promtail   1         1         1       1            1           <none>          26s

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/grafana      1/1     1            1           4m22s
deployment.apps/loki         1/1     1            1           11m
deployment.apps/prometheus   1/1     1            1           12m

NAME                                    DESIRED   CURRENT   READY   AGE
replicaset.apps/grafana-c8f745d76       1         1         1       4m22s
replicaset.apps/loki-64c97d484          1         1         1       6m4s
replicaset.apps/loki-6988df5f85         0         0         0       11m
replicaset.apps/prometheus-7b5d747766   1         1         1       12m
➜  k8s git:(HW-9) ✗ kubectl get svc -n monitoring grafana

NAME      TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
grafana   NodePort   10.152.183.58   <none>        3000:32001/TCP   3m10s
```
