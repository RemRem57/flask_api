import time
import w1thermsensor

sensor = w1thermsensor.W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    print("Temperature : {:.2f} °C".format(temperature))
    time.sleep(1)