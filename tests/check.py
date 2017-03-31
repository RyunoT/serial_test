from CanDigitalPanel import rs232c


def main_check():
    cdp = rs232c.rs232c(5)
    ret = cdp.into_program_mode()
    print(ret)

    ret = cdp.setting_write(30, 0)
    print(ret)

    ret = cdp.setting_read(30)
    print(ret)

    ret = cdp.setting_write(30, 2)
    print(ret)

    ret = cdp.setting_read(30)
    print(ret)

    cdp._setting_WriteRead(30, 0)
    cdp._setting_WriteRead(30, 1)
    cdp._setting_WriteRead(30, 2)

    ret = cdp.outof_program_mode()
    print(ret)

    cdp.rs232c_close()
    return



main_check()

