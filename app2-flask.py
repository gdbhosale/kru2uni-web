#!flask/bin/python
from flask import Flask
from flask import request
import krutidev2unicode as kd

app = Flask(__name__)

@app.route('/kru2uni', methods=['POST'])
def kru2uni():
    data = request.form.get("data")
    print data
    # kd.kru2uni(data)
    return data

if __name__ == '__main__':
    app.run(debug=True)
