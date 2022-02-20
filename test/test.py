#!/usr/bin/python

import usb.core
dev = usb.core.find(idVendor=0x0483, idProduct=0x5740)
buf = b'\xa5\xa5\xff\x00\x01\x05\x06\x07'
dev.write(0x04, buf)
print(dev.read(0x85, len(buf)))
