**1. Стек з попереднього завдання описати в compose.yaml файлі**

Стек сервісів
- demo: Flask-додаток
- fluentd: лог-агент, який збирає логи з docker
- loki: сховище логів від Grafana Labs
- grafana: інтерфейс для візуалізації логів

**2. Розгорнути за допомогою docker-compose**
![Screenshot 2025-06-10 at 20.49.44.png](Screenshot%202025-06-10%20at%2020.49.44.png)
![Screenshot 2025-06-10 at 20.51.11.png](Screenshot%202025-06-10%20at%2020.51.11.png)

Успішно запустив всі сервіси за допомогою docker-compose

**3. Додати БД та підключити до нашого сервісу**

- додав сервіс postgres з необхідними допоміжними налаштуваннями, перевірив що demo сервіс взаємодіє з ним як і очікується
![Screenshot 2025-06-10 at 22.59.11.png](Screenshot%202025-06-10%20at%2022.59.11.png)
**4. Перевірити функціонування усіх сервісів**
Всі сервіси працюють як і очікувалось
![Screenshot 2025-06-10 at 23.00.55.png](Screenshot%202025-06-10%20at%2023.00.55.png)
![Screenshot 2025-06-10 at 22.28.51.png](Screenshot%202025-06-10%20at%2022.28.51.png)

- опис труднощів
  Проблема з резолвінгом імені fluentd у Docker Compose
  ❌ Симптом проблеми:
  Після конфігурації сервісу demo, який логував дані через Fluentd, з’ясувалося, що:

Fluentd не приймав логи, хоча був запущений і прослуховував порт 24224.

У docker-compose.yml у сервісі demo було прописано:

```
logging:
    driver: fluentd
options:
    fluentd-address: fluentd:24224
```
Але логи не надходили, а в Loki вони так і не з'являлись.

**🔍 Причина:**
Службова назва fluentd не резолвилася в IP-адресу всередині Docker мережі logging.

Хоча docker-compose автоматично додає кожному сервісу ім’я, доступне всередині спільної мережі, у цьому випадку:

Або ім’я fluentd не було ще зареєстроване, коли demo стартував;

Або log драйвер Docker Fluentd не підтримує DNS-резолвінг, як звичайні сервіси (це особливість лог-драйверів — вони працюють поза контекстом Docker DNS);

У підсумку, відбувалася помилка з'єднання на fluentd:24224.

✅ Обхідне рішення: ручна IP-адреса
Щоб обійти проблему з резолвінгом:

Ми додали IPAM (керування IP) у конфігурацію мережі logging:

```aiignore
networks:
    logging:
        driver: bridge
ipam:
    config:
        - subnet: 172.20.0.0/16
```
І прописали фіксовану IP-адресу для Fluentd:

```
fluentd:
    networks:
        logging:
            ipv4_address: 172.20.0.10
```

Потім, у demo:
```
logging:
    driver: fluentd
options:
    fluentd-address: 172.20.0.10:24224
```

**Доповнення до ДЗ:**
Виправив коментарі, а саме додав фіксовані теги та спрощені атрибути для оптимізації синтаксису.
Також дописав для чого використовував healthcheck для fluentd застосунку.
(оскільки сервіс demo запускався швидше ніж fluentd, в результаті чого відбувалась помилка запуску застосунку, оскільки логіка виконання даного сервісу очікує на успішний зв'язок з fluentd при запуску)

```aiignore
➜  17-Pazynuyk-Ostap git:(HW-6) ✗ docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED          STATUS                    PORTS                                         NAMES
1eba93438684   grafana/grafana:11.5.0      "/run.sh"                12 seconds ago   Up 11 seconds             0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp   grafana
e4c06731ff24   grafana/loki:3.4.4          "/usr/bin/loki -conf…"   12 seconds ago   Up 11 seconds             3100/tcp                                      loki
6b38febedd25   postgres:17                 "docker-entrypoint.s…"   12 seconds ago   Up 11 seconds             5432/tcp                                      postgres
58b023190158   python-app:hw-5             "python3 app.py"         4 days ago       Up 5 seconds              0.0.0.0:80->5000/tcp, [::]:80->5000/tcp       demo
da4a0fba53a0   17-pazynuyk-ostap-fluentd   "tini -- /bin/entryp…"   4 days ago       Up 11 seconds (healthy)   5140/tcp, 24224/tcp                           fluentd
```
