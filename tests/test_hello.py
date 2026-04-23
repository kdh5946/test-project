import unittest

from hello import get_message


class TestHello(unittest.TestCase):
    def test_get_message(self) -> None:
        self.assertEqual(get_message(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
