# https://docs.python.org/zh-tw/3/library/unittest.html
# python3 [-v] simple.py


# 搭配模組
## python3 -m unittest -h

## python3 -m unittest [test_module].[test_class].[test_method]
## python3 -m unittest simple.my_class

TYPE = "TEST_ALL"
#TYPE = "TEST_USERDEF"

import unittest

class my_class(unittest.TestCase):

    def setUp(self):
        "before each test "
    def tearDown(self):
        "after each test "

    def test_eq(self):
        self.assertEqual(1, 1)

    def test_True(self):
        self.assertTrue(True)

    def test_False(self):
        self.assertFalse(False)

    def test_split(self):
        with self.assertRaises(TypeError):      # 要求觸發 typeError
            "hello".split(1)                    # trigger typeError

    def test_skip(self):
        if True:
            self.skipTest("no reason")
        self.fail("shouldn't happen")

    @unittest.skipUnless(1==2, "Unless 1==2 or skip the test")
    #@unittest.skipIf(True, "skip if true")
    #@unittest.skip("Add this line to skip this test")
    def test_fail(self):
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_fail_again(self):
        self.fail("shouldn't happen")

    def test_zero(self):
        for i in range(3):
            with self.subTest(i=i):              # 印出所有錯誤
                self.assertEqual(i, 0)



if __name__ == "__main__":
    if TYPE == "TEST_ALL":
        unittest.main()
    
    
    if TYPE == "TEST_USERDEF":
        def suite():
            suite = unittest.TestSuite()
            suite.addTest(my_class('test_eq'))
            suite.addTest(my_class('test_True'))
            return suite
    
        runner = unittest.TextTestRunner()
        runner.run(suite())
