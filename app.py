from flask import Flask
from views import alerts_blueprint
from views import stores_blueprint
from views import users_blueprint
import os

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.config.update(
    ADMIN=os.environ.get('ADMIN')
) 

app.register_blueprint(alerts_blueprint, url_prefix="/alerts")
app.register_blueprint(stores_blueprint, url_prefix="/stores")
app.register_blueprint(users_blueprint, url_prefix="/users")




if __name__=="__main__":
    app.run()
