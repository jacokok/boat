from machine import PWM, Pin
from time import sleep
from ibus import IBus

ibus_in = IBus(1)
led = Pin(25, Pin.OUT)
pwmPin = Pin(2)
pwm = PWM(pwmPin)
pwm.freq(24)
led.on()
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


while True:
    res = ibus_in.read()
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

        channel3 = clamp(IBus.normalize(res[3]), -100, 100, 0, 100)
        print("channel", channel3)
        # print(channel3)
        pwm.duty_ns(getDutyNs(channel3))
    # else:
    #     print("Status offline {}".format(res[0]))

# while True:
#     print("Lets go")
#     pwm.duty_ns(1148000)
#     sleep(3)
#     # print("Full blast")
#     # pwm.duty_ns(1832000)
#     # sleep(3)

#     i = 1148000
#     while i < 1532000:
#         print("Increment")
#         i = i + 10
#         pwm.duty_ns(i)

#     pwm.duty_ns(1148000)
#     print("Done")
