from flask import Flask, Markup, make_response, request
import uuid
import datetime
app = Flask(__name__)

fingerprinter = open('./fingerprinter.js')

def create_advertisement(title):
    normal_ad = Markup(f'''
        <html>
            <title>
                Non-Evil Advertisement
            </title>
            <body>
                <h1>{title}</h1>
                <script>
                    console.log('TODO: add fingerprinting javascript code');
                    fetch('/fingerprints', {})
                </script>
            </body>
        </html>
    ''')
    


# <iframe src="https://evilthirdparty.com"></iframe>

@app.route('/')
def evil_third_party():
    '''
    This method is the main end-point of the evil third-party. Whenever a
    request is made for the embedable content of the evil third-party, it will
    go through this function.

    The first time a request is made to the evil third-party, the evil
    third-party will set a cookie with a unique random ID to identify the user's
    session.

    Thereafter, whenever a request is made to this evil third-party, it will
    save a tuple of the user's (cookie-id, URL) to track the user's history on
    the first-party site.

    In order to show the "Gotcha" message to W, we check if the URL matches the
    URL form submission scheme and change the response to a different document
    saying "Gotcha W, your name is _____"

    In any other case, this evil third-party will show a random advertisement to
    seem like the service isn't tracking the users
    '''

    # create the advertisement document
    response = make_response(create_advertisement('Free money'))
    response.headers.set('Content-Type', 'text/html')

    # ensure a cookie_id
    cookie_id = request.cookies.get('cookie_id')
    if not cookie_id:
        cookie_id = uuid.uuid4().hex
        response.set_cookie('cookie_id',  cookie_id)

    # grab URL from referer header
    url = request.headers.get('referer')
    # user_agent = request.headers.get('user-agent')
    # ip_address = request.remote_addr
    timestamp = datetime.datetime.now()

    # this tuple will be used to track the user on the first-party site
    # and grab PII leaked from the URL
    tracking_tuple = (cookie_id, url, timestamp)
    print(tracking_tuple)

    # TODO: save tuple to DB or in-memory

    return response

@app.route('/fingerprints', method='POST')
def fingerprints():
    request_data = request.get_json()
    print(request_data)


@app.route('/history')
def history():
    return 'TODO'