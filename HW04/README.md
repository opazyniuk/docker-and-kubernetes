
1. Перевірте доступність веб-додатку за адресою http://localhost:80
![Screenshot 2025-05-28 at 18.12.11.png](Screenshot%202025-05-28%20at%2018.12.11.png)
```aiignore
➜  17-Pazynuyk-Ostap git:(main) ✗ docker build -t python-app:hw4-with-quotes . 
[+] Building 12.7s (11/11) FINISHED                                                                                          docker:default
 => [internal] load build definition from Dockerfile                                                                                   0.0s
 => => transferring dockerfile: 333B                                                                                                   0.0s
 => [internal] load metadata for docker.io/library/ubuntu:24.04                                                                        0.8s
 => [auth] library/ubuntu:pull token for registry-1.docker.io                                                                          0.0s
 => [internal] load .dockerignore                                                                                                      0.0s
 => => transferring context: 2B                                                                                                        0.0s
 => [1/5] FROM docker.io/library/ubuntu:24.04@sha256:6015f66923d7afbc53558d7ccffd325d43b4e249f41a6e93eef074c9505d2233                  0.0s
 => [internal] load build context                                                                                                      0.1s
 => => transferring context: 229.70kB                                                                                                  0.1s
 => CACHED [2/5] RUN apt-get update &&     apt-get install -y python3 python3-pip python3-venv libpq-dev &&     apt-get clean          0.0s
 => CACHED [3/5] WORKDIR /app                                                                                                          0.0s
 => [4/5] COPY . .                                                                                                                     0.4s
 => [5/5] RUN python3 -m venv venv_new &&     venv_new/bin/pip install -r requirements.txt                                            10.9s
 => exporting to image                                                                                                                 0.4s 
 => => exporting layers                                                                                                                0.4s 
 => => writing image sha256:dbb539cdc08ddadb5bd3e0b5e8e557a0667f0ede11ec84bc14461e7d6f26f1a4                                           0.0s 
 => => naming to docker.io/library/python-app:hw4-with-quotes                                                                          0.0s 
➜  17-Pazynuyk-Ostap git:(main) ✗ docker run -d \
  --name app \
  -p 80:5000 \
  --network app-network \
  -e USE_POSTGRES=true \
  -e POSTGRES_DB=demo \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_HOST=db \
  -e BACKGROUND_COLOR=#ffffff \
  -v $(pwd)/static:/static:ro \
 python-app:hw4-with-quotes
f667ae314050b9b00d0ffdff6a17aefb27d6dce9688620fcd45b18e02cb8e62e
```
- Збудував образ для застосунку
- Розгорнув образ застосунку з необхідними змінними

2. Перевірте відсутність доступу до PostgreSQL за адресою http://localhost:5432
![Screenshot 2025-05-28 at 18.13.12.png](Screenshot%202025-05-28%20at%2018.13.12.png)


3. Перевірте відображення випадкових цитат (перезавантажте сторінку)
![Screenshot 2025-05-28 at 17.57.05.png](Screenshot%202025-05-28%20at%2017.57.05.png)
![Screenshot 2025-05-28 at 17.57.14.png](Screenshot%202025-05-28%20at%2017.57.14.png)

- Труднощі, неправильно вказав шлях до файлу з налаштуванням бази даних, виправив це та перезапустив застосунок для postgresql
```aiignore
17-Pazynuyk-Ostap git:(main) ✗ docker volume create app-pgdata
app-pgdata
➜  17-Pazynuyk-Ostap git:(main) ✗ docker run -d \                
  --name db \
  --network app-network \
  -e POSTGRES_DB=demo \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -v app-pgdata:/var/lib/postgresql/data \
  -v $(pwd)/docker/init-scripts/init.sql:/docker-entrypoint-initdb.d/init.sql:ro \
  postgres

a08a5327f5c5eafa9950d2d0fda9223e5ad5b7995da72434779aeb166b722c75
➜  17-Pazynuyk-Ostap git:(main) ✗ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                                     NAMES
f667ae314050   python-app:hw4-with-quotes   "venv_new/bin/python…"   7 minutes ago   Up 7 minutes   0.0.0.0:80->5000/tcp, [::]:80->5000/tcp   app
➜  17-Pazynuyk-Ostap git:(main) ✗ docker ps -a
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS                     PORTS                                     NAMES
a08a5327f5c5   postgres                     "docker-entrypoint.s…"   11 seconds ago   Exited (1) 9 seconds ago                                             db
f667ae314050   python-app:hw4-with-quotes   "venv_new/bin/python…"   7 minutes ago    Up 7 minutes               0.0.0.0:80->5000/tcp, [::]:80->5000/tcp   app
➜  17-Pazynuyk-Ostap git:(main) ✗ docker logs db
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default "max_connections" ... 100
selecting default "shared_buffers" ... 128MB
selecting default time zone ... Etc/UTC
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok


Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgresql/data -l logfile start

initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
waiting for server to start....2025-05-28 14:52:30.333 UTC [48] LOG:  starting PostgreSQL 17.5 (Debian 17.5-1.pgdg120+1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
2025-05-28 14:52:30.333 UTC [48] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2025-05-28 14:52:30.335 UTC [51] LOG:  database system was shut down at 2025-05-28 14:52:30 UTC
2025-05-28 14:52:30.343 UTC [48] LOG:  database system is ready to accept connections
 done
server started
CREATE DATABASE


/usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/init.sql
psql:/docker-entrypoint-initdb.d/init.sql: error: could not read from input file: Is a directory
```


- Виправлення, перезапустив postgres і впевнився що все працює коректно
```aiignore
    ➜  17-Pazynuyk-Ostap git:(main) ✗ docker stop db             
db
➜  17-Pazynuyk-Ostap git:(main) ✗ docker remove db           
db
➜  17-Pazynuyk-Ostap git:(main) ✗ docker volume rm app-pgdata
app-pgdata
➜  17-Pazynuyk-Ostap git:(main) ✗ docker volume create app-pgdata
app-pgdata
➜  17-Pazynuyk-Ostap git:(main) ✗ docker run -d \                
  --name db \
  --network app-network \
  -e POSTGRES_DB=demo \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -v app-pgdata:/var/lib/postgresql/data \
  -v $(pwd)/db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro \
  postgres

6b78a853aa2baf49aefba32979588dfaba0be57329568768729b52e6c5854c3e
➜  17-Pazynuyk-Ostap git:(main) ✗ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                     NAMES
6b78a853aa2b   postgres                     "docker-entrypoint.s…"   3 minutes ago    Up 3 minutes    5432/tcp                                  db
f667ae314050   python-app:hw4-with-quotes   "venv_new/bin/python…"   14 minutes ago   Up 14 minutes   0.0.0.0:80->5000/tcp, [::]:80->5000/tcp   app
```

4. Перевірте відображення картинки
![Screenshot 2025-05-28 at 17.57.05.png](Screenshot%202025-05-28%20at%2017.57.05.png)
- Перезавантажив браузер і впевнився що картинка відображається

5. Перевірте збереження даних після перезапуску контейнерів
![Screenshot 2025-05-28 at 18.15.40.png](Screenshot%202025-05-28%20at%2018.15.40.png)
- Перезапустив контейнери і побачив що застосунок працює як і очікувалось зберігаючи дані
```aiignore
```aiignore
➜  17-Pazynuyk-Ostap git:(HW-4) curl http://127.0.0.1:80/  

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
    <p>Current time: 2025-05-28 15:15:17</p>
    <p>Database status: Connected</p>
    <p>Feature flags:</p>
    <ul>
        <li>USE_POSTGRES: True</li>
        <li>FAIL_AFTER_START: False</li>
    </ul>
    
    <div class="quote-block">
        <blockquote>"In the souls of the people the grapes of wrath are filling and growing heavy, growing heavy for the vintage."</blockquote>
        <p><strong>John Steinbeck</strong>, <em>The Grapes of Wrath</em></p>
    </div>
    
    <div class="image-container">
        <img src="/static/photo.jpg" alt="Demo Image">
    </div>
</body>
</html>%                                                                                                                                                                                       
```
