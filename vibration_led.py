import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(37, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(35, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time.sleep(10)
count = 0
num = 0

try:
    while True:
        result = GPIO.input(23)
        print(result)
        if result == 1:
            count = count + 1
            if count == 1:
                print("진동이 감지 되었습니다.")
                GPIO.output(35, GPIO.LOW)
                GPIO.output(37, GPIO.HIGH)
                time.sleep(3)
        elif count > 2:
            count = 0
            GPIO.output(35, GPIO.HIGH)
            GPIO.output(37, GPIO.LOW)
            time.sleep(60)
            break
except KeyboardInterrupt:
    pass

GPIO.cleanup()
