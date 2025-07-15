## ✅ Звіт: Health Checks (Liveness & Readiness Probes)

### 📋 Завдання

#### 🔹 Liveness Probe
- Налаштовано перевірку на ендпоінт `/health/live`
- Використано HTTP GET на порт `5000`

#### 🔹 Readiness Probe
- Налаштовано перевірку на ендпоінт `/health/ready`
- Використано HTTP GET на порт `5000`

#### YAML-конфігурація (фрагмент з `deployment.yaml`):
```yaml
livenessProbe:
  httpGet:
    path: /health/live
    port: 5000
  initialDelaySeconds: 5
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /health/ready
    port: 5000
  initialDelaySeconds: 5
  periodSeconds: 10
```

---

### 🧪 Тестування Readiness Probe

#### 🔸 Крок 1: Імітація проблеми
- Значення `POSTGRES_PASSWORD` у `ConfigMap` було навмисно видалене (порожнє).
- Після `rollout restart` pod запустився, але не міг з’єднатися з БД.
- Ендпоінт `/health/ready` повертав `503`, `readinessProbe` не проходила.

#### 🔸 Крок 2: Результат
- Pod отримав статус `0/1 READY`, Kubernetes **не направляв трафік** на нього.
- У `kubectl describe pod` було зафіксовано подію:

![Screenshot 2025-07-11 at 18.37.53.png](Screenshot%202025-07-11%20at%2018.37.53.png)

---

### 🛠 Виправлення ситуації

#### 🔸 Кроки
1. Оновлено `ConfigMap` зі значенням:
    ```yaml
    POSTGRES_PASSWORD: password
    ```
2. Повторно застосовано конфігурацію:
    ```bash
    kubectl apply -f k8s/demo-cm.yaml
    kubectl rollout restart deployment demo-app -n demo
    ```
3. Нові pod'и стартували з правильним значенням, `readinessProbe` пройшла успішно:
    ```
    demo-app-79cd47984c-hr9lv   1/1     Running   0   ...
    ```

![Screenshot 2025-07-11 at 18.37.03.png](Screenshot%202025-07-11%20at%2018.37.03.png)

---

### 🐞 Проблеми і рішення

| Проблема                              | Рішення                                                                 |
|--------------------------------------|--------------------------------------------------------------------------|
| Pod не проходив readiness check      | Навмисно зламали підключення до БД, щоб перевірити поведінку readiness  |
| `POSTGRES_PASSWORD` був порожній     | Оновили ConfigMap, перезапустили Deployment                             |
| Pod мав `0/1 READY`                  | Очікувана поведінка Kubernetes на провал readiness                      |

---

### 📸 Докази виконання (додані до PR)

- `kubectl describe pod` з подіями `Readiness probe failed`
- `kubectl exec ... printenv` — демонстрація змінної `POSTGRES_PASSWORD` (порожньої та коректної)
- `kubectl get pods` — перехід від `0/1` до `1/1` після виправлення
- Вміст `ConfigMap` до та після оновлення


# 📘 Kubernetes Ingress + TLS + Версії застосунку

Цей звіт описує виконання домашнього завдання з налаштування Ingress-контролера в MicroK8s із підтримкою TLS та маршрутизацією до двох версій застосунку (`v1` та `v2`).

---

## ✅ Звіт: Ingress

### 1. Увімкнення Ingress:

```bash
microk8s enable ingress
```

### 2. Створення TLS-сертифіката і секрету:

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout tls.key -out tls.crt -subj "/CN=demo.local"

kubectl create secret tls demo-local-tls \
  --cert=tls.crt --key=tls.key \
  -n demo
```

### 3. Записи в `/etc/hosts`:

```
127.0.0.1 demo.local
127.0.0.1 v1.demo.local
```

---

## 🚀 Розгортання застосунків

### Версія `v1`:

* Deployment: `demo-app-v1`
* Образ: `opazyniuk/python-app:hw-8`
* Label: `version: v1`
* Фон: білий
* База даних: **не підключена**

### Версія `v2`:

* Deployment: `demo-app-v2`
* Service: `demo-service`
* Образ: `opazyniuk/python-app:hw-5`
* Label: `version: v2`
* Фон: синій
* База даних: **підключена**

---

## 🌐 Ingress

### Анотація:

```yaml
nginx.ingress.kubernetes.io/rewrite-target: /$1
```

### Ingress-правила:

```yaml
spec:
  tls:
    - hosts:
        - demo.local
        - v1.demo.local
      secretName: demo-local-tls
  rules:
    - host: demo.local
      http:
        paths:
          - path: /v1(/|$)(.*)
            pathType: Prefix
            backend:
              service:
                name: demo-app-v1
                port:
                  number: 80
          - path: /(.*)
            pathType: Prefix
            backend:
              service:
                name: demo-service
                port:
                  number: 80
    - host: v1.demo.local
      http:
        paths:
          - path: /(.*)
            pathType: Prefix
            backend:
              service:
                name: demo-app-v1
                port:
                  number: 80
```

---

## 🔮 Перевірка результатів

### Команди:

```bash
curl -k https://demo.local/
curl -k https://demo.local/v1
curl -k https://v1.demo.local/
```

### Результати:

| URL                                            | Версія | Очікувано         | Фактично |
| ---------------------------------------------- | ------ | ----------------- | -------- |
| [https://demo.local](https://demo.local)       | `v2`   | Синій фон, база є | ✅        |
| [https://demo.local/v1](https://demo.local/v1) | `v1`   | Білий фон, база ❌ | ✅        |
| [https://v1.demo.local](https://v1.demo.local) | `v1`   | Білий фон, база ❌ | ✅        |

---

## 📊 Підсумок

| Компонент         | Статус | Коментар                                 |
| ----------------- | ------ | ---------------------------------------- |
| Ingress           | ✅      | TLS + маршрутизація працює               |
| TLS-секрет        | ✅      | Самопідписаний, використовується Ingress |
| demo-app-v1       | ✅      | Доступний по /v1 та v1.demo.local        |
| demo-service (v2) | ✅      | Основна версія                           |
| DNS (hosts)       | ✅      | Правильно маршрутизовано локально        |
| Перевірка         | ✅      | curl показав коректну роботу всього      |

---

**✅ Домашнє завдання виконано повністю.**
![Screenshot 2025-07-15 at 20.27.45.png](Screenshot%202025-07-15%20at%2020.27.45.png)
![Screenshot 2025-07-15 at 20.28.21.png](Screenshot%202025-07-15%20at%2020.28.21.png)
![Screenshot 2025-07-15 at 21.04.03.png](Screenshot%202025-07-15%20at%2021.04.03.png)
