from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.email import Email

@app.route("/")
def index():
    return render_template("index.html")

# process route
@app.route("/create", methods=["POST"])
def success():
    if not Email.validate_email(request.form):
        return redirect("/")
    Email.save(request.form)
    return redirect("./success")

# display route
@app.route("/success")
def show_email():
    emails = Email.get_all()
    return render_template("success.html", all_email=emails)

@app.route("/destroy/<int:id>")
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect("/success")
