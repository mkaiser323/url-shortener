from flask import Flask, request, jsonify
import random, string
app = Flask(__name__)


## usecase - rename these after export
class UrlShortener:
  def __init__(self, url_repository, domain_name, url_length):
    self.url_repository = url_repository
    self.domain_name = domain_name
    self.url_length = url_length

  def get_short_url(self, long_url):
    ## if short url already exists for given long url, return existing
    found, url = self.url_repository.find_by_long_url(long_url)

    if found:
      return url
    
    ## if not exists, generate, check if exists, store and return
    short_url = None
    found = True
    while found:
      ##TODO: unlikely that it will be needed, but probably want some forced exit after n attempts 
      short_url = random_url(self.url_length)
      found, url = self.url_repository.find_by_short_url(short_url)

    url = Url(long_url, short_url)
    self.url_repository.add_url(url)
    return url
  

  def get_long_url(self, short_url):
    return self.url_repository.find_by_short_url(short_url)


## domain
class Url:
  def __init__(self, long, short):
    self.long = long
    self.short = short

## repo - hardcoding return values for now
class UrlRepository:
  def __init__(self):
    ## setup db connection here
    self.mock_data = None
    return

  def find_by_long_url(self, long_url):
    return self.mock_data, self.mock_data

  def find_by_short_url(self, short_url):
    return self.mock_data, self.mock_data

  def add_url(self, url):
    ## save to db
    self.mock_data = url
    return

## lib
def random_url(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))



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

