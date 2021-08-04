from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/view", methods=["post"])
def view():
    images = request.files.getlist("image[]")
    print("mimetype: ", images[0].mimetype)
    #print("content: ", images[0].stream.read())
    return ""

app.run()
