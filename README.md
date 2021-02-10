# url-shortener

Started: 2/9/21 6:40 PM

Finished: 2/9/21 9:34 PM

REST-based web service that shortens urls

## Setup instructions:

1. Set the following environment variables:

```
export FLASK_APP=app.py
export FLASK_ENV=development
```

2. Navigate to the root project directory and ctivate the environment using the following command:

```. venv/bin/activate```

3. Start the server by running:

```flask run```

## APIs

### Shorten Url

#### Request:
```
POST http://127.0.0.1:5000/shorten

{
    "long_url": "original/long/url.com"
}

```

#### Response:
```
{
    "longUrl": "original/long/url.com",
    "shortUrl": "5h0rt3nd"
}
```

### Retreive original URL from shortened



#### Request:
```
GET http://127.0.0.1:5000/getLongUrl?short_url=5h0rt3nd
```

#### Successful Response:
```
{
    "longUrl": "original/long/url.com",
    "shortUrl": "5h0rt3nd"
}
```

#### Failed Response:
The following message will be returned if a short_url is supplied for which no long_url exists
```
{
    "error": "no long_url exists for given short_url: n0suchurl"
}
```

## Credits: 

Followed https://medium.com/@onejohi/building-a-simple-rest-api-with-python-and-flask-b404371dc699 to set up basic rest server using Flask
