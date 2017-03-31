import unittest

class CDP_config:
    config = {
        # item: [begin, end, float_change]
        1: [0, 2, 1],
        2: [0, 5, 1],
        3: [1, 99, 0.1],  # [0.1, 9.9]
        4: [1, 9, 1],
#        5: [2, 9999, 1],
#        6: [1, 99, 1],
#        7: [0, 1, 1],
#        10: [1, 9999, 1],
#        11: [1, 9999, 1],
#        12: [0, 6, 1],
#        13: [0, 1, 1],
#        14: [0, 1, 1],
#        15: [0, 1, 1],
#        16: [0, 1, 1],
#        17: [0, 1, 1],
#        20: [1, 99999, 1],
#        21: [1, 99999, 1],
#        22: [1, 99999, 1],
#        23: [1, 99999, 1],
        30: [0, 3, 1],
    }


class Test_NoConnection(unittest.TestCase):
    def test_MakeBytesLine(self):
        s = "RP" + str(1).zfill(2) + "\r"
        s = s.encode("utf-8")
        self.assertEquals(b"RP01\r", s)

    def test_all_CDP_setting_test(self):
        keys = CDP_config.config.keys()
        for i in keys:
            begin, end, float_change = CDP_config.config[i]
            for j in range(begin, end + 1):
                # 小数変換
                deci = round(j * float_change, 6)
                print("item:{0}, value:{1}".format(i, deci))
            print("Finish WP{0} and RP{0} test".format(str(i).zfill(2)))

        print("Finish all_setting_test")






if __name__ == "__main__":
    unittest.main()

