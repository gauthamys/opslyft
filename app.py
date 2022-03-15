"""TEST"""
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_opslyft():
    """need to get a 10/10 on lint :)"""
    return f"{os.environ.get('MESSAGE')}"

if __name__ == '__main___':
    app.run(debug=True, port=5000, host='0.0.0.0')
