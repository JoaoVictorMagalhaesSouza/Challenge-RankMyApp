from flask import Flask
import rmp_dashboard

app = Flask(__name__)
app_dash = rmp_dashboard.init_app(app)
app = app_dash.server

@app.route('/')
def dashboard():
    return app_dash.index()

if __name__ == '__main__':
    app_dash.run_server(host='0.0.0.0',port=8050,debug=False)
