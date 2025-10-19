import unittest
import sys
from io import StringIO

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        try:
            from solution import hello
        except SyntaxError as e:
            print(f"Синтаксическая ошибка: {e.msg}: строка - {e.lineno}")
            sys.exit(1)
        except ImportError:
            print("Функция 'hello' не определена")
            sys.exit(1)

        expected = "Hello, World!"
        try:
            result = hello()
        except Exception as e:
            print(f"Ошибка вызова hello(): {e}")
            sys.exit(1)

        if result != expected:
            print(f"Функция 'hello' вернула '{result}', ожидается '{expected}'")
            sys.exit(1)

    def test_hi(self):
        try:
            from solution import hi
        except ImportError:
            print("Функция 'hi' не определена")
            sys.exit(1)

        expected = "Hi!"
        try:
            result = hi()
        except Exception as e:
            print(f"Ошибка вызова hi(): {e}")
            sys.exit(1)

        if result != expected:
            print(f"Функция 'hi' вернула '{result}', ожидается '{expected}'")
            sys.exit(1)


if __name__ == "__main__":
    # Capture and discard all unittest output
    buffer = StringIO()
    runner = unittest.TextTestRunner(stream=buffer, verbosity=0)
    _ = unittest.main(testRunner=runner, exit=False)
