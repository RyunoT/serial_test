import unittest
from CanDigitalPanel import rs232c


class Test_CanDigitalPanel(unittest.TestCase):
    CDP = rs232c.rs232c(5)
    dic = rs232c.CDP_config

    def setUp(self):
        self.CDP.into_program_mode()

    def tearDown(self):
        self.CDP.outof_program_mode()

    def _test_setting_WriteRead(self, item, value):
        ret_w = self.CDP.setting_write(item, value)
        self.assertEquals(b"O\r\n", ret_w)

        ret_r = self.CDP.setting_read(item)
        ret_r_uni = int((ret_r.decode("utf-8")).split()[0])
        exp_r = value
        self.assertEqual(exp_r, ret_r_uni)

    def _test_single_setting(self):
        self._test_setting_WriteRead(30, 0)
        self._test_setting_WriteRead(30, 2)

    def test_all_setting(self):
        keys = self.dic.config.keys()
        for i in keys:
            with self.subTest(i=i):
                begin, end, float_change = self.dic.config[i]
                for j in range(begin, end + 1):
                    with self.subTest(j=j):
                        # 小数変換
                        deci = round(j * float_change, 6)
                        self._test_setting_WriteRead(i, j)



if __name__ == "__main__":
    unittest.main()
