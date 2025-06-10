1. **Підготовка середовища**

- Скопіюйте папку logs у свій репозиторій
```
DOCKER-AND-KUBERNETES_MARTYNIUK_1 git:(main) cp -r ./logs ../17-Pazynuyk-Ostap/
```

- Там знаходиться файл з налаштуваннями для fluentd1
```aiignore
➜  DOCKER-AND-KUBERNETES_MARTYNIUK_1 git:(main) cd ../17-Pazynuyk-Ostap 
➜  17-Pazynuyk-Ostap git:(main) ✗ docker network create logging
4a54bfb6c245eb4e706e1e666fdc06b192370c49799338669907c2586b87b1a6
➜  17-Pazynuyk-Ostap git:(main) ✗ cd logs 
➜  logs git:(main) ✗ ls -la
total 16
drwxrwxr-x  2 ostap ostap 4096 May 29 16:31 .
drwxrwxr-x 14 ostap ostap 4096 May 29 16:30 ..
-rw-rw-r--  1 ostap ostap  151 May 29 16:36 Dockerfile
-rw-rw-r--  1 ostap ostap  240 May 29 16:30 fluent.conf
➜  logs git:(main) ✗ 
```

2. **Створення кастомного образу для Fluentd**

- Створіть Dockerfile в директорії logs
```aiignore
➜  logs git:(main) ✗ cat Dockerfile
FROM fluent/fluentd:v1.16-debian

USER root

RUN gem install fluent-plugin-grafana-loki --no-document

COPY fluent.conf /fluentd/etc/

USER fluent
```
- Використовуйте офіційний образ fluent/fluentd

Зроблено у Dockerfile

- Встановіть необхідний плагіни для роботи з Loki
- Скопіюйте конфігураційний файл
- Зберіть докер образ
```aiignore
➜  logs git:(main) ✗ docker build -t custom-fluentd .
[+] Building 13.8s (8/8) FINISHED                                                                                                                                                 docker:default
 => [internal] load build definition from Dockerfile                                                                                                                                        0.0s
 => => transferring dockerfile: 186B                                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/fluent/fluentd:v1.16-debian                                                                                                                      1.7s
 => [internal] load .dockerignore                                                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                                             0.0s
 => [1/3] FROM docker.io/fluent/fluentd:v1.16-debian@sha256:cfd3004ce65cee1b7614bd58bb525706992588ca3a9b38708f93be9cf8c519a5                                                                9.9s
 => => resolve docker.io/fluent/fluentd:v1.16-debian@sha256:cfd3004ce65cee1b7614bd58bb525706992588ca3a9b38708f93be9cf8c519a5                                                                0.0s
 => => sha256:cfd3004ce65cee1b7614bd58bb525706992588ca3a9b38708f93be9cf8c519a5 990B / 990B                                                                                                  0.0s
 => => sha256:3b250293b581fa658da047b479db3c82ed92df8a33f48a6ec980ed1d235dc0de 2.07kB / 2.07kB                                                                                              0.0s
 => => sha256:87911fd295d355d0b5df936381f8c2b6a954e26ffdc125778afc9184ae4af0ad 10.68kB / 10.68kB                                                                                            0.0s
 => => sha256:073578d117750f596aa7c996766062136858c6982a3366ccfda4b86863b9f6e4 3.32MB / 3.32MB                                                                                              1.1s
 => => sha256:943331d8a9a9863299c02e5de6cce58602a5bc3dc564315aa886fe706376f27f 28.07MB / 28.07MB                                                                                            6.5s
 => => sha256:3a6a41801c108bbc051599c06248ae883c1dfda0b5e11ba381d880d24951703c 190B / 190B                                                                                                  0.3s
 => => sha256:f9b528631e023ec6df6232ebd753e91cd88f7a7d77629ba3cf6ca3c9649d1a77 35.88MB / 35.88MB                                                                                            7.5s
 => => sha256:394e732f50f5ab2bddcd3cd96eea115623ef49e9d5420ff41fd6a3a260f650df 143B / 143B                                                                                                  1.4s
 => => sha256:86423a774338de7bc80e9b979fe0344bd39a837f6d5109f9ffbccf0815ebe5e9 19.35MB / 19.35MB                                                                                            6.4s
 => => sha256:b29dc0a0854eec6cb2dc1dbc4ceae043273ece18b9bec6ce7a1dfa53c28181cf 1.18kB / 1.18kB                                                                                              6.6s
 => => sha256:041e2134b27013a9538161db37477e6fd4f0d3c9a867df664941171131cc99c5 404B / 404B                                                                                                  6.6s
 => => extracting sha256:943331d8a9a9863299c02e5de6cce58602a5bc3dc564315aa886fe706376f27f                                                                                                   1.3s
 => => sha256:9fcfe22a551ff0a480619509aecbd6121415cacf7f61286327eeafaf9107f634 479B / 479B                                                                                                  6.9s
 => => extracting sha256:073578d117750f596aa7c996766062136858c6982a3366ccfda4b86863b9f6e4                                                                                                   0.1s
 => => extracting sha256:3a6a41801c108bbc051599c06248ae883c1dfda0b5e11ba381d880d24951703c                                                                                                   0.0s
 => => extracting sha256:f9b528631e023ec6df6232ebd753e91cd88f7a7d77629ba3cf6ca3c9649d1a77                                                                                                   0.8s
 => => extracting sha256:394e732f50f5ab2bddcd3cd96eea115623ef49e9d5420ff41fd6a3a260f650df                                                                                                   0.0s
 => => extracting sha256:86423a774338de7bc80e9b979fe0344bd39a837f6d5109f9ffbccf0815ebe5e9                                                                                                   1.0s
 => => extracting sha256:b29dc0a0854eec6cb2dc1dbc4ceae043273ece18b9bec6ce7a1dfa53c28181cf                                                                                                   0.0s
 => => extracting sha256:041e2134b27013a9538161db37477e6fd4f0d3c9a867df664941171131cc99c5                                                                                                   0.0s
 => => extracting sha256:9fcfe22a551ff0a480619509aecbd6121415cacf7f61286327eeafaf9107f634                                                                                                   0.0s
 => [internal] load build context                                                                                                                                                           0.0s
 => => transferring context: 280B                                                                                                                                                           0.0s
 => [2/3] RUN gem install fluent-plugin-grafana-loki --no-document                                                                                                                          2.2s
 => [3/3] COPY fluent.conf /fluentd/etc/                                                                                                                                                    0.0s 
 => exporting to image                                                                                                                                                                      0.0s 
 => => exporting layers                                                                                                                                                                     0.0s
 => => writing image sha256:75e3af9151fafc123fb2ac2cb7e5ca991f4f7b86b0cf0c99d90d2cdf74453ea7                                                                                                0.0s
 => => naming to docker.io/library/custom-fluentd   
```
![Screenshot 2025-05-29 at 20.38.46.png](Screenshot%202025-05-29%20at%2020.38.46.png)

3. **Налаштування мережі**

- Створіть Docker мережу з назвою logging
![Screenshot 2025-05-29 at 20.25.50.png](Screenshot%202025-05-29%20at%2020.25.50.png)
```aiignore
  17-Pazynuyk-Ostap git:(main) ✗ docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
9986335ee1f4   app-network   bridge    local
cf2f862c37a7   bridge        bridge    local
a94f1621e941   host          host      local
4a54bfb6c245   logging       bridge    local
2f637a780515   none          null      local

```

4. **Запуск Loki**

- Запустіть Loki з наступними параметрами:
  - Назва контейнера: loki
  - Підключення до мережі logging
  - Порти не мапити
  - Образ: grafana/loki
```aiignore
➜  logs git:(main) ✗ docker run -d \
  --name loki \
  --network logging \
  grafana/loki
Unable to find image 'grafana/loki:latest' locally
latest: Pulling from grafana/loki
8ab2969f3376: Pull complete 
2e4cf50eeb92: Pull complete 
4e9f20d26c87: Pull complete 
0f8b424aa0b9: Pull complete 
d557676654e5: Pull complete 
d82bc7a76a83: Pull complete 
d858cbc252ad: Pull complete 
1069fc2daed1: Pull complete 
b40161cd83fc: Pull complete 
3f4e2c586348: Pull complete 
80a8c047508a: Pull complete 
ffeccacd1a73: Pull complete 
6e72028b5e58: Pull complete 
ea1a0470c003: Pull complete 
5e7c20c4db2b: Pull complete 
b7fff975d039: Pull complete 
Digest: sha256:a74594532eec4cc313401beedc4dd2708c43674c032084b1aeb87c14a5be1745
Status: Downloaded newer image for grafana/loki:latest
47a543c5fe63f4d39dce2c3bfd1ca078fcb05e5ec66ae5e6111bb56cc6ca1638
```

5. **Запуск Fluentd**
- Запустіть Fluentd з наступними параметрами:
- Назва контейнера: fluentd
- Підключення до мережі logging
- Порти не мапити
- Передати енв змінну LOKI_URL
```aiignore
➜  logs git:(main) ✗ docker run -d \
  --name fluentd \
  --network logging \
  -e LOKI_URL=http://loki:3100 \
  custom-fluentd
08bb1dcd54c498d5c113755f83798eb61c22cd1b721a7239f93421a098eb6e4a
➜  logs git:(main) ✗ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                 NAMES
08bb1dcd54c4   custom-fluentd   "tini -- /bin/entryp…"   3 seconds ago   Up 2 seconds   5140/tcp, 24224/tcp   fluentd
47a543c5fe63   grafana/loki     "/usr/bin/loki -conf…"   3 minutes ago   Up 3 minutes   3100/tcp              loki
➜  logs git:(main) ✗ docker logs fluentd
2025-05-29 17:45:55 +0000 [info]: init supervisor logger path=nil rotate_age=nil rotate_size=nil
2025-05-29 17:45:55 +0000 [info]: parsing config file is succeeded path="/fluentd/etc/fluent.conf"
2025-05-29 17:45:55 +0000 [info]: gem 'fluentd' version '1.16.9'
2025-05-29 17:45:55 +0000 [info]: gem 'fluent-plugin-grafana-loki' version '1.2.20'
2025-05-29 17:45:55 +0000 [warn]: define <match fluent.**> to capture fluentd logs in top level is deprecated. Use <label @FLUENT_LOG> instead
2025-05-29 17:45:55 +0000 [info]: using configuration file: <ROOT>
  <source>
    @type forward
  </source>
  <filter **>
    @type stdout
  </filter>
  <match **>
    @type loki
    url "http://loki:3100"
    extra_labels {"job":"fluentd"}
    <buffer>
      flush_interval 10s
      flush_at_shutdown true
    </buffer>
  </match>
</ROOT>
2025-05-29 17:45:55 +0000 [info]: starting fluentd-1.16.9 pid=7 ruby="3.2.8"
2025-05-29 17:45:55 +0000 [info]: spawn command to main:  cmdline=["/usr/local/bin/ruby", "-Eascii-8bit:ascii-8bit", "/usr/local/bundle/bin/fluentd", "--config", "/fluentd/etc/fluent.conf", "--plugin", "/fluentd/plugins", "--under-supervisor"]
2025-05-29 17:45:55 +0000 [info]: #0 init worker0 logger path=nil rotate_age=nil rotate_size=nil
2025-05-29 17:45:55 +0000 [info]: adding filter pattern="**" type="stdout"
2025-05-29 17:45:55 +0000 [info]: adding match pattern="**" type="loki"
2025-05-29 17:45:55 +0000 [info]: adding source type="forward"
2025-05-29 17:45:55 +0000 [warn]: #0 define <match fluent.**> to capture fluentd logs in top level is deprecated. Use <label @FLUENT_LOG> instead
2025-05-29 17:45:55 +0000 [info]: #0 starting fluentd worker pid=16 ppid=7 worker=0
2025-05-29 17:45:55 +0000 [info]: #0 listening port port=24224 bind="0.0.0.0"
2025-05-29 17:45:55 +0000 [info]: #0 fluentd worker is now running worker=0
2025-05-29 17:45:55.534098101 +0000 fluent.info: {"pid":16,"ppid":7,"worker":0,"message":"starting fluentd worker pid=16 ppid=7 worker=0"}
2025-05-29 17:45:55.534448980 +0000 fluent.info: {"port":24224,"bind":"0.0.0.0","message":"listening port port=24224 bind=\"0.0.0.0\""}
2025-05-29 17:45:55.535436572 +0000 fluent.info: {"worker":0,"message":"fluentd worker is now running worker=0"}

```

6. **Запуск Grafana**

- Запустіть Grafana з наступними параметрами:
  - Назва контейнера: grafana
  - Підключення до мережі logging
  - Замапити порт 3000 на 3000
  - Образ grafana/grafana
```aiignore
  logs git:(main) ✗ docker run -d \
  --name grafana \
  --network logging \
  -p 3000:3000 \
  grafana/grafana

Unable to find image 'grafana/grafana:latest' locally
latest: Pulling from grafana/grafana
6e771e15690e: Pull complete 
c13cf23161d8: Pull complete 
a2b255b2aa14: Pull complete 
a89eac3bcaee: Pull complete 
8c99e2a25287: Pull complete 
c66b418533e4: Pull complete 
b24a93192a6a: Pull complete 
1a4df7eb367d: Pull complete 
117e9cc05b96: Pull complete 
9a8c18aee5ea: Pull complete 
Digest: sha256:06dc8d60e184705e5dc00e051a6d92342a44010d7d5e538d0a36339e85abb9b7
Status: Downloaded newer image for grafana/grafana:latest
34e15582b7c6cc50fdf6fcb63113f39516aec4ff0ce24d10ec4fc6779b3dc50c
➜  logs git:(main) ✗ docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                                         NAMES
34e15582b7c6   grafana/grafana   "/run.sh"                5 seconds ago   Up 5 seconds   0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp   grafana
08bb1dcd54c4   custom-fluentd    "tini -- /bin/entryp…"   4 minutes ago   Up 4 minutes   5140/tcp, 24224/tcp                           fluentd
47a543c5fe63   grafana/loki      "/usr/bin/loki -conf…"   8 minutes ago   Up 8 minutes   3100/tcp                                      loki

```

7. **Запустіть демо-сервіс**

- Запустіть контейнер з наступними параметрами:
  - Назва контейнера: demo
  - Підключення до мережі logging
  - Образ оптимізований з попереднього завдання
  - Передати параметри для log driver
  - Передати тег docker через опції дравера
  - Замапити порт 80 на 5000
docker 
8. **Перевірте роботу компонентів**

- Перевірте доступність демо-сервісу
```aiignore
➜  logs git:(main) ✗ curl http://127.0.0.1:80/

<!DOCTYPE html>
<html>
<head>
    <title>Demo Updated App Ostap</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #ffffff;
        }
        .image-container {
            margin: 20px 0;
            text-align: center;
        }
        .image-container img {
            max-width: 300px;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <h1>Demo Updated App Ostap</h1>
    <p>Current time: 2025-05-29 18:28:51</p>
    <p>Database status: Not connected</p>
    <p>Feature flags:</p>
    <ul>
        
        <li>USE_POSTGRES: False</li>
        
        <li>FAIL_AFTER_START: False</li>
        
    </ul>
    <div class="image-container">
        <img src="/static/photo.jpg" alt="Demo Image">
    </div>
</body>
</html>%     
```
- Перевірте збір логів у Fluentd
```aiignore
➜  logs git:(main) ✗ docker logs fluentd | tail -n 5         
2025-05-29 18:30:10 +0000 [info]: #0 listening port port=24224 bind="0.0.0.0"
2025-05-29 18:30:10 +0000 [info]: #0 fluentd worker is now running worker=0
2025-05-29 18:30:10.152186238 +0000 fluent.info: {"pid":16,"ppid":7,"worker":0,"message":"starting fluentd worker pid=16 ppid=7 worker=0"}
2025-05-29 18:30:10.152718157 +0000 fluent.info: {"port":24224,"bind":"0.0.0.0","message":"listening port port=24224 bind=\"0.0.0.0\""}
2025-05-29 18:30:10.153379701 +0000 fluent.info: {"worker":0,"message":"fluentd worker is now running worker=0"}
```

- Підключіть data source Loki в Grafana
- Перевірте відображення логів у Grafana
![Screenshot 2025-05-29 at 21.32.23.png](Screenshot%202025-05-29%20at%2021.32.23.png)

- Створіть дашборд для відображення логів
![Screenshot 2025-05-29 at 21.39.40.png](../../../../../../../var/folders/vz/3c78h5j929s_08z10prx36ym0000gn/T/TemporaryItems/NSIRD_screencaptureui_yn7Xoo/Screenshot%202025-05-29%20at%2021.39.40.png)

- Опис будь-яких проблем, з якими ви зіткнулися
Виникли труднощі з розумінням синтаксису у Grafana для філтрації логів
