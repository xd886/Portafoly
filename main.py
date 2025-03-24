from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Diccionario de proyectos
PROJECTS = {
    "python": "static/img/python-project.png",
    "discord": "static/img/discord-project.png",
    "html": "static/img/html-project.png",
    "db": "static/img/db-project.png"
}

@app.route("/", methods=["GET", "POST"])
def index():
    project_image = None

    if request.method == "POST":
        skill = request.form.get("skill")
        if skill in PROJECTS:
            project_image = url_for('static', filename=f"img/{skill}-project.png")

    return render_template("index.html", project_image=project_image)

if __name__ == "__main__":
    app.run(debug=True)
