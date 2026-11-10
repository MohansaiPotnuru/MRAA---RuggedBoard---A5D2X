#!/usr/bin/env python3
"""Read a potentiometer on the mikroBUS "AN" pin (MRAA AIO 6) of the RuggedBoard-A5D2X.

Wiring: pot wiper -> mikroBUS AN, pot ends -> 3V3 (expansion header pin 1) and GND (pin 60).
Run on the board:  python3 aio_read.py        (Ctrl+C to stop)
"""
import sys
import time

import mraa

AIO_PIN = 6
VREF = 3.3        # ADC reference voltage
PERIOD_S = 0.5


def main() -> int:
    print("libmraa", mraa.getVersion(), "on", mraa.getPlatformName())
    try:
        adc = mraa.Aio(AIO_PIN)
    except ValueError as exc:            # raised when the pin has no ADC
        print(f"AIO {AIO_PIN} not available: {exc}", file=sys.stderr)
        return 1

    bits = adc.getBit()
    print(f"AIO {AIO_PIN}: {bits}-bit ADC")
    try:
        while True:
            raw = adc.read()             # 0 .. 2^bits - 1
            frac = adc.readFloat()       # 0.0 .. 1.0
            print(f"ADC raw 0x{raw:03X} ({raw:4d})  fraction {frac:.5f}  ~{frac * VREF:.3f} V")
            time.sleep(PERIOD_S)
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main())
