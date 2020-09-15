# Contextos

from flask import flask

app = Flask(__name__)

## 1 Configuração

### Add configuração
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DB_URI"] = "mysql://.."

### Registrar Rotas

@app.route("/path")
def funcao():
    ...

app.add_url_rule("/path", callable)

### Iniciar extensões

from flask admin import Admin
Admin.init_app(app)

### Registrar Blueprints
app.register_blueprints(...)

### add hooks

@app.before_request(...)
@app.error_handler(...)

### Chamar outras factories

views.init_app(app)

## 2 App Context

### App está pronto! `app`

### Testar
#app.test_client
#debug
#objetos globais do flask
#(importar request, session, g)
#- Hooks

from flask import current_app, g

## 3 Request Context
### usar globais do flask
from flask import request, session, g

request.args
request.form