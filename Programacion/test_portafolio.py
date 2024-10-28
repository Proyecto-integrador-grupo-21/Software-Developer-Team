import unittest
from portafolio import Portafolio

class TestPortafolio(unittest.TestCase):

    def setUp(self):
        self.cuil = "20-12335178-9"
        
        self.portafolio = Portafolio(self.cuil)

    def test_calcular_acciones(self):
        acciones, total_invertido_actual = self.portafolio.calcular_acciones()

        self.assertTrue(len(acciones) > 0, "Debería haber acciones en el portafolio.")
        

    def test_mostrar_acciones(self):
        from io import StringIO
        import sys

        output = StringIO()
        sys.stdout = output

        self.portafolio.mostrar_acciones()

        sys.stdout = sys.__stdout__

        printed_output = output.getvalue()

        self.assertIn("Total invertido en acciones que se poseen actualmente:", printed_output)

if __name__ == '__main__':
    unittest.main()
