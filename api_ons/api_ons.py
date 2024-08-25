import requests


class ApiOns:
    def __init__(self):
        self.base_url = "https://apicarga.ons.org.br/prd"

    def get_carga_verificada(
        self, data_inicio, data_fim, cod_areacarga
    ) -> requests.Response:
        url = self.base_url + "/cargaverificada"
        params = {
            "dat_inicio": data_inicio,
            "dat_fim": data_fim,
            "cod_areacarga": cod_areacarga,
        }
        response = requests.get(url, params=params)
        return response

    def get_carga_programada(
        self, data_inicio, data_fim, cod_areacarga
    ) -> requests.Response:
        url = self.base_url + "/cargaprogramada"
        params = {
            "dat_inicio": data_inicio,
            "dat_fim": data_fim,
            "cod_areacarga": cod_areacarga,
        }
        response = requests.get(url, params=params)
        return response


if __name__ == "__main__":

    api = ApiOns()

    print("Teste de carga verificada")
    resp_verificada = api.get_carga_verificada("2021-01-01", "2021-01-02", "SP")
    print(resp_verificada.status_code)
    if resp_verificada.status_code == 200:
        print(resp_verificada.content)
        
    print("Teste de carga programada")
    resp_programada = api.get_carga_verificada("2021-01-01", "2021-01-02", "SP")
    print(resp_programada.status_code)
    if resp_programada.status_code == 200:
        print(resp_programada.content)
