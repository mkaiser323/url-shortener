from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return 'url-shortner is running and ready to accept requests!'


@app.route('/shorten', methods=['POST'])
def shorten():
  request_data = request.get_json()

  url = request_data['url']
  resp = {
      'message': 'received request to shorten ' + url,
      'shortUrl': 'shortUrl',
      'longUrl': 'longUrl'
    }

  return jsonify(resp)

@app.route('/getLongUrl', methods=['GET'])
def getLongUrl():
  url = request.args.get('shorturl')
  resp = {
      'message': 'received request to shorten ' + url
    }

  return jsonify(resp)
