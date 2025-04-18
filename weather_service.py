from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather/<city_id>', methods=['GET'])
def get_weather(city_id):
    try:
        city_id_int = int(city_id)
        if city_id_int % 2 == 0:
            weather_type = "COLD"
        else:
            weather_type = "WARM"
        return jsonify({"weather_type": weather_type}), 200
    except ValueError:
        return jsonify({"error": "Invalid city_id, must be an integer"}), 400
    except Exception as e:
        return jsonify({"error": f"Weather service error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) # Weather-Service 监听 5001 端口
