#!/usr/bin/env python3
"""SPI loop-back test on the RuggedBoard-A5D2X (MRAA SPI bus 0).

Wiring: connect MOSI directly to MISO with one jumper wire.
With the jumper fitted every received frame must equal the transmitted one;
without it the test reports a mismatch and exits with status 1.
Run on the board:  python3 spi_loopback.py
"""
import random
import sys

import mraa

SPI_BUS = 0
FRAMES = 100
FRAME_LEN = 4
SPEED_HZ = 1_000_000


def main() -> int:
    print("libmraa", mraa.getVersion(), "on", mraa.getPlatformName())
    spi = mraa.Spi(SPI_BUS)
    spi.frequency(SPEED_HZ)
    spi.mode(mraa.SPI_MODE0)

    for i in range(FRAMES):
        tx = bytearray(random.randrange(256) for _ in range(FRAME_LEN))
        rx = spi.write(tx)               # full-duplex: returns the bytes clocked in on MISO
        if rx != tx:
            print(f"frame {i}: sent {tx.hex(' ')}, received {bytes(rx).hex(' ')}  -> MISMATCH")
            print("Is MOSI connected to MISO?")
            return 1
        print(f"frame {i:3d}: {tx.hex(' ')}  OK")

    print(f"PASS: {FRAMES} frames looped back correctly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
