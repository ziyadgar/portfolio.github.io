"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


footerp = "Copyright Ziyad GARGOURI 2021"
reseaux_dict = {
    "https://www.facebook.com/profile.php?id=100075172872516": "facebook.png",
    "https://www.instagram.com/zg.digital/": "instagram.png",
    "https://www.linkedin.com/in/ziyad-gargouri/": "linkedin.png",
    "https://twitter.com/ZG_Digital": "twitter.png",
}


@app.route("/")
def home():
    title = "Home Page"
    h1 = "Ziyad Gargouri"
    h3 = "Bienvenu sur mon site"
    """Renders the home page."""
    return render_template(
        "index.html",
        title=title,
        footer=footerp,
        hometitle=h1,
        homesstitle=h3,
        reseau=reseaux_dict,
    )


@app.route("/a_propos")
def a_propos():
    title = "A propos Page"
    h1 = "A propos de moi"
    """Renders the a_propos page."""
    return render_template(
        "a_propos.html", title=title, footer=footerp, abouttitle=h1, reseau=reseaux_dict
    )


@app.route("/competences")
def competences():
    title = "Competences Page"
    h1 = "Mes compétences"
    h3l = "Langages et Frameworks"
    h3sw = "Logiciels"
    skillslevel = {
        "Python": "50",
        "Falsk": "60",
        "Jinja": "40",
        "HTML": "70",
        "CSS": "50",
        "SQL": "0",
        "API": "0",
        "JS": "0",
        "React": "0",
        "Bootstrap": "50",
        "Wordpress": "50",
        "Prestashop": "50",
    }
    softwarelevel = {
        "Photoshop": "30",
        "Indesign": "40",
        "illustrator": "25",
        "Adobe XD": "45",
        "Plesk": "40",
        "Git": "50",
        "VisualStudio": "35",
        "VSCode": "75",
        "Office": "75",
    }
    """Renders the competences page."""
    return render_template(
        "competence.html",
        title=title,
        footer=footerp,
        my_dict_skills=skillslevel,
        my_dict_sw=softwarelevel,
        skillstitle=h1,
        skillsleveltitle=h3l,
        skillsswtitle=h3sw,
        reseau=reseaux_dict,
    )


@app.route("/projets")
def projets():
    title = "Projets Page"
    urlsimage = [
        "matrice.png",
    ]
    urlsprojet = [
        "https://flourshower.ziyadgargouri.fr/",
    ]
    nameprojet = [
        "FlourShower",
    ]
    langprojet = [
        "HTML/CSS",
    ]
    dateprojet = [
        "21/11/2021",
    ]
    creatorprojet = [
        "Ziyad Gargouri",
    ]
    origineprojet = [
        "Ecole Matrice",
    ]
    maquetteorigine = [
        "Ecole Matrice",
    ]
    indice = range(len(urlsimage))
    """Renders the projets page."""
    return render_template(
        "projets.html",
        title=title,
        footer=footerp,
        urlsimage=urlsimage,
        urlsprojet=urlsprojet,
        nameprojet=nameprojet,
        langprojet=langprojet,
        dateprojet=dateprojet,
        creatorprojet=creatorprojet,
        origineprojet=origineprojet,
        maquetteorigine=maquetteorigine,
        indice=indice,
        reseau=reseaux_dict,
    )


if __name__ == "__main__":
    import os

    HOST = os.environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(os.environ.get("SERVER_PORT", "5555"))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
