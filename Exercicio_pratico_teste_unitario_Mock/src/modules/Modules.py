import json


class AtendimentoProfessor:
    def __init__(self, json_data):
        self.dados = json.loads(json_data)

    def get_predio(self):
        sala = int(self.dados['sala'])
        if 1 <= sala <= 5:
            return 1
        elif 6 <= sala <= 10:
            return 2
        else:
            raise ValueError("Sala inválida")

    def get_horario(self):
        return self.dados['horarioDeAtendimento']

    def get_periodo(self):
        return self.dados['periodo']

    def get_nome(self):
        return self.dados['nomeDoProfessor']
