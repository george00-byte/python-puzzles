from flask import Flask
from flask_caching import Cache

app = Flask(__name__)

# Configure caching
app.config['CACHE_TYPE'] = 'SimpleCache'  # Options: 'SimpleCache', 'RedisCache', etc.
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Default timeout for cache in seconds
cache = Cache(app)

@app.route('/')
@cache.cached(timeout=60)  # Cache this route for 60 seconds
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
