from flask import Flask, jsonify
import random

app = Flask(__name__)

HOT_BEVERAGES = ["cappuccino", "latte", "espresso"]
COLD_BEVERAGES = ["lemonade", "ice tea", "soda"]

@app.route('/beverage/<weather_type>', methods=['GET'])
def get_beverage(weather_type):
    try:
        weather_type = weather_type.upper() # 转换为大写，忽略大小写
        if weather_type == "HOT" or weather_type == "WARM": # 同时支持 "HOT" 和 "WARM" 天气类型
            beverage_name = random.choice(HOT_BEVERAGES)
        elif weather_type == "COLD":
            beverage_name = random.choice(COLD_BEVERAGES)
        else:
            return jsonify({"error": "Invalid weather_type, must be WARM or COLD"}), 400
        return jsonify({"beverage_name": beverage_name}), 200
    except Exception as e:
        return jsonify({"error": f"Beverage preference service error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True) # Beverage-Preference-Service 监听 5002 端口
