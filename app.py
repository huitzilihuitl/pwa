from flask import Flask, render_template, redirect, session, request
import requests


app = Flask(__name__)
url_base = "https://sandbox.belvo.com"


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/login", methods=["POST"] )
def login():
    # Valida los datos del formulario
    username = request.form.get("username")
    password = request.form.get("password")

    u = 'huitzi'
    p = '123'

    if username == u and password == p: 
        # El usuario ha iniciado sesión correctamente
        # session["username"] = username
        return redirect("/home")
    else:
        # El usuario no ha iniciado sesión correctamente
        return redirect("/")


@app.route("/home")
def home():
    lista_bancos = list_banks()
    return render_template('home.html', bancos=lista_bancos)


@app.route("/manifest.json")
def manifest():
    return render_template('manifest.json')


def list_banks():
    url = url_base + "/api/institutions/"
    response = requests.get(url, auth=('f9934a7e-9a02-42d1-82b5-1620b8374b6f', 'iJ-FUVXs4ewuP8ZIlDpuV86iQlZA8s_wLYOFCIZT@gwy0oi#xSFehBDFWN3PXC_W'))

    if response.status_code == 200:
        # La petición se realizó correctamente
        data = response.json()
        instituciones = data['results']
        for i, v in enumerate(instituciones):
            print(i)
            print(v['icon_logo'])
            print('--------------------------')
            if v['icon_logo'] is None:
                v['icon_logo'] = '../static/bank-building.png'

        return instituciones
    else:
        # La petición no se realizó correctamente
        print(response.status_code)
