import unittest
import json
from tests.Module import AtendimentoProfessor

class TestAtendimentoProfessor(unittest.TestCase):

    def setUp(self):
        self.valid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "3",
            "predio": "1"
        })
        self.invalid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "22",
            "predio": "1"
        })

    def test_get_predio_success(self):
        obj = AtendimentoProfessor(self.valid_json)
        self.assertEqual(obj.get_predio(), "1")

    def test_get_predio_success_range_6_10(self):
        valid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "8",
            "predio": "2"
        })
        obj = AtendimentoProfessor(valid_json)
        self.assertEqual(obj.get_predio(), "2")

    def test_get_predio_success_range_11_15(self):
        valid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "12",
            "predio": "3"
        })
        obj = AtendimentoProfessor(valid_json)
        self.assertEqual(obj.get_predio(), "3")

    def test_get_predio_success_range_16_20(self):
        valid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "18",
            "predio": "4"
        })
        obj = AtendimentoProfessor(valid_json)
        self.assertEqual(obj.get_predio(), "4")

    def test_get_predio_success_above_21(self):
        valid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "22",
            "predio": "5"
        })
        obj = AtendimentoProfessor(valid_json)
        self.assertEqual(obj.get_predio(), "5")

    def test_get_predio_success_above_27(self):
        valid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "28",
            "predio": "6"
        })
        obj = AtendimentoProfessor(valid_json)
        self.assertEqual(obj.get_predio(), "6")

    def test_get_predio_success_range_1_5(self):
        valid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "2",
            "predio": "1"
        })
        obj = AtendimentoProfessor(valid_json)
        self.assertEqual(obj.get_predio(), "1")

    def test_get_predio_success_boundary(self):
        valid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "10",
            "predio": "2"
        })
        obj = AtendimentoProfessor(valid_json)
        self.assertEqual(obj.get_predio(), "2")

    def test_get_horario_success(self):
        obj = AtendimentoProfessor(self.valid_json)
        self.assertEqual(obj.get_horario(), "10:00 - 12:00")

    def test_get_periodo_success(self):
        obj = AtendimentoProfessor(self.valid_json)
        self.assertEqual(obj.get_periodo(), "integral")

    def test_get_nome_success(self):
        obj = AtendimentoProfessor(self.valid_json)
        self.assertEqual(obj.get_nome(), "Prof. João")

    def test_get_predio_failure(self):
        with self.assertRaises(ValueError):
            obj = AtendimentoProfessor(self.invalid_json)
            obj.get_predio()

    def test_get_predio_failure_missing_predio(self):
        invalid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "3"
        })
        obj = AtendimentoProfessor(invalid_json)
        with self.assertRaises(KeyError):
            obj.get_predio()

    def test_get_predio_failure_invalid_sala(self):
        invalid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "-1",
            "predio": "1"
        })
        obj = AtendimentoProfessor(invalid_json)
        with self.assertRaises(ValueError):
            obj.get_predio()

    def test_get_horario_failure(self):
        invalid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "periodo": "integral",
            "sala": "3",
            "predio": "1"
        })
        obj = AtendimentoProfessor(invalid_json)
        with self.assertRaises(KeyError):
            obj.get_horario()

    def test_get_periodo_failure(self):
        invalid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "sala": "3",
            "predio": "1"
        })
        obj = AtendimentoProfessor(invalid_json)
        with self.assertRaises(KeyError):
            obj.get_periodo()

    def test_get_nome_failure(self):
        invalid_json = json.dumps({
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "3",
            "predio": "1"
        })
        obj = AtendimentoProfessor(invalid_json)
        with self.assertRaises(KeyError):
            obj.get_nome()

    def test_get_predio_failure_non_numeric_sala(self):
        invalid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "abc",
            "predio": "1"
        })
        obj = AtendimentoProfessor(invalid_json)
        with self.assertRaises(ValueError):
            obj.get_predio()

    def test_get_predio_failure_out_of_range(self):
        invalid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "0",
            "predio": "1"
        })
        obj = AtendimentoProfessor(invalid_json)
        with self.assertRaises(ValueError):
            obj.get_predio()

    def test_get_predio_failure_invalid_predio(self):
        invalid_json = json.dumps({
            "nomeDoProfessor": "Prof. João",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "integral",
            "sala": "3",
            "predio": "7"
        })
        obj = AtendimentoProfessor(invalid_json)
        with self.assertRaises(ValueError):
            obj.get_predio()

if __name__ == '__main__':
    unittest.main()
