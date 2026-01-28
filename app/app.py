from flask import Flask, jsonify
import time
import redis

app = Flask(__name__)
# Connect to Redis (localhost works because they share a Pod)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('stock', 100)

@app.route('/buy', methods=['POST'])
def buy():
    # Simulate slight processing (Chaos will add the big delay)
    time.sleep(0.1) 
    stock = r.decr('stock')
    return jsonify({"message": "Purchase successful!", "stock_remaining": stock})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)