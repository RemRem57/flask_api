from flask import Flask, Response
import time
from prometheus_client import Counter, Gauge, start_http_server, generate_latest
import RPi.GPIO as GPIO
import w1thermsensor

content_type = str('text/plain; version=0.0.4; charset=utf-8')
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN,
           pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)

thermal_sensor = w1thermsensor.W1ThermSensor()  # Thermal sensor object


def get_temperature():
    temperature = read_temp()
    temperature = format(temperature, ".2f")
    if all(v is not None for v in [temperature]):  # if all values are not None
        response = {"temperature": temperature}
        return response
    else:
        time.sleep(0.2)
        temperature = 30
        temperature = format(temperature, ".2f")
        response = {"temperature": temperature}
        return response


def read_temp():
    # For test return the button state (0 or 1)
    return thermal_sensor.get_temperature()


app = Flask(__name__)

current_temperature = Gauge(
    'current_temperature',
    'the current temperature in celsius, this is a gauge as the value can increase or decrease',
    ['cave']
)


@app.route('/metrics')
def metrics():
    metrics_object = get_temperature()
    current_temperature.labels('study').set(metrics_object['temperature'])
    return Response(generate_latest(), mimetype=content_type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
