import unittest


class TestCase(unittest.TestCase):
    """
    测试报告功能点测试Testcase
    """
    @classmethod
    def setUpClass(cls) -> None:
        print("测试")

    def test_something(self):
        """
        测试。
        :return:
        """
        qiwang = 3

        self.assertEqual(2, qiwang)
    def test_02_xx(self):
        qiwang = 3
        self.assertEqual(3,qiwang)



if __name__ == '__main__':
    unittest.main()
