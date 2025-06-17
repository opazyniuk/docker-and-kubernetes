1. **Підготовка середовища**
    - Скопіюйте оновлений код застосунку у свій репозиторій
      - Файл app.py оновлено, зміни можна побачити у diff цього PR-y. 
    - Зберіть новий образ та завантажте його на DockerHub з новим мінорним тегом
      - Новий образ зібрано та завантажено до Docker Hub 
        - https://hub.docker.com/layers/opazyniuk/python-app/hw-7/images/sha256-50b8b50757b07e7e8d9092fa64f157f683a4c42d4a905b2991d7c2c4773bd398.

2. **Створіть ConfigMap для налаштувань застосунку**
    - Створіть файл `demo-cm.yaml`
    - Додайте змінні середовища, наприклад: `BACKGROUND_COLOR`, `FIB_NUMBER`

Створив новий файл і додав необхідні налаштування, переглянути файл можна за шляхом `k8s/demo-cm.yaml`

3. **Створіть Deployment для demo застосунку**
    - Створіть файл `demo.yaml`
    - Підключіть ConfigMap як змінні середовища
    - Не забудьте про resource requests/limits

Створив новий файл і додав необхідні налаштування, переглянути файл можна за шляхом `k8s/demo.yaml`

4. **Створіть Service для доступу до застосунку**
    - Створіть файл `demo-svc.yaml`
    - Тип сервісу: ClusterIP або NodePort

Створив новий файл і додав необхідні налаштування, переглянути файл можна за шляхом `k8s/demo-svc.yaml`.
Тип сервісу вирішив обрати **NodePort**.

5. **Створіть HPA для demo Deployment**
    - Створіть файл `demo-hpa.yaml`
    - Використовуйте CPU як метрику

Створив новий файл і додав необхідні налаштування, переглянути файл можна за шляхом `k8s/demo-hpa.yaml`.
Використав CPU як значення, по якому треба орієнтуватись для того, щоб виконувалось масштабування або згортання додаткових подів.

6. **Перевірте статус усіх ресурсів**

Послідовно запускав усі маніфести у кластері, внаслідок чого вдалось успішно запустити всі необхідні сервіси.
```aiignore
➜  k8s git:(main) ✗ kubectl get all -n demo

NAME                            READY   STATUS    RESTARTS   AGE
pod/demo-app-75b7c57d4f-5lk48   1/1     Running   0          9s
pod/demo-app-75b7c57d4f-cd2gt   1/1     Running   0          17s

NAME                   TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/demo-service   NodePort   10.152.183.72   <none>        5000:30007/TCP   26m

NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/demo-app   2/2     2            2           27m

NAME                                  DESIRED   CURRENT   READY   AGE
replicaset.apps/demo-app-54c8b9fcc8   0         0         0       44s
replicaset.apps/demo-app-6657959fb    0         0         0       4m20s
replicaset.apps/demo-app-75b7c57d4f   2         2         2       17s
replicaset.apps/demo-app-76f99c454d   0         0         0       8m59s
replicaset.apps/demo-app-7b688d66cb   0         0         0       27m
```
![Screenshot 2025-06-17 at 19.47.43.png](Screenshot%202025-06-17%20at%2019.47.43.png)

7. **Перевірте метрики**

![Screenshot 2025-06-17 at 19.50.36.png](Screenshot%202025-06-17%20at%2019.50.36.png)
Перевірив що метрики відслідковуються так як і очікувалось.

8. **Створіть навантаження на сервіс**
    - Дізнайтесь ClusterIP або NodePort сервісу
    - Використайте pod з утилітою `curl`, або робіть запити локально (якщо створили NodePort) для навантаження

Встановив бібліотеку stress на один з подів і почав його "мочити" споживанням CPU, і припинив цей процес щоб побачити зміни
```aiignore
  k8s git:(main) ✗ kubectl get pods -n demo         

NAME                        READY   STATUS    RESTARTS   AGE
demo-app-75b7c57d4f-5lk48   1/1     Running   0          26m
demo-app-75b7c57d4f-cd2gt   1/1     Running   0          26m
➜  k8s git:(main) ✗ kubectl exec -it demo-app-75b7c57d4f-5lk48 -n demo -- /bin/sh
# apt update && apt install -y stress
Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]
Get:2 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]
Get:3 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]
Get:4 http://deb.debian.org/debian bookworm/main arm64 Packages [8693 kB]
Get:5 http://deb.debian.org/debian bookworm-updates/main arm64 Packages [756 B]
Get:6 http://deb.debian.org/debian-security bookworm-security/main arm64 Packages [259 kB]
Fetched 9207 kB in 4s (2587 kB/s)                         
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
1 package can be upgraded. Run 'apt list --upgradable' to see it.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  stress
0 upgraded, 1 newly installed, 0 to remove and 1 not upgraded.
Need to get 21.3 kB of archives.
After this operation, 97.3 kB of additional disk space will be used.
Get:1 http://deb.debian.org/debian bookworm/main arm64 stress arm64 1.0.7-1 [21.3 kB]
Fetched 21.3 kB in 0s (228 kB/s) 
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package stress.
(Reading database ... 6680 files and directories currently installed.)
Preparing to unpack .../stress_1.0.7-1_arm64.deb ...
Unpacking stress (1.0.7-1) ...
Setting up stress (1.0.7-1) ...
# stress --cpu 1 --timeout 300
stress: info: [618] dispatching hogs: 1 cpu, 0 io, 0 vm, 0 hdd
^C# 
```

9. **Спостерігайте за HPA**

Запустив команду з відслідковування стану масшстабування подів, побачив що зразу після запуску мною команди stress, збільшилась кількість реплік
```aiignore
➜  k8s git:(main) ✗ kubectl get hpa -n demo -w
NAME           REFERENCE             TARGETS        MINPODS   MAXPODS   REPLICAS   AGE
demo-app-hpa   Deployment/demo-app   cpu: 32%/50%   2         5         2          36m
demo-app-hpa   Deployment/demo-app   cpu: 1%/50%    2         5         2          36m

demo-app-hpa   Deployment/demo-app   cpu: 2%/50%    2         5         2          41m
demo-app-hpa   Deployment/demo-app   cpu: 1%/50%    2         5         2          41m

demo-app-hpa   Deployment/demo-app   cpu: 84%/50%   2         5         2          53m
demo-app-hpa   Deployment/demo-app   cpu: 8%/50%    2         5         4          54m

demo-app-hpa   Deployment/demo-app   cpu: 126%/50%   2         5         4          54m
demo-app-hpa   Deployment/demo-app   cpu: 103%/50%   2         5         5          54m

demo-app-hpa   Deployment/demo-app   cpu: 7%/50%     2         5         5          55m
demo-app-hpa   Deployment/demo-app   cpu: 1%/50%     2         5         5          55m
```

Застосунок відображається у хост системі через заданий порт.
![Screenshot 2025-06-17 at 20.22.26.png](Screenshot%202025-06-17%20at%2020.22.26.png)