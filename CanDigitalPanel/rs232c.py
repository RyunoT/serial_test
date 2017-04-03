import serial


class CDP_config:
    config = {
        # item: [begin, end, float_change, initial]
        1:  [0, 2, 1, 0],
        2:  [0, 4, 1, 1],
        3:  [1, 99, 0.1, 3],  # [0.1, 9.9]
        4:  [1, 9, 1, 1],
        5:  [2, 9999, 1, 2],
        6:  [1, 99, 1, 25],
        7:  [0, 1, 1, 0],
        10: [1, 9999, 1, 300],
        11: [1, 9999, 1, 700],
        12: [0, 6, 1, 5],  # bug!!!!!
        13: [0, 1, 1, 1],
        14: [0, 1, 1, 1],
        15: [0, 1, 1, 0],
        16: [0, 1, 1, 0],
        17: [0, 1, 1, 0],
        20: [1, 99999, 1, 20000],
        21: [1, 99999, 1, 20000],
        22: [1, 99999, 1, 1],
        23: [1, 99999, 1, 1],
        30: [0, 3, 1, 0],
    }

#    initial_config = {
#        1: 0,
#        2: 1,
#        3: 0.3,
#        4: 1,
#        5: 2,
#        6: 25,
#        7: 0,
#        10: 300,
#        11: 700,
#        12: 5,
#        13: 1,
#        14: 1,
#        15: 0,
#        16: 0,
#        17: 0,
#        20: 20000,
#        21: 20000,
#        22: 1,
#        23: 1,
#        30: 0,
#    }


class rs232c:
    config = CDP_config()

    def __init__(self, port, boudrate):
        self.port = port
        self.boudrate = boudrate
        self.ser = None
        self.read_buff = str()
        self.write_buff = str()

    def is_opened(self):
        self.ser = serial.Serial(port=self.port - 1,
                                 baudrate=self.boudrate,
                                 bytesize=8,
                                 parity="N",
                                 stopbits=1,
                                 timeout=1)
        self._rs232c_write("S")     # stop output mode

    def is_closed(self):
        self.ser.close()
        return

    def _serial_readline(self):
        self.read_buff = self.ser.readline()
        return self.read_buff

    def _rs232c_write(self, write_line):
        self.write_buff = write_line.encode("utf-8")
        self.ser.write(self.write_buff)
        self.read_buff = self._serial_readline()
        return self.read_buff

    def into_program_mode(self):
        self._rs232c_write("P")
        return self.read_buff

    def outof_program_mode(self):
        self._rs232c_write("E\r")
        return self.read_buff

    def _RP(self, item):
        line = "RP" + str(item).zfill(2) + "\r"
        return line

    def setting_read(self, item):
        self._rs232c_write(self._RP(item))
        return self.read_buff

    def _WP(self, item, value):
        line = "WP" + str(item).zfill(2) + "," + str(value) + "\r"
        return line

    def setting_write(self, item, value):
        self._rs232c_write(self._WP(item, value))
        return self.read_buff

    def initial_setting(self):
        initial_keys = self.config.config.keys()
        for i in initial_keys:
            initial_value = self.config.config[3]
            self.setting_write(i, initial_value)
