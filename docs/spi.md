# SPI: loop-back test

Sends 100 random 4-byte frames on SPI bus 0 and checks that each one comes back unchanged. This verifies the SPI controller, the driver and the MRAA bindings without any external device.

| | |
|---|---|
| Script | [`examples/spi_loopback.py`](../examples/spi_loopback.py) |
| MRAA bus | SPI 0, mode 0, 1 MHz |
| Extra hardware | one jumper wire |

## Wiring

Connect **MOSI to MISO** with a jumper wire. Whatever the controller shifts out is then shifted straight back in.

## Steps

```sh
root@ruggedboard-a5d2x:/data# python3 spi_loopback.py
```

## Expected output

With MOSI and MISO connected:

```text
libmraa v2.0.0 on Atmel SAMA5
frame   0: d1 a2 80 93  OK
frame   1: 7a 3a 6c 11  OK
...
frame  99: aa f1 4c aa  OK
PASS: 100 frames looped back correctly
```

Without the jumper, MISO floats or reads all zeros, so the very first frame fails. Example:

```text
frame 0: sent 2e 05 5c 13, received 00 00 00 00  -> MISMATCH
Is MOSI connected to MISO?
```

The script exits with status `0` on pass and `1` on fail, so you can use it in test scripts.

## Key API

```python
spi = mraa.Spi(0)
spi.frequency(1_000_000)
spi.mode(mraa.SPI_MODE0)
rx = spi.write(bytearray(b"\x01\x02"))   # full duplex: returns received bytes
```
