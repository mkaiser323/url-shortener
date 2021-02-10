from flask import Flask, request, jsonify
from domain.usecase import UrlShortener
from repository.url import UrlRepository

app = Flask(__name__)

url_shortener = UrlShortener(UrlRepository(), "www.url-shortener.com", 8)

@app.route('/')
def index():
  return 'url-shortner is running and ready to accept requests!'


@app.route('/shorten', methods=['POST'])
def get_short_url():
  request_data = request.get_json()

  long_url = request_data['long_url']
  ##TODO validate url

  url = url_shortener.get_short_url(long_url)

  return jsonify({
      'shortUrl': url.short,
      'longUrl': url.long
  })

@app.route('/getLongUrl', methods=['GET'])
def get_long_url():
  short_url = request.args.get('short_url')

  found, url = url_shortener.get_long_url(short_url)

  if not found:
    return jsonify({
      'error': 'no long_url exists for given short_url: ' + short_url
    })

  return jsonify({
      'shortUrl': url.short,
      'longUrl': url.long
  })

