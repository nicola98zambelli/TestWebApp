import unittest
from api import app


class TestCalculatorAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_add(self):
        response = self.client.get("/add?a=10&b=20")
        self.assertEqual(response.json["result"], 30)
        print("add ok")

    def test_subtract(self):
        response = self.client.get("/subtract?a=20&b=10")
        self.assertEqual(response.json["result"], 10)
        print("subtract ok")

    def test_multiply(self):
        response = self.client.get("/multiply?a=20&b=10")
        self.assertEqual(response.json["result"], 200)
        print("multiply ok")

    def test_divide(self):
        response = self.client.get("/divide?a=20&b=10")
        self.assertEqual(response.json["result"], 2)
        print("divide ok")

    def test_power(self):
        response = self.client.get("/power?base=2&exp=3")
        self.assertEqual(response.json["result"], 8)
        print("power ok")

    def test_square_root(self):
        response = self.client.get("/square-root?num=49")
        self.assertEqual(response.json["result"], 7)
        print("square root ok")

    def test_modulus(self):
        response = self.client.get("/modulus?a=5&b=2")
        self.assertEqual(response.json["result"],1)
        print("modulus ok")


if __name__ == "__main__":
    unittest.main()
