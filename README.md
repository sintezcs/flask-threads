## Flask-Threads
[![Actions Status](https://github.com/sintezcs/flask-threads/workflows/GitHub%20Build/badge.svg)](https://github.com/sintezcs/flask-threads/actions)

A helper library to work with threads within Flask applications.

The main problem that you face trying to spin a background thread or running a 
future in Flask app - is loosing the application context. The most common 
scenario is to try to access `flask.g` object. Application context 
is a thread local so you can not access it from another thread and Flask will 
raise an exception if you would try to. 

This library provides helper classes that allows you accessing the current 
application context from another thread.

**Warning! Alpha-version, use at your own risk.**

### Installation
```bash
$ pip install Flask-Threads
```

### Examples

#### Threads

```python
from flask import g
from flask import request
from flask import Flask
from flaskthreads import AppContextThread

app = Flask('my_app')


@app.route('/user')
def get_user():
    g.user_id = request.headers.get('user-id')
    t = AppContextThread(target=do_some_user_work_in_another_thread)
    t.start()
    t.join()
    return 'ok'


def do_some_user_work_in_another_thread():
    id = g.user_id
    print(id)

```

#### Concurrent futures

```python
from flask import g
from flask import request
from flask import Flask
from flaskthreads import ThreadPoolWithAppContextExecutor

app = Flask('my_app')


@app.route('/user')
def get_user():
    g.user_id = request.headers.get('user-id')
    with ThreadPoolWithAppContextExecutor(max_workers=2) as pool:
        future = pool.submit(do_some_user_work_in_another_thread)
        future.result()
    return 'ok'


def do_some_user_work_in_another_thread():
    id = g.user_id
    print(id)
```
