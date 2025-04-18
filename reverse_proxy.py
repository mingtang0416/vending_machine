from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ORDER_BEVERAGE_SERVICE_URL = "http://order-beverage-service:5000/order"  # 使用 Docker Compose 服务名

@app.route('/', methods=['POST'])
def reverse_proxy():
    try:
        city_id = request.form.get('city_id')
        if not city_id:
            return jsonify({"error": "Missing city_id parameter"}), 400

        data = {'city_id': city_id}
        response = requests.post(ORDER_BEVERAGE_SERVICE_URL, data=data)
        response.raise_for_status()  # 检查 HTTP 状态码，非 200 状态码会抛出异常
        return jsonify(response.json()), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error communicating with order-beverage-service: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Reverse proxy error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
