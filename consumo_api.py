import json
import requests

def pega_palavra():
    headers = {'Content-Type': 'application/json'}

    try:

        # Tenta acessar a API, em Node, que retorna uma string, caso contrario retorna BOLA msm
        response = requests.get("http://localhost:3333/", headers=headers)
        if response.status_code == 200:
            resonse_data = json.loads(response.content.decode('utf-8'))
            return resonse_data["palavra"]
        else:
            return "BOLA"
    except:
        return "BOLA"