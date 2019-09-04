## Flask-Threads
A helper library to work with threads within Flask applications.

The main problem that you face trying to spin a background thread or running a 
future in Flask app - is loosing the application context. The most common 
scenario is to try to access `flask.g` object. Application context 
is a thread local so you can not access it from another thread and Flask will 
raise an exception if you would try to. 

This library provides helper classes that allows you accessing the current 
application context from another thread.

**Warning! Alpha-version, use at your own risk.**

### Examples

#### Threads

```python
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
# TBD
```
