## hardcoding return values for now
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
