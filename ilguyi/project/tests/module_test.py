from unittest import TestCase

from ilguyi.project import hello


class TestHello(TestCase):
  def test_hello_func(self):
    s = hello.hello()
    self.assertTrue(isinstance(s, str))
