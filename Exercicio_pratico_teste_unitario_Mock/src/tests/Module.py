import json

class AtendimentoProfessor:
    def __init__(self, json_data):
        self.dados = json.loads(json_data)

    def get_predio(self):
        try:
            sala = int(self.dados['sala'])
        except (ValueError, KeyError):
            raise ValueError("Sala inválida")

        predio = self.dados['predio']
        # Determina o prédio baseado na faixa da sala
        if 1 <= sala <= 5:
            expected_predio = "1"
        elif 6 <= sala <= 10:
            expected_predio = "2"
        elif 11 <= sala <= 15:
            expected_predio = "3"
        elif 16 <= sala <= 20:
            expected_predio = "4"
        elif 21 <= sala <= 26:
            expected_predio = "5"
        elif 27 <= sala <= 31:
            expected_predio = "6"
        else:
            raise ValueError("Sala fora do intervalo válido")

        if predio != expected_predio:
            raise ValueError("Predio informado não corresponde ao intervalo da sala")

        return predio

    def get_horario(self):
        return self.dados['horarioDeAtendimento']

    def get_periodo(self):
        return self.dados['periodo']

    def get_nome(self):
        return self.dados['nomeDoProfessor']
