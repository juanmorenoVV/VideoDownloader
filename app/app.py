from flask import Flask, render_template, request

from pytube import YouTube

import os 

from pathlib import Path


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])

def home():

    return render_template("index.html")

@app.route("/downloadvideo", methods=["GET, POST"])
def downloadvideo():
    if request.method == "POST":
        urlVideo = request.form[urlVideo]
        videoYt = YouTube(urlVideo)

        path = "Videos" 
        folder = "VideosYt"

        url_Downloads = str(Path.home() / path)

        videoYt.streams.get_highest_resolution().download(output_path=os.path.join(url_Downloads, folder))
        return render_template("templates/index.html")
    else:
        return render_template("templates/index.html")



@app.errorhandler(404)
def not_found(error):
    return render_template("templates/index.html")




if __name__ == "__main__":
    app.run(debug=True, port=5000)



