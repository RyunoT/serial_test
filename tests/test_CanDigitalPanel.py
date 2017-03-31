import unittest
from CanDigitalPanel import rs232c


class Test_CanDigitalPanel(unittest.TestCase):
    CDP = rs232c.rs232c(1)

    def setUp(self):
        # self.CDP = rs232c.rs232c(1)
        pass

    def tearDown(self):
        # self.CDP.rs232c_close()
        pass

    def test_CDP_setting_read(self):
        pass



if __name__ == "__main__":
    unittest.main()
