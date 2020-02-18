# Check 
Simple web-app that uses a Sci-kit Learn model to determine whether a user is human or a bot.

## Docker

To build the image from the **Dockerfile**  just run:

```docker build .```

To run the image:

```docker run -d -p 5000:5000 IMAGE```


## App

To run the app alone:

```python3 app.py```

You may need to install the required packages:

```pip3 install -r requirements.txt```

## Sending data with curl post requests

To send user activity to be checked by the SKLearn model, structure your curl command like the following one:

```curl 0.0.0.0:5000/ -d '{"country":"US", "region":"CA", "visitortype":"ANONYMOUS", "referrer":"1"}' -H 'Content-Type: application/json'```

*Keys*:

- **country**: User's country
- **region**: User's region
- **visitortype**: Whether the user is browsing anonymously or logged in.
- **referrer**: Either 1 or 0


