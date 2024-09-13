import unittest

def run_tests():
    # Descobre e executa todos os testes no diretório 'tests'
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='*_test.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run_tests()
