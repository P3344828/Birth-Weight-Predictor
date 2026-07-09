from flask import Flask, render_template
from routes import predict, user
from extentions import cache

app = Flask(__name__)

## Configure Flask-Caching
app.config['CACHE_TYPE']= 'SimpleCache'

## Initialize cache with the Flask app
cache.init_app(app)


## Register blueprints for modular routing
app.register_blueprint(user.user_bp)
app.register_blueprint(predict.predict_bp)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

