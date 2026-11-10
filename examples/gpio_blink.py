#!/usr/bin/env python3
"""Cycle the three on-board LEDs of the RuggedBoard-A5D2X (MRAA GPIO 61, 62, 63).

Run on the board:  python3 gpio_blink.py      (Ctrl+C to stop - LEDs are switched off)
"""
import time

import mraa

LED_PINS = (61, 62, 63)          # MRAA pin numbers, see board schematic (LEDs D4 / D17 / ...)
PATTERN = ((1, 0, 1), (0, 1, 0), (0, 0, 1))
STEP_S = 1.0


def main() -> None:
    print("libmraa", mraa.getVersion(), "on", mraa.getPlatformName())
    leds = []
    for pin in LED_PINS:
        gpio = mraa.Gpio(pin)
        gpio.dir(mraa.DIR_OUT)
        leds.append(gpio)
        print(f"gpio {pin} configured as output")

    try:
        while True:
            for states in PATTERN:
                for gpio, value in zip(leds, states):
                    gpio.write(value)
                print("LEDs", states)
                time.sleep(STEP_S)
    except KeyboardInterrupt:
        pass
    finally:
        for gpio in leds:
            gpio.write(0)
        print("\nLEDs off")


if __name__ == "__main__":
    main()
