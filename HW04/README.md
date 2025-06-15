
Перевірте доступність веб-додатку за адресою http://localhost:80
![Screenshot 2025-05-28 at 18.12.11.png](Screenshot%202025-05-28%20at%2018.12.11.png)

Перевірте відсутність доступу до PostgreSQL за адресою http://localhost:5432
![Screenshot 2025-05-28 at 18.13.12.png](Screenshot%202025-05-28%20at%2018.13.12.png)

Перевірте відображення випадкових цитат (перезавантажте сторінку)
![Screenshot 2025-05-28 at 17.57.05.png](Screenshot%202025-05-28%20at%2017.57.05.png)
![Screenshot 2025-05-28 at 17.57.14.png](Screenshot%202025-05-28%20at%2017.57.14.png)
Перевірте відображення картинки
![Screenshot 2025-05-28 at 17.57.05.png](Screenshot%202025-05-28%20at%2017.57.05.png)

Перевірте збереження даних після перезапуску контейнерів
![Screenshot 2025-05-28 at 18.15.40.png](Screenshot%202025-05-28%20at%2018.15.40.png)


Логи виконання ДЗ (скорочені):
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
➜  17-Pazynuyk-Ostap git:(main) ✗ docker log db
docker: unknown command: docker log

Run 'docker --help' for more information
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
➜  17-Pazynuyk-Ostap git:(main) ✗ docker stop db          
db
➜  17-Pazynuyk-Ostap git:(main) ✗ docker remove db
db
➜  17-Pazynuyk-Ostap git:(main) ✗ docker run -d \                                      
  --name db \ 
  --network app-network \
  -e POSTGRES_DB=demo \      
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \  
  -v app-pgdata:/var/lib/postgresql/data \
  -v $(pwd)/db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro \
  postgres                     

7c8eb259d5f5eb803f32f5f3b41d47b96dcb75592ac9765cfa11501e1090cec6
➜  17-Pazynuyk-Ostap git:(main) ✗ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                                     NAMES
7c8eb259d5f5   postgres                     "docker-entrypoint.s…"   6 seconds ago   Up 5 seconds   5432/tcp                                  db
f667ae314050   python-app:hw4-with-quotes   "venv_new/bin/python…"   9 minutes ago   Up 9 minutes   0.0.0.0:80->5000/tcp, [::]:80->5000/tcp   app
➜  17-Pazynuyk-Ostap git:(main) ✗ docker logs app
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.0.3:5000
Press CTRL+C to quit
172.18.0.1 - - [28/May/2025 14:45:18] "GET / HTTP/1.1" 200 -
172.18.0.1 - - [28/May/2025 14:45:18] "GET /static/photo.jpg HTTP/1.1" 304 -
172.18.0.1 - - [28/May/2025 14:45:22] "GET / HTTP/1.1" 200 -
172.18.0.1 - - [28/May/2025 14:45:22] "GET /static/photo.jpg HTTP/1.1" 304 -
172.18.0.1 - - [28/May/2025 14:45:24] "GET / HTTP/1.1" 200 -
172.18.0.1 - - [28/May/2025 14:45:24] "GET /static/photo.jpg HTTP/1.1" 304 -
172.18.0.1 - - [28/May/2025 14:45:26] "GET / HTTP/1.1" 200 -
172.18.0.1 - - [28/May/2025 14:45:26] "GET /static/photo.jpg HTTP/1.1" 304 -
172.18.0.1 - - [28/May/2025 14:49:00] "GET / HTTP/1.1" 200 -
172.18.0.1 - - [28/May/2025 14:49:00] "GET /static/photo.jpg HTTP/1.1" 304 -
172.18.0.1 - - [28/May/2025 14:49:01] "GET / HTTP/1.1" 200 -
172.18.0.1 - - [28/May/2025 14:49:01] "GET /static/photo.jpg HTTP/1.1" 304 -
[2025-05-28 14:54:44,775] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "/app/venv_new/lib/python3.12/site-packages/flask/app.py", line 1463, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/venv_new/lib/python3.12/site-packages/flask/app.py", line 872, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/venv_new/lib/python3.12/site-packages/flask/app.py", line 870, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/venv_new/lib/python3.12/site-packages/flask/app.py", line 855, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app.py", line 116, in home
    quote = fetch_random_quote() if db_connected else None
            ^^^^^^^^^^^^^^^^^^^^
  File "/app/app.py", line 95, in fetch_random_quote
    cur.execute("""
psycopg2.errors.UndefinedTable: relation "quotes" does not exist
LINE 3:                 FROM quotes
                             ^

172.18.0.1 - - [28/May/2025 14:54:44] "GET / HTTP/1.1" 500 -
[2025-05-28 14:54:45,763] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "/app/venv_new/lib/python3.12/site-packages/flask/app.py", line 1463, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/venv_new/lib/python3.12/site-packages/flask/app.py", line 872, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/venv_new/lib/python3.12/site-packages/flask/app.py", line 870, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/venv_new/lib/python3.12/site-packages/flask/app.py", line 855, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app.py", line 116, in home
    quote = fetch_random_quote() if db_connected else None
            ^^^^^^^^^^^^^^^^^^^^
  File "/app/app.py", line 95, in fetch_random_quote
    cur.execute("""
psycopg2.errors.UndefinedTable: relation "quotes" does not exist
LINE 3:                 FROM quotes
                             ^

172.18.0.1 - - [28/May/2025 14:54:45] "GET / HTTP/1.1" 500 -
➜  17-Pazynuyk-Ostap git:(main) ✗ docker logs db

PostgreSQL Database directory appears to contain a database; Skipping initialization

2025-05-28 14:54:35.161 UTC [1] LOG:  starting PostgreSQL 17.5 (Debian 17.5-1.pgdg120+1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
2025-05-28 14:54:35.161 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2025-05-28 14:54:35.161 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2025-05-28 14:54:35.162 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2025-05-28 14:54:35.164 UTC [29] LOG:  database system was interrupted; last known up at 2025-05-28 14:52:30 UTC
2025-05-28 14:54:35.173 UTC [29] LOG:  database system was not properly shut down; automatic recovery in progress
2025-05-28 14:54:35.178 UTC [29] LOG:  redo starts at 0/14E4F98
2025-05-28 14:54:35.210 UTC [29] LOG:  invalid record length at 0/1908950: expected at least 24, got 0
2025-05-28 14:54:35.210 UTC [29] LOG:  redo done at 0/1908908 system usage: CPU: user: 0.00 s, system: 0.02 s, elapsed: 0.03 s
2025-05-28 14:54:35.212 UTC [27] LOG:  checkpoint starting: end-of-recovery immediate wait
2025-05-28 14:54:35.244 UTC [27] LOG:  checkpoint complete: wrote 921 buffers (5.6%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.030 s, sync=0.001 s, total=0.033 s; sync files=301, longest=0.001 s, average=0.001 s; distance=4238 kB, estimate=4238 kB; lsn=0/1908950, redo lsn=0/1908950
2025-05-28 14:54:35.247 UTC [1] LOG:  database system is ready to accept connections
2025-05-28 14:54:44.774 UTC [34] ERROR:  relation "quotes" does not exist at character 72
2025-05-28 14:54:44.774 UTC [34] STATEMENT:  
	                SELECT quote, work_title, author
	                FROM quotes
	                ORDER BY RANDOM()
	                LIMIT 1;
	            
2025-05-28 14:54:45.763 UTC [36] ERROR:  relation "quotes" does not exist at character 72
2025-05-28 14:54:45.763 UTC [36] STATEMENT:  
	                SELECT quote, work_title, author
	                FROM quotes
	                ORDER BY RANDOM()
	                LIMIT 1;
	            
➜  17-Pazynuyk-Ostap git:(main) ✗ docker volume rm app-pgdata    
Error response from daemon: remove app-pgdata: volume is in use - [7c8eb259d5f5eb803f32f5f3b41d47b96dcb75592ac9765cfa11501e1090cec6]
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
6b78a853aa2b   postgres                     "docker-entrypoint.s…"   3 seconds ago    Up 2 seconds    5432/tcp                                  db
f667ae314050   python-app:hw4-with-quotes   "venv_new/bin/python…"   10 minutes ago   Up 10 minutes   0.0.0.0:80->5000/tcp, [::]:80->5000/tcp   app
➜  17-Pazynuyk-Ostap git:(main) ✗ docker images
REPOSITORY             TAG               IMAGE ID       CREATED          SIZE
python-app             hw4-with-quotes   dbb539cdc08d   11 minutes ago   653MB
<none>                 <none>            def3a58009b4   13 minutes ago   653MB
<none>                 <none>            5ae300bd13de   17 minutes ago   653MB
<none>                 <none>            7ca22f28daba   20 minutes ago   653MB
<none>                 <none>            ae41b0e14ef7   23 minutes ago   653MB
<none>                 <none>            f67cb0c83c4f   29 minutes ago   653MB
hw4-start-python-app   latest            2c9d3dcda8dd   23 hours ago     653MB
hw4-start-python-app   start             2c9d3dcda8dd   23 hours ago     653MB
python-app             hw4-start         2c9d3dcda8dd   23 hours ago     653MB
opazyniuk/python-app   hw4-start         2c9d3dcda8dd   23 hours ago     653MB
postgres               latest            01b18d758935   6 days ago       459MB
➜  17-Pazynuyk-Ostap git:(main) ✗ docker volumes
docker: unknown command: docker volumes

Run 'docker --help' for more information
➜  17-Pazynuyk-Ostap git:(main) ✗ docker volume ps
docker: unknown command: docker volume ps

Usage:  docker volume COMMAND

Run 'docker volume --help' for more information
➜  17-Pazynuyk-Ostap git:(main) ✗ docker volume ls
DRIVER    VOLUME NAME
local     app-pgdata
➜  17-Pazynuyk-Ostap git:(main) ✗ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                     NAMES
6b78a853aa2b   postgres                     "docker-entrypoint.s…"   3 minutes ago    Up 3 minutes    5432/tcp                                  db
f667ae314050   python-app:hw4-with-quotes   "venv_new/bin/python…"   14 minutes ago   Up 14 minutes   0.0.0.0:80->5000/tcp, [::]:80->5000/tcp   app
➜  17-Pazynuyk-Ostap git:(HW-4) docker image prune -a
WARNING! This will remove all images without at least one container associated to them.
Are you sure you want to continue? [y/N] y
Deleted Images:
deleted: sha256:5ae300bd13de2a7e71a9a492c8c893066d92eb652ca6fc2aca82c729885394f7
deleted: sha256:def3a58009b48aa5811fbfe6ac99f3ec6dcb9ad9f386a5b7c2b58fedaece8d85
untagged: hw4-start-python-app:latest
untagged: hw4-start-python-app:start
untagged: python-app:hw4-start
untagged: opazyniuk/python-app:hw4-start
untagged: opazyniuk/python-app@sha256:88bc6672381cdc7250d09f77ae6bcfb1607c9c553f0089b7745369623d6dc09e
deleted: sha256:2c9d3dcda8dd529091dd53e990029e72b8d01a6e058b9763f7ddaec0930e7350
deleted: sha256:f67cb0c83c4f43b353dcd52a445150002a481cd85228954012bc59cc93241606
deleted: sha256:ae41b0e14ef7f2cd271b6c11a95c137b2fc4c1f4dc21ee72dac25e54d3f56952
deleted: sha256:7ca22f28dabaa90ee86fcc9b5aac5417277d7a8262f507b826832e066149cca8

Total reclaimed space: 0B
➜  17-Pazynuyk-Ostap git:(HW-4) docker images                                                                      
REPOSITORY   TAG               IMAGE ID       CREATED          SIZE
python-app   hw4-with-quotes   dbb539cdc08d   20 minutes ago   653MB
postgres     latest            01b18d758935   6 days ago       459MB
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
    <p>Current time: 2025-05-28 15:11:55</p>
    <p>Database status: Connected</p>
    <p>Feature flags:</p>
    <ul>
        <li>USE_POSTGRES: True</li>
        <li>FAIL_AFTER_START: False</li>
    </ul>
    
    <div class="quote-block">
        <blockquote>"Adjust the flower, adorn the bower, make sweet the honeyed hour."</blockquote>
        <p><strong>John Steinbeck</strong>, <em>Of Mice and Men</em></p>
    </div>
    
    <div class="image-container">
        <img src="/static/photo.jpg" alt="Demo Image">
    </div>
</body>
</html>%                                                                                                                                                                                       ➜  17-Pazynuyk-Ostap git:(HW-4) curl http://127.0.0.1:5432/
curl: (7) Failed to connect to 127.0.0.1 port 5432 after 0 ms: Could not connect to server
➜  17-Pazynuyk-Ostap git:(HW-4) docker stop db
db
➜  17-Pazynuyk-Ostap git:(HW-4) docker stop app
app
➜  17-Pazynuyk-Ostap git:(HW-4) docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
➜  17-Pazynuyk-Ostap git:(HW-4) docker start app
app
➜  17-Pazynuyk-Ostap git:(HW-4) docker start db 
db
➜  17-Pazynuyk-Ostap git:(HW-4) docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS         PORTS                                     NAMES
6b78a853aa2b   postgres                     "docker-entrypoint.s…"   19 minutes ago   Up 2 seconds   5432/tcp                                  db
f667ae314050   python-app:hw4-with-quotes   "venv_new/bin/python…"   30 minutes ago   Up 5 seconds   0.0.0.0:80->5000/tcp, [::]:80->5000/tcp   app
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
</html>%                                                                                                                                                                                       ➜  17-Pazynuyk-Ostap git:(HW-4) 

```
