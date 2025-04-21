import os

from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/quienes-somos/")
def quienes_somos():
    return render_template('about.html')

@app.route("/nuestro-equipo/")
def nuestro_equipo():
    return render_template('our_team.html')

@app.route("/noticias")
def noticias():
    return render_template('news.html')

@app.route("/nuestro-trabajo/")
def nuestro_trabajo():
    return render_template('our_work.html')

@app.route("/contacto/")
def contacto():
    return render_template('contact.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
