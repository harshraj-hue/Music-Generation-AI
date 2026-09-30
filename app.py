from flask import Flask, render_template, request, jsonify, send_from_directory
from generate_music import generate_music
import os

app = Flask(__name__)

OUTPUT_DIR = "generated_music"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({
            "success": False,
            "message": "Please enter a music description."
        })

    try:
        filename = "generated_music.wav"

        generate_music(
            prompt=prompt,
            filename=filename
        )

        return jsonify({
            "success": True,
            "message": "Music generated successfully!",
            "audio_url": f"/music/{filename}"
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error generating music: {str(e)}"
        })


@app.route("/music/<filename>")
def music(filename):
    return send_from_directory(
        OUTPUT_DIR,
        filename
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )