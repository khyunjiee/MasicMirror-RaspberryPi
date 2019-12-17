import time
import Adafruit_DHT
import io
import socket
import struct
import picamera

client_socket = socket.socket()
client_socket.connect(('220.69.172.42',8000))
connection = client_socket.makefile('wb')

# 온습도 센서와 라즈베리 파이는 아래와 같이 다이렉트로 연결
# Signal(녹색) - GPIO4 (Pin no. 7)
# Vcc(빨강) - 5V 전원 (Pin no. 2)
# Ground(검정) - GND (Pin no. 6)

sensor = Adafruit_DHT.DHT11

pin = 4

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, pin)
        if h is not None and t is not None:
            if t > 29:
                with picamera.PiCamera() as camera:
                    camera.resolution = (1024, 768)
                    camera.start_preview()
                    time.sleep(2)

                    start = time.time()
                    stream = io.BytesIO()

                    for foo in camera.capture_continuous(stream, 'jpeg'):
                        connection.write(struct.pack('<L', stream.tell()))
                        connection.flush()
                        stream.seek(0)
                        connection.write(stream.read())

                        if time.time() - start > 30:
                            break
                        stream.seek(0)
                        stream.truncate()
                        break
            print("Tempurature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t,h))
        else:
            print("Read Error")
        time.sleep(1)
    conneection.write(struct.pack('<L',0))

except KeyboardInterrupt:
    print("Terminated by Keyboard")

finally:
    print("End of program")
    connection.close()
    client_socket.close()