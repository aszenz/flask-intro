from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    html= """
        <html>
            <h1>Serving from flask</h1>
        </html>
        """
    return html 

if __name__ == '__main__':
    app.debug=True
    app.run()
