import requests

def fetch_data(ine_code):
    province_code = f"{ine_code[0]}{ine_code[1]}"

    api = f"https://www.el-tiempo.net/api/json/v2/provincias/{province_code}/municipios/{ine_code}"
    response = requests.get(api)

    if response.status_code == 200:
        return response.json()
    