from CanDigitalPanel import rs232c
import time


def main_check():
    cdp = rs232c.rs232c(4)
    ret = cdp.into_program_mode()
    print(ret)

    ret = cdp.CDP_setting_write(30, 0)
    print(ret)

    ret = cdp.CDP_setting_read(30)
    print(ret)

    ret = cdp.CDP_setting_write(30, 2)
    print(ret)

    ret = cdp.CDP_setting_read(30)
    print(ret)

    cdp.CDP_setting_test(30, 0)
    cdp.CDP_setting_test(30, 1)
    cdp.CDP_setting_test(30, 2)

    ret = cdp.outof_program_mode()
    print(ret)

    cdp.rs232c_close()
    return

main_check()

