from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "IVR Audio Server is running"

@app.route("/announcement.wav")
def announcement():
    return send_file(
        "network_announcement_ivr.wav",
        mimetype="audio/wav",
        as_attachment=False
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
