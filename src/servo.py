from machine import Pin, PWM
from time import sleep

servo_pin = Pin(0)
servo = PWM(servo_pin)

# Set Duty Cycle for Different Angles
max_duty = 7864
min_duty = 1802
half_duty = int(max_duty / 2)

servo.freq(50)


def getDuty(percentage: int):
    percentage = max(min(percentage, 100), 10)
    return int(1802 + (7864 - 1802) * percentage / 100)


try:
    while True:
        duty = int(input("Enter percentage : "))
        servo.duty_u16(getDuty(duty))
        sleep(1)

except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM
    servo.deinit()
