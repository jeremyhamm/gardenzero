#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError

shunt_ohms = 0.1
max_expected_amps = 0.6,
address=0x40

def read():
  ina = INA219(shunt_ohms, max_expected_amps, address)
  ina.configure()

  print("Bus Voltage: %.3f V" % ina.voltage())
  try:
    print("Bus Current: %.3f mA" % ina.current())
    print("Power: %.3f mW" % ina.power())
    print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
  except DeviceRangeError as e:
    # Current out of device range with specified shunt resistor
    print(e)


if __name__ == "__main__":
  read()
  
while 1:
  read_ina219()
  sleep(3)