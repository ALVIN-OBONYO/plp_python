from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

todoz = [{"todo": " Addtask", "viewtask": False}]

@app.route("/")
def index():
    return render_template("index.html", todoz =todoz)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form.get("todo")
    todoz.append({"task": todo, "done":False})
    return redirect(url_for("index"))
    # def edit(index):

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todoz[index]
    if request.method == "POST":
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)


@app.route("/check/<int:index>")
def check(index):
    todoz[index]["done"] = not todoz[index]['done']
    return redirect(url_for("index"))                                        
@app.route("/delete/<int:index>")
def delete(index):
    todoz.pop(index)
    return redirect(url_for("index"))




if __name__ == '__main__':
    app.run(debug=True)
