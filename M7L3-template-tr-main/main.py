from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/oyun.html")
def oyun():
    return render_template("oyun.html")

@app.route("/arama", methods=["GET"])
def arama():
    query = request.args.get("query")
    
    # Eğer "İklim Değişikliği" yazılırsa iklim_degisim.html sayfasına yönlendiriyoruz
    if query and "İklim Değişikliği" in query:
        return render_template("iklim_degisim.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


