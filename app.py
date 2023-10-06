from flask import Flask, request, render_template
import openai

app = Flask(__name__)

list_img = []

@app.route('/', methods=["GET", "POST"])
def peticion():
    if request.method == 'POST':
        descripcion = request.form.get("descripcion")
        nimg = int(request.form.get("nimg"))
        for _ in range(nimg):
            url_img = crear_img(descripcion)
            list_img.append(url_img)
    return render_template('index.html', list_img=list_img)

def crear_img(descripcion):
    openai.api_key = "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"

    respuesta = openai.Image.create(
            prompt=descripcion,
            n=1,
            size="512x512"
        )
    return respuesta["data"][0]["url"]


if __name__ == "_main_":
    app.run(debug=True, port=5000)