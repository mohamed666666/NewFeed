'''from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    mysql.init_app(app)
    
   
    
    from .controllers.user_controller import user_bp
    app.register_blueprint(user_bp)
    
    return app'''

#error 
'''from flask_mysqldb import MySQL
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/mohamed/Codes/InterView/env/lib/python3.11/site-packages/flask_mysqldb/__init__.py", line 4, in <module>
    import MySQLdb
  File "/home/mohamed/Codes/InterView/env/lib/python3.11/site-packages/MySQLdb/__init__.py", line 17, in <module>
    from . import _mysql
ImportError: libmariadb.so.3: cannot open shared object file: No such file or directory'''