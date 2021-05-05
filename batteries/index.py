from ina219 import INA219, DeviceRangeError
from time import sleep

SHUNT_OHM = 0.1
MAXCURRENT = 0.4

#ina = INA219(SHUNT_OHM, MAXCURRENT)
ina = INA219(SHUNT_OHM)

#ina.configure(ina.RANGE_16V, ina.GAIN_1_40MV)
ina.configure(ina.RANGE_16V, ina.GAIN_AUTO)
#ina.configure()


def read_ina219():
  #ina = INA219(SHUNT_OHM)
  #ina.configure(ina.RANGE_16V, ina.GAIN_AUTO)
  try:
    Uges = ina.voltage() + ina.shunt_voltage()/1000
    
    spannung = round(ina.voltage(), 3)
    strom = ina.current()
    leistung =round(ina.power(), 3)
    supply = round(ina.supply_voltage(), 3)
    shuntV = round(ina.shunt_voltage(), 3)
    
    print(str(spannung) + "V " + str(strom) + "mA " + str(leistung) + "mW  | supply: " + str(supply) + "V  | shunt: " + str(shuntV) + "mV  | Uges: " + str(Uges) + "V")
      
  except DeviceRangeError as e:
    print("too high")
  
  
while 1:
  read_ina219()
  sleep(3)