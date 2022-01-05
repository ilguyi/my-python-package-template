from unittest import TestCase

from my_package import hello


class TestHello(TestCase):
  def test_hello_func(self):
    s = hello.hello()
    self.assertTrue(isinstance(s, str))
