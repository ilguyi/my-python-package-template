from unittest import TestCase

from my_package import main


class TestCmd(TestCase):
  def test_hello_func(self):
    main()
