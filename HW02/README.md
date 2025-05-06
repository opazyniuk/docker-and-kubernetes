# 17-Pazyniuk-Ostap

**Підготовка середовища**
- Перевірте поточну версію Docker у вашій системі:

```
ostap@ostap:~$ docker -v
Docker version 28.1.1, build 4eba377
```
![Screenshot 2025-05-06 at 21.04.29.png](Screenshot%202025-05-06%20at%2021.04.29.png)

**Отримання та перевірка образу**

- Завантажте образ enoot/r-d:0.0.1
![Screenshot 2025-05-06 at 21.17.03.png](Screenshot%202025-05-06%20at%2021.17.03.png)
```aiignore
ostap@ostap:~$ docker pull enoot/r-d:0.0.1
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.49/images/create?fromImage=docker.io%2Fenoot%2Fr-d&tag=0.0.1": dial unix /var/run/docker.sock: connect: permission denied
ostap@ostap:~$ docker pull enoot/r-d:0.0.1
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.49/images/create?fromImage=docker.io%2Fenoot%2Fr-d&tag=0.0.1": dial unix /var/run/docker.sock: connect: permission denied
ostap@ostap:~$ sudo groupadd docker
[sudo] password for ostap: 
groupadd: group 'docker' already exists
ostap@ostap:~$ sudo usermod -aG docker $USER
ostap@ostap:~$ docker pull enoot/r-d:0.0.1
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.49/images/create?fromImage=docker.io%2Fenoot%2Fr-d&tag=0.0.1": dial unix /var/run/docker.sock: connect: permission denied
ostap@ostap:~$ newgrp docker
ostap@ostap:~$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

ostap@ostap:~$ docker pull enoot/r-d:0.0.1
0.0.1: Pulling from enoot/r-d
943331d8a9a9: Pull complete 
df007eea74a3: Pull complete 
394dbe96ba14: Pull complete 
0e5ecbd2fab7: Pull complete 
fbcb18a0346c: Pull complete 
ac0765c1fae8: Pull complete 
8bb1a8959c0d: Pull complete 
f9e74d662acb: Pull complete 
Digest: sha256:c4ad9e66182d11219c2bcea22c08f8eb15772ee316c22bb33be7746826c9de76
Status: Downloaded newer image for enoot/r-d:0.0.1
docker.io/enoot/r-d:0.0.1
```
- Перевірте список завантажених образів
```aiignore
ostap@ostap:~$ docker ls
docker: unknown command: docker ls

Run 'docker --help' for more information
ostap@ostap:~$ docker image ls
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
enoot/r-d     0.0.1     aaeda3261b24   5 days ago     180MB
hello-world   latest    f1f77a0f96b7   3 months ago   5.2kB
ostap@ostap:~$ 
```

**Запуск та тестування**

- Запустіть контейнер у звичайному режимі на порту 1337
- Перевірте список запущених контейнерів
![Screenshot 2025-05-06 at 21.25.59.png](Screenshot%202025-05-06%20at%2021.25.59.png)
```aiignore
ostap@ostap:~$ docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
ostap@ostap:~$ docker run -d -p 1337:5000 aaeda3261b24
e895edd6a85e6d8375fb25cb1139c5ec766659fbeb07c39962f833a55bd240fd
ostap@ostap:~$ docker container ls
CONTAINER ID   IMAGE          COMMAND           CREATED         STATUS         PORTS                                         NAMES
e895edd6a85e   aaeda3261b24   "python app.py"   3 seconds ago   Up 3 seconds   0.0.0.0:1337->5000/tcp, [::]:1337->5000/tcp   youthful_spence
ostap@ostap:~$ 
```


**Експерименти з фоновим режимом**

- Запустіть контейнер у фоновому режимі на порту 1234 з ім'ям background-app
- Перевірте логи контейнера
- Запустіть ще один контейнер з рожевим фоном на порту 5678

```aiignore
ostap@ostap:~$ docker run -d -p 1337:5000 aaeda3261b24
e895edd6a85e6d8375fb25cb1139c5ec766659fbeb07c39962f833a55bd240fd
ostap@ostap:~$ docker container ls
CONTAINER ID   IMAGE          COMMAND           CREATED         STATUS         PORTS                                         NAMES
e895edd6a85e   aaeda3261b24   "python app.py"   3 seconds ago   Up 3 seconds   0.0.0.0:1337->5000/tcp, [::]:1337->5000/tcp   youthful_spence
ostap@ostap:~$ docker run -d -p 1234:5000 --name ostap-python-app enoot/r-d
Unable to find image 'enoot/r-d:latest' locally
docker: Error response from daemon: manifest for enoot/r-d:latest not found: manifest unknown: manifest unknown

Run 'docker run --help' for more information
ostap@ostap:~$ docker run -d -p 1234:5000 --name ostap-python-app enoot/r-d:0.0.1
09073b838bdedc896ec3e39a65ac88f8ecc37fe32b0f529bc38de485a6852e7b
ostap@ostap:~$ docker stop ostap-python-app
ostap-python-app
ostap@ostap:~$ docker run -d -p 1234:5000 --name background-app enoot/r-d:0.0.1
bac9709488862d10862d01130ab16e83ec318bbcdd86a8ed84a328f8ee46bc52
ostap@ostap:~$ docker container ls
CONTAINER ID   IMAGE             COMMAND           CREATED          STATUS          PORTS                                         NAMES
bac970948886   enoot/r-d:0.0.1   "python app.py"   7 seconds ago    Up 7 seconds    0.0.0.0:1234->5000/tcp, [::]:1234->5000/tcp   background-app
e895edd6a85e   aaeda3261b24      "python app.py"   15 minutes ago   Up 15 minutes   0.0.0.0:1337->5000/tcp, [::]:1337->5000/tcp   youthful_spence
ostap@ostap:~$ docker logs background-app
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.3:5000
Press CTRL+C to quit
ostap@ostap:~$ docker run -d -p 5678:5000 --name background-app enoot/r-d:0.0.1
docker: Error response from daemon: Conflict. The container name "/background-app" is already in use by container "bac9709488862d10862d01130ab16e83ec318bbcdd86a8ed84a328f8ee46bc52". You have to remove (or rename) that container to be able to reuse that name.

Run 'docker run --help' for more information
ostap@ostap:~$ docker run -d -p 5678:5000 --name background-app-2 enoot/r-d:0.0.1
f9cfc5f545c8f371fe6914f4c9c53985a6e9c0dc7786067f0b0be86b5f5dfeae
ostap@ostap:~$ docker container ls
CONTAINER ID   IMAGE             COMMAND           CREATED          STATUS          PORTS                                         NAMES
f9cfc5f545c8   enoot/r-d:0.0.1   "python app.py"   3 seconds ago    Up 3 seconds    0.0.0.0:5678->5000/tcp, [::]:5678->5000/tcp   background-app-2
bac970948886   enoot/r-d:0.0.1   "python app.py"   2 minutes ago    Up 2 minutes    0.0.0.0:1234->5000/tcp, [::]:1234->5000/tcp   background-app
e895edd6a85e   aaeda3261b24      "python app.py"   18 minutes ago   Up 18 minutes   0.0.0.0:1337->5000/tcp, [::]:1337->5000/tcp   youthful_spence
ostap@ostap:~$ docker run -d -p 5678:5000 -e BACKGROUND_COLOR=#FF8DA1 --name background-app-2 enoot/r-d:0.0.1
docker: Error response from daemon: Conflict. The container name "/background-app-2" is already in use by container "f9cfc5f545c8f371fe6914f4c9c53985a6e9c0dc7786067f0b0be86b5f5dfeae". You have to remove (or rename) that container to be able to reuse that name.

Run 'docker run --help' for more information
ostap@ostap:~$ docker stop background-app-2
background-app-2
ostap@ostap:~$ docker run -d -p 5678:5000 -e BACKGROUND_COLOR=#FF8DA1 --name background-app-2 enoot/r-d:0.0.1
docker: Error response from daemon: Conflict. The container name "/background-app-2" is already in use by container "f9cfc5f545c8f371fe6914f4c9c53985a6e9c0dc7786067f0b0be86b5f5dfeae". You have to remove (or rename) that container to be able to reuse that name.

Run 'docker run --help' for more information
ostap@ostap:~$ docker container ls
CONTAINER ID   IMAGE             COMMAND           CREATED          STATUS          PORTS                                         NAMES
bac970948886   enoot/r-d:0.0.1   "python app.py"   7 minutes ago    Up 7 minutes    0.0.0.0:1234->5000/tcp, [::]:1234->5000/tcp   background-app
e895edd6a85e   aaeda3261b24      "python app.py"   23 minutes ago   Up 23 minutes   0.0.0.0:1337->5000/tcp, [::]:1337->5000/tcp   youthful_spence
ostap@ostap:~$ docker run -d -p 5678:5000 -e BACKGROUND_COLOR=#FF8DA1 --name background-app-2 enoot/r-d:0.0.1
docker: Error response from daemon: Conflict. The container name "/background-app-2" is already in use by container "f9cfc5f545c8f371fe6914f4c9c53985a6e9c0dc7786067f0b0be86b5f5dfeae". You have to remove (or rename) that container to be able to reuse that name.

Run 'docker run --help' for more information
ostap@ostap:~$ docker container ls
CONTAINER ID   IMAGE             COMMAND           CREATED          STATUS          PORTS                                         NAMES
bac970948886   enoot/r-d:0.0.1   "python app.py"   8 minutes ago    Up 8 minutes    0.0.0.0:1234->5000/tcp, [::]:1234->5000/tcp   background-app
e895edd6a85e   aaeda3261b24      "python app.py"   23 minutes ago   Up 23 minutes   0.0.0.0:1337->5000/tcp, [::]:1337->5000/tcp   youthful_spence
ostap@ostap:~$ docker run -d -p 5678:5000 -e BACKGROUND_COLOR=#FF8DA1 --name background-app-pink enoot/r-d:0.0.1
8870a74f3f60e281cab303e1c5e3844ac4d5c92e362c1f49b4ae6883b80d1b8b
ostap@ostap:~$ docker container ls
CONTAINER ID   IMAGE             COMMAND           CREATED          STATUS          PORTS                                         NAMES
8870a74f3f60   enoot/r-d:0.0.1   "python app.py"   2 seconds ago    Up 2 seconds    0.0.0.0:5678->5000/tcp, [::]:5678->5000/tcp   background-app-pink
bac970948886   enoot/r-d:0.0.1   "python app.py"   8 minutes ago    Up 8 minutes    0.0.0.0:1234->5000/tcp, [::]:1234->5000/tcp   background-app
e895edd6a85e   aaeda3261b24      "python app.py"   24 minutes ago   Up 24 minutes   0.0.0.0:1337->5000/tcp, [::]:1337->5000/tcp   youthful_spence
```
![Screenshot 2025-05-06 at 21.53.37.png](Screenshot%202025-05-06%20at%2021.53.37.png)
![Screenshot 2025-05-06 at 21.54.06.png](Screenshot%202025-05-06%20at%2021.54.06.png)
![Screenshot 2025-05-06 at 21.54.17.png](Screenshot%202025-05-06%20at%2021.54.17.png)

**Керування контейнерами**

- Зупиніть один з працюючих контейнерів
- Перевірте список всіх контейнерів (включно із зупиненими)
- Видаліть зупинений контейнер

**Очищення ресурсів**

- Зупиніть всі контейнери
- Видаліть всі контейнери
- Видаліть образ enoot/r-d:0.0.1
```aiignore
ostap@ostap:~$ docker container ls
CONTAINER ID   IMAGE             COMMAND           CREATED          STATUS          PORTS                                         NAMES
8870a74f3f60   enoot/r-d:0.0.1   "python app.py"   2 seconds ago    Up 2 seconds    0.0.0.0:5678->5000/tcp, [::]:5678->5000/tcp   background-app-pink
bac970948886   enoot/r-d:0.0.1   "python app.py"   8 minutes ago    Up 8 minutes    0.0.0.0:1234->5000/tcp, [::]:1234->5000/tcp   background-app
e895edd6a85e   aaeda3261b24      "python app.py"   24 minutes ago   Up 24 minutes   0.0.0.0:1337->5000/tcp, [::]:1337->5000/tcp   youthful_spence
ostap@ostap:~$ docker stop background-app-pink
background-app-pink
ostap@ostap:~$ docker stop background-app
background-app
ostap@ostap:~$ docker stop youthful_spence
youthful_spence
ostap@ostap:~$ docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
ostap@ostap:~$ docker ps --filter "status=exited"
CONTAINER ID   IMAGE             COMMAND           CREATED          STATUS                            PORTS     NAMES
8870a74f3f60   enoot/r-d:0.0.1   "python app.py"   10 minutes ago   Exited (137) 2 minutes ago                  background-app-pink
f9cfc5f545c8   enoot/r-d:0.0.1   "python app.py"   16 minutes ago   Exited (137) 11 minutes ago                 background-app-2
bac970948886   enoot/r-d:0.0.1   "python app.py"   19 minutes ago   Exited (137) About a minute ago             background-app
09073b838bde   enoot/r-d:0.0.1   "python app.py"   20 minutes ago   Exited (137) 19 minutes ago                 ostap-python-app
e895edd6a85e   aaeda3261b24      "python app.py"   34 minutes ago   Exited (137) About a minute ago             youthful_spence
461f77084822   aaeda3261b24      "python app.py"   36 minutes ago   Exited (137) 35 minutes ago                 fervent_margulis
35c61bc7a624   hello-world       "/hello"          43 minutes ago   Exited (0) 43 minutes ago                   hopeful_cannon
5d15c5932c09   hello-world       "/hello"          28 hours ago     Exited (0) 28 hours ago                     competent_kepler
ostap@ostap:~$ sudo docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs sudo docker rm
[sudo] password for ostap: 
8870a74f3f60
f9cfc5f545c8
bac970948886
09073b838bde
e895edd6a85e
461f77084822
35c61bc7a624
5d15c5932c09
ostap@ostap:~$ docker ps --filter "status=exited"
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
ostap@ostap:~$ docker image ps
docker: unknown command: docker image ps

Usage:  docker image

Run 'docker image --help' for more information
ostap@ostap:~$ docker image ls
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
enoot/r-d     0.0.1     aaeda3261b24   5 days ago     180MB
hello-world   latest    f1f77a0f96b7   3 months ago   5.2kB
ostap@ostap:~$ docker image rm aaeda3261b24
Untagged: enoot/r-d:0.0.1
Untagged: enoot/r-d@sha256:c4ad9e66182d11219c2bcea22c08f8eb15772ee316c22bb33be7746826c9de76
Deleted: sha256:aaeda3261b240890dfc22020eb024ee152025137669a2aebb89a976a0d0f9a33
Deleted: sha256:40d1d8f1dff347adabb3934d80837e0e9b2e380d7d27d5f107537547b3438eac
Deleted: sha256:4be0ff182132b3ac68f11740fdfb564f58173caf0133e3c0385be90c7f2cc114
Deleted: sha256:826d28ef96d66b32b4ab0af91a0cf64cb6d8f141049ab1be0e9f6c3a9eee2a97
Deleted: sha256:d5d70a87cd9603180f44f522a720088c54834c44757339bc9dcf73a40cfb9139
Deleted: sha256:4a0e85ad15aa9b5bc29ee6301e80688afee0918702f7fdc1ec97aeaa49690685
Deleted: sha256:002d8625c0cfb673c34a706de011d88c0f6df043bc0d9b5e5e731b1cd680b3c6
Deleted: sha256:fcef40e3c81ab3ebaacc8e45ce6c1719f2626dbfe3bd8880ac0e05fe46cabd9a
```

![Screenshot 2025-05-06 at 22.01.50.png](Screenshot%202025-05-06%20at%2022.01.50.png)


**Очікувані результати**
- Скріншоти виконання кожного пункту завдання
  - Додано після кожного завдання зверху
- Короткий опис виконаних дій
  - Скачав та налаштував докер та виконав базові команди з керування ним
- Опис будь-яких проблем, з якими ви зіткнулися
  - Оновив права для root користувача у віртуальній машині, щоб він мав можливість стягувти образи з докера;
  - Налаштування змінних середовища через докер;
  - Забув спочатку вказати версійність при розгортанні образу.
