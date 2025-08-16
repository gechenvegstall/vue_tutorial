from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return "hello,world!"

"""
Flask 路由支持不同的 HTTP 请求方法，GET、POST、PUT、DELETE可以通过 methods 参数指定允许的请求方法。
除了app.route()还有：
@app.before_request：在每个请求处理之前运行的函数。
@app.after_request：在每个请求处理之后运行的函数。
@app.teardown_request：在请求结束后运行的函数，用于清理工作。
"""
@app.route("/hello")
def hello_world():
    return "hello flask!"


if __name__=="__main__":
    app.run(debug=True)