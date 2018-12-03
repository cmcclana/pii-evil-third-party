# Private Browsing PII Leakage Research

## Installation instructions

Make sure you have pipenv and python3 installed:

https://pipenv.readthedocs.io/en/latest/install/

Make sure you install mongodb also (brew for Mac)

```
pipenv install
```

To run the app, type the following into a terminal and keep running:

```
mongod --dbpath=./db
```

Type the following into a new terminal

```
pipenv shell
FLASK_APP=app.py flask run
```

Then go to http://localhost:5000 to see the site!

To see the database, open and/or install Robo 3T. 
Create an initial connection with default settings.
The database will be under flask_session -> Collections -> sessions.
In Mongo, a document is like a row and a collection is like a table.
Right click one of the sessions and select "View Document" to see the document. 
The long string under val is base64 encoded, so to see the contents, paste into a base64 decoder. 

To close the app, press ctrl+c in both terminals.

## Approach

How evil third-party works:

1. first-party embeds third-party ad service as an image
2. user makes request to first-party
3. first-party responds with html document
4. user's browser loads the document and then makes the request to the third-party from the img tag src attribute
5. third-party responds with image but also adds Set-Cookie header with a unique ID.
6. user goes somewhere else on the first-party site (2nd request)
7. first-party responds with img tag to third-party again
8. user's browser make a call to third-party again but this time, it sends cookies along with the request including the referer header
9. user goes to their profile where the URL scheme contains PII
10. every request to the third-party is recorded on the third-party's backend. every request to the third-party will save a key-value pair where the key is the cookie (which is that unique ID set from step 5) and the value is the URL from the referer header.
nvm need to store a 3-tuple: (cookie-id, finger-print-id, URL)
11. user goes to a different site that also embeds the third-party
12. when the user's browser makes a request for an image from the third-party, it will also send the cookies set from the first site (third-party cookie).
13. save all cookie key-value pairs to some database or even a file

---

1. W submits form in private mode
2. User's browser loads confirmation of submission (which contains 3rd party ad image)
3. 3rd party will get the URL, the fingerprint.

if (url matches submission scheme) {
    w's identity = lookup W's identity from fingerprints
    return image with w's identity
}


I think the User-Agent header only includes the user's browser and operating system which isn't very unique and IP v4 addresses can be shared amongst many computers (though IP v6 would be unique enough but those change frequently).


1. first-party site loads: makes http call to first-party
2. third-party embedded document loads; makes http call to third-party from first-party with referer header from first-party.
    gives tuple of: (cookie_id, url, timestamp, ip, user-agent)
3. third-party doc runs a fingerprint. needs to upload this fingerprint and the resulting tuple from the upload of the fingerprint will be (cookie_id, fingerprint)
