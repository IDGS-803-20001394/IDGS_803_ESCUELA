from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

from Alumnos.routes import alumnos
from Maestros.routes import maestros

app = Flask(__name__)
app.config['SECRET_KEY'] = "ContraseñaEncriptada"
app.config['DEBUG'] = True
csrf = CSRFProtect()

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

app.register_blueprint(alumnos)
app.register_blueprint(maestros)

if __name__ == "__main__":
    csrf.init_app(app)
    app.run()