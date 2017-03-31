from CanDigitalPanel import rs232c


def main():
    cdp = rs232c.rs232c(3)
    cdp.into_program_mode()

    ret = cdp.CDP_setting_write(1, 0)
    print(ret)

    ret = cdp.CDP_setting_read(1)
    print(ret)

    ret = cdp.CDP_setting_write(1, 1)
    print(ret)

    ret = cdp.CDP_setting_read(1)
    print(ret)


main()

