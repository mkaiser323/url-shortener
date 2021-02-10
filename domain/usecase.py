
from model import Url
from lib.rand import random_url

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