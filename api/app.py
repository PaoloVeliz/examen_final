from flask import Flask
from service import Heat
app = Flask(__name__)


def html(content, columns):
    return '<html><head>Informacion de ambas bases de datos</head><body>' + str(content) + '</body></html>'

@app.route('/test', methods=['GET'])
def welcome():
    return "hola"

@app.route('/data', methods=['GET'])
def holi():
    result = ""
    result = "tabla 1 = " + str(Heat.getAllDataFromTable1())
    result = result + "tabla 2 = " + str(Heat.getAllDataFromTable2())
    return html(result, "")


if __name__ == '__main__':
    app.run()