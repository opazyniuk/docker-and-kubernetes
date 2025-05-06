# 17-Pazyniuk-Ostap


Запущений сервіс без змін
![Screenshot 2025-05-03 at 10.33.22.png](Screenshot%202025-05-03%20at%2010.33.22.png)

Запущений сервіс з змінами
![Screenshot 2025-05-03 at 10.19.33.png](Screenshot%202025-05-03%20at%2010.19.33.png)

Логи запущеного застосунку без змін
```ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ code
ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (main)$ python3 -m venv venv
ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (main)$ source venv/bin/activate
(venv) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (main)$ export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
(venv) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (main)$ pip install -r requirements.txt
Requirement already satisfied: flask==3.0.1 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 1)) (3.0.1)
Requirement already satisfied: psycopg2-binary==2.9.8 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 2)) (2.9.8)
Requirement already satisfied: Werkzeug>=3.0.0 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from flask==3.0.1->-r requirements.txt (line 1)) (3.0.6)
Requirement already satisfied: Jinja2>=3.1.2 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from flask==3.0.1->-r requirements.txt (line 1)) (3.1.6)
Requirement already satisfied: itsdangerous>=2.1.2 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from flask==3.0.1->-r requirements.txt (line 1)) (2.2.0)
Requirement already satisfied: click>=8.1.3 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from flask==3.0.1->-r requirements.txt (line 1)) (8.1.8)
Requirement already satisfied: blinker>=1.6.2 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from flask==3.0.1->-r requirements.txt (line 1)) (1.8.2)
Requirement already satisfied: importlib-metadata>=3.6.0 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from flask==3.0.1->-r requirements.txt (line 1)) (8.5.0)
Requirement already satisfied: zipp>=3.20 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from importlib-metadata>=3.6.0->flask==3.0.1->-r requirements.txt (line 1)) (3.20.2)
Requirement already satisfied: MarkupSafe>=2.0 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from Jinja2>=3.1.2->flask==3.0.1->-r requirements.txt (line 1)) (2.1.5)
(venv) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (main)$ PORT=5001 python app.py
* Serving Flask app 'app'
* Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5001
* Running on http://10.0.2.15:5001
  Press CTRL+C to quit
  127.0.0.1 - - [03/May/2025 07:32:25] "GET / HTTP/1.1" 200 -
  127.0.0.1 - - [03/May/2025 07:32:25] "GET /static/photo.jpg HTTP/1.1" 200 -
  127.0.0.1 - - [03/May/2025 07:33:03] "GET / HTTP/1.1" 200 -
  127.0.0.1 - - [03/May/2025 07:33:03] "GET /static/photo.jpg HTTP/1.1" 404 -
```

Логи запущеного застосунку з змінами
```aiignore
ostap@ostap:~$ cd 
.cache/        Desktop/       Documents/     .gnupg/        Music/         .pki/          .pyenv/        .ssh/          Videos/        
.config/       devops_course/ Downloads/     .local/        Pictures/      Public/        snap/          Templates/     .vscode/       
ostap@ostap:~$ cd devops_course/
ostap@ostap:~/devops_course$ cd
cd                 cd-create-profile  cd-fix-profile     cd-iccdump         cd-it8             
ostap@ostap:~/devops_course$ cd
cd                 cd-create-profile  cd-fix-profile     cd-iccdump         cd-it8             
ostap@ostap:~/devops_course$ cd 
17-Pazynuyk-Ostap/                 DOCKER-AND-KUBERNETES_MARTYNIUK_1/ 
ostap@ostap:~/devops_course$ cd DOCKER-AND-KUBERNETES_MARTYNIUK_1/
ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ python3 -m venv venv_new
ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ 
ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ source venv_new/bin/activate
(venv_new) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ pip install -r requirements.txt
Collecting blinker==1.8.2 (from -r requirements.txt (line 1))
  Downloading blinker-1.8.2-py3-none-any.whl.metadata (1.6 kB)
Collecting click==8.1.8 (from -r requirements.txt (line 2))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting flask==3.0.1 (from -r requirements.txt (line 3))
  Using cached flask-3.0.1-py3-none-any.whl.metadata (3.6 kB)
Collecting importlib-metadata==8.5.0 (from -r requirements.txt (line 4))
  Downloading importlib_metadata-8.5.0-py3-none-any.whl.metadata (4.8 kB)
Collecting itsdangerous==2.2.0 (from -r requirements.txt (line 5))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2==3.1.6 (from -r requirements.txt (line 6))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting MarkupSafe==2.1.5 (from -r requirements.txt (line 7))
  Downloading MarkupSafe-2.1.5.tar.gz (19 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting psycopg2-binary==2.9.8 (from -r requirements.txt (line 8))
  Using cached psycopg2-binary-2.9.8.tar.gz (383 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting werkzeug==3.0.6 (from -r requirements.txt (line 9))
  Downloading werkzeug-3.0.6-py3-none-any.whl.metadata (3.7 kB)
Collecting zipp==3.20.2 (from -r requirements.txt (line 10))
  Downloading zipp-3.20.2-py3-none-any.whl.metadata (3.7 kB)
Downloading blinker-1.8.2-py3-none-any.whl (9.5 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached flask-3.0.1-py3-none-any.whl (101 kB)
Downloading importlib_metadata-8.5.0-py3-none-any.whl (26 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading werkzeug-3.0.6-py3-none-any.whl (227 kB)
Downloading zipp-3.20.2-py3-none-any.whl (9.2 kB)
Building wheels for collected packages: MarkupSafe, psycopg2-binary
  Building wheel for MarkupSafe (pyproject.toml) ... done
  Created wheel for MarkupSafe: filename=markupsafe-2.1.5-cp313-cp313-linux_aarch64.whl size=28658 sha256=07ce047fff73dc4b476b529a98d087b119ee79f5abca0325cbe2a1982f746cef
  Stored in directory: /home/ostap/.cache/pip/wheels/c2/0c/c0/d6d953ac80cacc2dd1d329d675c67d1e7775bad02a8faedef0
  Building wheel for psycopg2-binary (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for psycopg2-binary (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [143 lines of output]
      /tmp/pip-build-env-pn9wutp5/overlay/lib/python3.13/site-packages/setuptools/dist.py:759: SetuptoolsDeprecationWarning: License classifiers are deprecated.
      !!
      
              ********************************************************************************
              Please consider removing the following classifiers in favor of a SPDX license expression:
      
              License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
      
              See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
              ********************************************************************************
      
      !!
        self._finalize_license_expression()
      running bdist_wheel
      running build
      running build_py
      creating build/lib.linux-aarch64-cpython-313/psycopg2
      copying lib/tz.py -> build/lib.linux-aarch64-cpython-313/psycopg2
      copying lib/sql.py -> build/lib.linux-aarch64-cpython-313/psycopg2
      copying lib/pool.py -> build/lib.linux-aarch64-cpython-313/psycopg2
      copying lib/extras.py -> build/lib.linux-aarch64-cpython-313/psycopg2
      copying lib/extensions.py -> build/lib.linux-aarch64-cpython-313/psycopg2
      copying lib/errors.py -> build/lib.linux-aarch64-cpython-313/psycopg2
      copying lib/errorcodes.py -> build/lib.linux-aarch64-cpython-313/psycopg2
      copying lib/_range.py -> build/lib.linux-aarch64-cpython-313/psycopg2
      copying lib/_json.py -> build/lib.linux-aarch64-cpython-313/psycopg2
      copying lib/_ipaddress.py -> build/lib.linux-aarch64-cpython-313/psycopg2
      copying lib/__init__.py -> build/lib.linux-aarch64-cpython-313/psycopg2
      running build_ext
      building 'psycopg2._psycopg' extension
      creating build/temp.linux-aarch64-cpython-313/psycopg
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/adapter_asis.c -o build/temp.linux-aarch64-cpython-313/psycopg/adapter_asis.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/adapter_binary.c -o build/temp.linux-aarch64-cpython-313/psycopg/adapter_binary.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/adapter_datetime.c -o build/temp.linux-aarch64-cpython-313/psycopg/adapter_datetime.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/adapter_list.c -o build/temp.linux-aarch64-cpython-313/psycopg/adapter_list.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/adapter_pboolean.c -o build/temp.linux-aarch64-cpython-313/psycopg/adapter_pboolean.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/adapter_pdecimal.c -o build/temp.linux-aarch64-cpython-313/psycopg/adapter_pdecimal.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/adapter_pfloat.c -o build/temp.linux-aarch64-cpython-313/psycopg/adapter_pfloat.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/adapter_pint.c -o build/temp.linux-aarch64-cpython-313/psycopg/adapter_pint.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/adapter_qstring.c -o build/temp.linux-aarch64-cpython-313/psycopg/adapter_qstring.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/aix_support.c -o build/temp.linux-aarch64-cpython-313/psycopg/aix_support.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/bytes_format.c -o build/temp.linux-aarch64-cpython-313/psycopg/bytes_format.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/column_type.c -o build/temp.linux-aarch64-cpython-313/psycopg/column_type.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/connection_int.c -o build/temp.linux-aarch64-cpython-313/psycopg/connection_int.o -Wdeclaration-after-statement
      psycopg/connection_int.c: In function ‘_conn_get_async_cursor’:
      psycopg/connection_int.c:1050:5: warning: ‘PyWeakref_GetObject’ is deprecated [-Wdeprecated-declarations]
       1050 |     if (!(py_curs = PyWeakref_GetObject(self->async_cursor))) {
            |     ^~
      In file included from /usr/include/python3.13/Python.h:113,
                       from ./psycopg/psycopg.h:35,
                       from psycopg/connection_int.c:28:
      /usr/include/python3.13/weakrefobject.h:30:44: note: declared here
         30 | Py_DEPRECATED(3.13) PyAPI_FUNC(PyObject *) PyWeakref_GetObject(PyObject *ref);
            |                                            ^~~~~~~~~~~~~~~~~~~
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/connection_type.c -o build/temp.linux-aarch64-cpython-313/psycopg/connection_type.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/conninfo_type.c -o build/temp.linux-aarch64-cpython-313/psycopg/conninfo_type.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/cursor_int.c -o build/temp.linux-aarch64-cpython-313/psycopg/cursor_int.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/cursor_type.c -o build/temp.linux-aarch64-cpython-313/psycopg/cursor_type.o -Wdeclaration-after-statement
      psycopg/cursor_type.c: In function ‘curs_fetchone’:
      psycopg/cursor_type.c:782:9: warning: ‘PyWeakref_GetObject’ is deprecated [-Wdeprecated-declarations]
        782 |         && PyWeakref_GetObject(self->conn->async_cursor) == (PyObject*)self)
            |         ^~
      In file included from /usr/include/python3.13/Python.h:113,
                       from ./psycopg/psycopg.h:35,
                       from psycopg/cursor_type.c:28:
      /usr/include/python3.13/weakrefobject.h:30:44: note: declared here
         30 | Py_DEPRECATED(3.13) PyAPI_FUNC(PyObject *) PyWeakref_GetObject(PyObject *ref);
            |                                            ^~~~~~~~~~~~~~~~~~~
      psycopg/cursor_type.c: In function ‘curs_next_named’:
      psycopg/cursor_type.c:829:9: warning: ‘PyWeakref_GetObject’ is deprecated [-Wdeprecated-declarations]
        829 |         && PyWeakref_GetObject(self->conn->async_cursor) == (PyObject*)self)
            |         ^~
      /usr/include/python3.13/weakrefobject.h:30:44: note: declared here
         30 | Py_DEPRECATED(3.13) PyAPI_FUNC(PyObject *) PyWeakref_GetObject(PyObject *ref);
            |                                            ^~~~~~~~~~~~~~~~~~~
      psycopg/cursor_type.c: In function ‘curs_fetchmany’:
      psycopg/cursor_type.c:914:9: warning: ‘PyWeakref_GetObject’ is deprecated [-Wdeprecated-declarations]
        914 |         && PyWeakref_GetObject(self->conn->async_cursor) == (PyObject*)self)
            |         ^~
      /usr/include/python3.13/weakrefobject.h:30:44: note: declared here
         30 | Py_DEPRECATED(3.13) PyAPI_FUNC(PyObject *) PyWeakref_GetObject(PyObject *ref);
            |                                            ^~~~~~~~~~~~~~~~~~~
      psycopg/cursor_type.c: In function ‘curs_fetchall’:
      psycopg/cursor_type.c:983:9: warning: ‘PyWeakref_GetObject’ is deprecated [-Wdeprecated-declarations]
        983 |         && PyWeakref_GetObject(self->conn->async_cursor) == (PyObject*)self)
            |         ^~
      /usr/include/python3.13/weakrefobject.h:30:44: note: declared here
         30 | Py_DEPRECATED(3.13) PyAPI_FUNC(PyObject *) PyWeakref_GetObject(PyObject *ref);
            |                                            ^~~~~~~~~~~~~~~~~~~
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/diagnostics_type.c -o build/temp.linux-aarch64-cpython-313/psycopg/diagnostics_type.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/error_type.c -o build/temp.linux-aarch64-cpython-313/psycopg/error_type.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/green.c -o build/temp.linux-aarch64-cpython-313/psycopg/green.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/libpq_support.c -o build/temp.linux-aarch64-cpython-313/psycopg/libpq_support.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/lobject_int.c -o build/temp.linux-aarch64-cpython-313/psycopg/lobject_int.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/lobject_type.c -o build/temp.linux-aarch64-cpython-313/psycopg/lobject_type.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/microprotocols.c -o build/temp.linux-aarch64-cpython-313/psycopg/microprotocols.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/microprotocols_proto.c -o build/temp.linux-aarch64-cpython-313/psycopg/microprotocols_proto.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/notify_type.c -o build/temp.linux-aarch64-cpython-313/psycopg/notify_type.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/pqpath.c -o build/temp.linux-aarch64-cpython-313/psycopg/pqpath.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/psycopgmodule.c -o build/temp.linux-aarch64-cpython-313/psycopg/psycopgmodule.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/replication_connection_type.c -o build/temp.linux-aarch64-cpython-313/psycopg/replication_connection_type.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/replication_cursor_type.c -o build/temp.linux-aarch64-cpython-313/psycopg/replication_cursor_type.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/replication_message_type.c -o build/temp.linux-aarch64-cpython-313/psycopg/replication_message_type.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/solaris_support.c -o build/temp.linux-aarch64-cpython-313/psycopg/solaris_support.o -Wdeclaration-after-statement
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/typecast.c -o build/temp.linux-aarch64-cpython-313/psycopg/typecast.o -Wdeclaration-after-statement
      In file included from ./psycopg/psycopg.h:38,
                       from psycopg/typecast.c:28:
      In function ‘typecast_array_scan’,
          inlined from ‘typecast_GENERIC_ARRAY_cast’ at ./psycopg/typecast_array.c:275:9:
      ./psycopg/config.h:58:25: warning: ‘%s’ directive argument is null [-Wformat-overflow=]
         58 |         fprintf(stderr, "[%d] " fmt "\n", (int) getpid() , ## args)
            |                         ^~~~~~~
      ./psycopg/typecast_array.c:185:9: note: in expansion of macro ‘Dprintf’
        185 |         Dprintf("typecast_array_scan: state = %d,"
            |         ^~~~~~~
      ./psycopg/config.h:58:25: warning: ‘%s’ directive argument is null [-Wformat-overflow=]
         58 |         fprintf(stderr, "[%d] " fmt "\n", (int) getpid() , ## args)
            |                         ^~~~~~~
      ./psycopg/typecast_array.c:185:9: note: in expansion of macro ‘Dprintf’
        185 |         Dprintf("typecast_array_scan: state = %d,"
            |         ^~~~~~~
      ./psycopg/config.h:58:25: warning: ‘%s’ directive argument is null [-Wformat-overflow=]
         58 |         fprintf(stderr, "[%d] " fmt "\n", (int) getpid() , ## args)
            |                         ^~~~~~~
      ./psycopg/typecast_array.c:185:9: note: in expansion of macro ‘Dprintf’
        185 |         Dprintf("typecast_array_scan: state = %d,"
            |         ^~~~~~~
      ./psycopg/config.h:58:25: warning: ‘%s’ directive argument is null [-Wformat-overflow=]
         58 |         fprintf(stderr, "[%d] " fmt "\n", (int) getpid() , ## args)
            |                         ^~~~~~~
      ./psycopg/typecast_array.c:185:9: note: in expansion of macro ‘Dprintf’
        185 |         Dprintf("typecast_array_scan: state = %d,"
            |         ^~~~~~~
      aarch64-linux-gnu-gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC "-DPSYCOPG_VERSION=2.9.8 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1 -DPG_VERSION_NUM=170004 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1 -I/home/ostap/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1/venv_new/include -I/usr/include/python3.13 -I. -I/usr/include/postgresql -I/usr/include/postgresql/17/server -I/usr/include/libxml2 -c psycopg/utils.c -o build/temp.linux-aarch64-cpython-313/psycopg/utils.o -Wdeclaration-after-statement
      psycopg/utils.c: In function ‘psyco_is_main_interp’:
      psycopg/utils.c:397:12: error: implicit declaration of function ‘_PyInterpreterState_Get’; did you mean ‘PyInterpreterState_Get’? [-Wimplicit-function-declaration]
        397 |     return _PyInterpreterState_Get() == PyInterpreterState_Main();
            |            ^~~~~~~~~~~~~~~~~~~~~~~
            |            PyInterpreterState_Get
      psycopg/utils.c:397:38: warning: comparison between pointer and integer
        397 |     return _PyInterpreterState_Get() == PyInterpreterState_Main();
            |                                      ^~
      error: command '/usr/bin/aarch64-linux-gnu-gcc' failed with exit code 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for psycopg2-binary
Successfully built MarkupSafe
Failed to build psycopg2-binary
ERROR: Failed to build installable wheels for some pyproject.toml based projects (psycopg2-binary)
(venv_new) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
(venv_new) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ pip install -r requirements.txt
Requirement already satisfied: blinker==1.8.2 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 1)) (1.8.2)
Requirement already satisfied: click==8.1.8 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 2)) (8.1.8)
Requirement already satisfied: flask==3.0.1 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 3)) (3.0.1)
Requirement already satisfied: importlib-metadata==8.5.0 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 4)) (8.5.0)
Requirement already satisfied: itsdangerous==2.2.0 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 5)) (2.2.0)
Requirement already satisfied: jinja2==3.1.6 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 6)) (3.1.6)
Requirement already satisfied: MarkupSafe==2.1.5 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 7)) (2.1.5)
Requirement already satisfied: psycopg2-binary==2.9.8 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 8)) (2.9.8)
Requirement already satisfied: werkzeug==3.0.6 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 9)) (3.0.6)
Requirement already satisfied: zipp==3.20.2 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 10)) (3.20.2)
WARNING: You are using pip version 21.1.1; however, version 25.0.1 is available.
You should consider upgrading via the '/home/ostap/.pyenv/versions/3.8.10/bin/python3.8 -m pip install --upgrade pip' command.
(venv_new) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ pip install -r requirements.txt
Requirement already satisfied: blinker==1.8.2 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 1)) (1.8.2)
Requirement already satisfied: click==8.1.8 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 2)) (8.1.8)
Requirement already satisfied: flask==3.0.1 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 3)) (3.0.1)
Requirement already satisfied: importlib-metadata==8.5.0 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 4)) (8.5.0)
Requirement already satisfied: itsdangerous==2.2.0 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 5)) (2.2.0)
Requirement already satisfied: jinja2==3.1.6 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 6)) (3.1.6)
Requirement already satisfied: MarkupSafe==2.1.5 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 7)) (2.1.5)
Requirement already satisfied: psycopg2-binary==2.9.8 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 8)) (2.9.8)
Requirement already satisfied: werkzeug==3.0.6 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 9)) (3.0.6)
Requirement already satisfied: zipp==3.20.2 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 10)) (3.20.2)
WARNING: You are using pip version 21.1.1; however, version 25.0.1 is available.
You should consider upgrading via the '/home/ostap/.pyenv/versions/3.8.10/bin/python3.8 -m pip install --upgrade pip' command.
(venv_new) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ /home/ostap/.pyenv/versions/3.8.10/bin/python3.8 -m pip install --upgrade pip'
> 
> '
Requirement already satisfied: pip in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (21.1.1)
Collecting pip
  Downloading pip-25.0.1-py3-none-any.whl (1.8 MB)
     |████████████████████████████████| 1.8 MB 1.1 MB/s 
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.1.1
    Uninstalling pip-21.1.1:
      Successfully uninstalled pip-21.1.1
Successfully installed pip-25.0.1
(venv_new) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ pip install -r requirements.txt
Requirement already satisfied: blinker==1.8.2 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 1)) (1.8.2)
Requirement already satisfied: click==8.1.8 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 2)) (8.1.8)
Requirement already satisfied: flask==3.0.1 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 3)) (3.0.1)
Requirement already satisfied: importlib-metadata==8.5.0 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 4)) (8.5.0)
Requirement already satisfied: itsdangerous==2.2.0 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 5)) (2.2.0)
Requirement already satisfied: jinja2==3.1.6 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 6)) (3.1.6)
Requirement already satisfied: MarkupSafe==2.1.5 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 7)) (2.1.5)
Requirement already satisfied: psycopg2-binary==2.9.8 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 8)) (2.9.8)
Requirement already satisfied: werkzeug==3.0.6 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 9)) (3.0.6)
Requirement already satisfied: zipp==3.20.2 in /home/ostap/.pyenv/versions/3.8.10/lib/python3.8/site-packages (from -r requirements.txt (line 10)) (3.20.2)
(venv_new) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ python --version
Python 3.8.10
(venv_new) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.2.15:5000
Press CTRL+C to quit
127.0.0.1 - - [03/May/2025 07:04:57] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/May/2025 07:04:57] "GET /static/photo.jpg HTTP/1.1" 404 -
127.0.0.1 - - [03/May/2025 07:04:59] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/May/2025 07:04:59] "GET /static/photo.jpg HTTP/1.1" 404 -
127.0.0.1 - - [03/May/2025 07:05:06] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/May/2025 07:05:06] "GET /static/photo.jpg HTTP/1.1" 404 -
127.0.0.1 - - [03/May/2025 07:05:13] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/May/2025 07:05:13] "GET /static/photo.jpg HTTP/1.1" 404 -
127.0.0.1 - - [03/May/2025 07:09:46] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/May/2025 07:09:46] "GET /static/photo.jpg HTTP/1.1" 404 -
127.0.0.1 - - [03/May/2025 07:09:46] "GET /static/photo.jpg HTTP/1.1" 404 -
127.0.0.1 - - [03/May/2025 07:12:38] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/May/2025 07:12:38] "GET /static/photo.jpg HTTP/1.1" 404 -
127.0.0.1 - - [03/May/2025 07:13:14] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/May/2025 07:13:14] "GET /static/photo.jpg HTTP/1.1" 404 -

^C(venv_new) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.2.15:5000
Press CTRL+C to quit
127.0.0.1 - - [03/May/2025 07:15:08] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/May/2025 07:15:08] "GET /static/photo.jpg HTTP/1.1" 404 -
127.0.0.1 - - [03/May/2025 07:16:32] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/May/2025 07:16:32] "GET /static/photo.jpg HTTP/1.1" 200 -
^C(venv_new) ostap@ostap:~/devops_course/DOCKER-AND-KUBERNETES_MARTYNIUK_1 (feature/citation)$ BACKGROUND_COLOR=#0000ff python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.2.15:5000
Press CTRL+C to quit

```