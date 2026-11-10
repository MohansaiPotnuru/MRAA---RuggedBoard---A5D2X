#!/usr/bin/env python3
"""Fade an external LED with PWM (MRAA pin 72 = connector M1 pin 16) on the RuggedBoard-A5D2X.

Wiring: LED anode -> M1 pin 16 (through a 330 ohm resistor), LED cathode -> M1 pin 8 (GND).
Run on the board:  python3 pwm_fade.py        (Ctrl+C to stop - PWM is disabled on exit)
"""
import time

import mraa

PWM_PIN = 72
PERIOD_US = 700       # ~1.43 kHz
STEP = 0.01
STEP_S = 0.05


def main() -> None:
    print("libmraa", mraa.getVersion(), "on", mraa.getPlatformName())
    pwm = mraa.Pwm(PWM_PIN)
    pwm.period_us(PERIOD_US)
    pwm.enable(True)

    duty = 0.0
    try:
        while True:
            pwm.write(duty)                       # duty cycle 0.0 .. 1.0
            print(f"duty {pwm.read():.6f}")       # value actually applied by the driver
            time.sleep(STEP_S)
            duty = duty + STEP if duty + STEP < 1.0 else 0.0
    except KeyboardInterrupt:
        pass
    finally:
        pwm.write(0.0)
        pwm.enable(False)
        print("\nPWM disabled")


if __name__ == "__main__":
    main()
