from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/status', methods=['GET'])
def get_status():
    # Lab Part E Response (Modify this later in Part F)
    return jsonify({
        "status": "Mobile backend online",
        "database": "connected",
        "server_environment": "Render.com PaaS"
    })

if __name__ == '__main__':
    # Render requires the app to bind to 0.0.0.0 and a dynamic port
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

