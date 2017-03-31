import unittest
from CanDigitalPanel import rs232c


class Test_CanDigitalPanel(unittest.TestCase):
    CDP = rs232c.rs232c(4)

    def setUp(self):
        self.CDP.into_program_mode()

    def tearDown(self):
        self.CDP.outof_program_mode()

    def test_setting_WriteRead(self):
        ret_w = self.CDP.CDP_setting_write(30, 0)
        self.assertEquals(b"O\r\n", ret_w)

        ret_r = self.CDP.CDP_setting_read(30)
        self.assertEqual(b"0\r\n", ret_r)


if __name__ == "__main__":
    unittest.main()
