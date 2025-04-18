from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEATHER_SERVICE_URL = "http://weather-service:5001/weather" # 使用 Docker Compose 服务名
BEVERAGE_PREFERENCE_SERVICE_URL = "http://beverage-preference-service:5002/beverage" # 使用 Docker Compose 服务名

@app.route('/order', methods=['POST'])
def place_order():
    try:
        city_id = request.form.get('city_id')
        if not city_id:
            return jsonify({"error": "Missing city_id parameter"}), 400

        # 1. 调用 Weather-Service 获取天气类型
        weather_response = requests.get(f"{WEATHER_SERVICE_URL}/{city_id}")
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        weather_type = weather_data.get('weather_type')
        if not weather_type:
            return jsonify({"error": "Failed to get weather type from weather-service"}), 500

        # 2. 调用 Beverage-Preference-Service 获取饮料名称
        beverage_response = requests.get(f"{BEVERAGE_PREFERENCE_SERVICE_URL}/{weather_type}")
        beverage_response.raise_for_status()
        beverage_data = beverage_response.json()
        beverage_name = beverage_data.get('beverage_name')
        if not beverage_name:
            return jsonify({"error": "Failed to get beverage name from beverage-preference-service"}), 500

        return jsonify({"beverage_type": beverage_name}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error communicating with downstream service: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Order beverage service error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) # Order-Beverage-Service 监听 5000 端口
