from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    ip_address = request.form['ip_address']
    api_token = '84833bff5b72a9'
    url = f'https://ipinfo.io/{ip_address}?token={api_token}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        data = {}
    return render_template('resultado.html', data=data)

@app.route('/get_my_ip', methods=['GET'])
def get_my_ip():
    response = requests.get('https://api64.ipify.org?format=json')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"ip": "No se pudo obtener la IP"})
print("")
print("")
print("\t\t\t██╗    ██╗██╗██╗     ██████╗ ██████╗ ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗")
print("\t\t\t██║    ██║██║██║     ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝")
print("\t\t\t██║ █╗ ██║██║██║     ██║  ██║██████╔╝██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   ")
print("\t\t\t██║███╗██║██║██║     ██║  ██║██╔══██╗██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   ")
print("\t\t\t╚███╔███╔╝██║███████╗██████╔╝██║  ██║██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   ")
print("\t\t\t ╚══╝╚══╝ ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ")

if __name__ == '__main__':
    app.run(debug=True)
