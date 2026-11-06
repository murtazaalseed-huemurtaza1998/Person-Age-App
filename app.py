from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)

@app.route("/api/calculate", methods=["POST"])
def calculate():
    try:
        data = request.get_json()
        age = int(data.get("age", 0))

        if age <= 0 or age > 120:
            return jsonify({"error": "اكتب عمر صحيح بين 1 و 120"}), 400

        return jsonify({
            "age": age,
            "days": age * 365,
            "hours": age * 365 * 24,
            "minutes": age * 365 * 24 * 60,
            "message": f"عمرك {age} سنة"
        })
    except:
        return jsonify({"error": "صار خطأ بالسيرفر"}), 500

if __name__ == "__main__":
    app.run()