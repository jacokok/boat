from machine import PWM, Pin
from time import sleep
from ibus import IBus

ibus_in = IBus(1)
led = Pin(25, Pin.OUT)
pwmPin = Pin(2)
pwm = PWM(pwmPin)
pwm.freq(24)
led.on()

servo_pin = Pin(0)
servo = PWM(servo_pin)
servo.freq(50)

# machine.freq(240000000)


def getDutyNs(percentage: int):
    # Deadzone
    if percentage < 5 and percentage > 0:
        return 1148000
    if percentage < 0 and percentage > -5:
        return 1148000
    result = int(1148000 + (1832000 - 1148000) * percentage / 100)
    print(result)
    return result


# def clamp(value: int, min_value: int, max_value: int):
#     if value - 20 > max_value:
#         return min_value
#     return max(min(value, max_value), min_value)


def clamp(value: int, original_min: int, original_max: int, new_min: int, new_max: int):
    if value - 20 > original_max:
        return new_min
    result = int(
        ((value - original_min) / (original_max - original_min)) * (new_max - new_min)
        + new_min
    )
    if result <= 1:
        return new_min
    return result


def getServoDuty(percentage: int):
    percentage = max(min(percentage, 100), 10)
    return int(1802 + (7864 - 1802) * percentage / 100)


try:
    while True:
        res = ibus_in.read()
        print(res)
        # if signal then display immediately
        if res[0] == 1:
            # print(
            #     "Status {} CH 1 {} Ch 2 {} Ch 3 {} Ch 4 {} Ch 5 {} Ch 6 {}".format(
            #         res[0],  # Status
            #         IBus.normalize(res[1]),
            #         IBus.normalize(res[2]),
            #         IBus.normalize(res[3]),
            #         IBus.normalize(res[4]),
            #         IBus.normalize(res[5], type="dial"),
            #         IBus.normalize(res[6], type="dial"),
            #     ),
            #     end="",
            # )
            # print(IBus.normalize(res[3]))
            # print(IBus.normalize(res[4]))
            # channel1 = IBus.normalize(res[1])
            # if channel1 < 100 and channel1 > -100:
            #     print(channel1)

            channel1 = clamp(IBus.normalize(res[1]), -100, 100, 0, 100)
            channel3 = clamp(IBus.normalize(res[3]), -100, 100, 0, 100)
            # print("channel", channel3)
            # print(channel3)
            print("channel1", channel1)
            pwm.duty_ns(getDutyNs(channel3))
            servo.duty_u16(getServoDuty(channel1))

except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM
    pwm.deinit()
    servo.deinit()
