import serial


class CDP_config:
    config = {
        # item: [begin, end, float_change]
        1: [0, 2, 1],
        2: [0, 4, 1],
        3: [1, 99, 0.1],  # [0.1, 9.9]
        4: [1, 9, 1],
        5: [2, 9999, 1],
        6: [1, 99, 1],
        7: [0, 1, 1],
        10: [1, 9999, 1],
        11: [1, 9999, 1],
        #12: [0, 6, 1],  bug!!!!!
        12: [1, 6, 1],
        13: [0, 1, 1],
        14: [0, 1, 1],
        15: [0, 1, 1],
        16: [0, 1, 1],
        17: [0, 1, 1],
        #20: [1, 99999, 1],
        #21: [1, 99999, 1],
        #22: [1, 99999, 1],
        #23: [1, 99999, 1],
        30: [0, 3, 1],
    }


class rs232c:
    def __init__(self, port_num):
        self.ser = serial.Serial(port=port_num - 1,
                                 baudrate=115200,
                                 bytesize=8,
                                 parity="N",
                                 stopbits=1,
                                 timeout=1)
        self.read_buff = None
        self.write_buff = None
        self._rs232c_write("S")

    def rs232c_close(self):
        self.ser.close()
        return

    def _rs232c_readline(self):
        self.read_buff = self.ser.readline()
        return self.read_buff

    def _rs232c_write(self, write_line):
        self.write_buff = write_line.encode("utf-8")
        self.ser.write(self.write_buff)
        return self._rs232c_readline()

    def into_program_mode(self):
        self._rs232c_write("P")
        return self.read_buff

    def outof_program_mode(self):
        self._rs232c_write("E\r")
        return self.read_buff

    def setting_read(self, item):
        line = "RP" + str(item).zfill(2) + "\r"
        self._rs232c_write(line)
        return self.read_buff

    def setting_write(self, item, value):
        line = "WP" + str(item).zfill(2) + "," + str(value) + "\r"
        self._rs232c_write(line)
        return self.read_buff

