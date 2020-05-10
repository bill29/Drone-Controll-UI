from flask import Flask, render_template

app = Flask(__name__)
"""
Dòng thứ 2, chúng ta khai báo 1 thể hiện của class Flask. 
Nó sẽ được sử dụng xuyên suốt trong chương trình của chúng ta.
"""
# @app.route('/')
# def hello_world():
#     return 'Hello, World'

# @app.route('/')
# def home():
#     user = {'username': 'Minh Dan'}
#     return render_template('hello.html', title = 'Home', user=user)

@app.route('/setting')
def setting():
    return 'Setting'

@app.route('/')
def controll():
    return render_template('controll.html')


if __name__ == '__main__':
    app.run()