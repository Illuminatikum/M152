from flask import Flask, render_template, request

app = Flask(__name__)
app.config['VIDEO_UPLOADS'] = "C:\Programming\video"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/me', methods=['POST'])
def getvalue():
    
    if request.method == "POST":
        if request.files:
            image = request.files


    video_mp4 = request.files['video_mp4']
    video_mp4.save(secure_filename(video_mp4.filename))

    return render_template('gif.html')

@app.route('/me')
def me():
    return render_template('me.html')

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)