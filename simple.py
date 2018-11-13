from flask import Flask, render_template_string, render_template, abort
app = Flask(__name__)
@app.route('/')
def hello_world():
    html= """
        <html>
            <h1>Serving from flask</h1>
        </html>
        """
    return html 
@app.route('/template-string')
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
@app.route('/template')
def hello_temp_user():
    user = "asrar"
    return render_template('index.html', user=user, colors=['red', 'green', 'blue'])
@app.route('/abstract')
def abstract():
    return render_template('abstract.html')
@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    return "Num1: {}, Num2: {}, Sum: {}".format(num1, num2, int(num1) + int(num2))
@app.route('/color/<string:color_name>')
def find_color(color_name):
    colors = ['red', 'green', 'blue']
    if color_name not in colors:
        abort(404)
    else:
        return "Color Found"
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
if __name__ == '__main__':
    app.debug=True
    app.run()
