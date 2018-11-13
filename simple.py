from flask import Flask
from flask import render_template_string
app = Flask(__name__)

@app.route('/')
def hello_world():
    html= """
        <html>
            <h1>Serving from flask</h1>
        </html>
        """
    return html 
@app.route('/template')
def hello_user():
    user = "asrar"
    html = """
            <html>
                <h1>Welcome {{user}}</h1>
                <ul>
                    {% for color in colors %}
                        <li>{{color}}</li>
                    {% endfor %}
                </ul>
            </html>
            """
    rendered_html = render_template_string(html, user=user, colors=['red', 'green', 'blue'])
    return rendered_html
if __name__ == '__main__':
    app.debug=True
    app.run()
