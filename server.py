from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    # Handle the OAuth2 response here
    return 'OAuth2 Callback received!'

if __name__ == '__main__':
    app.run(port=3000)