# MRAA Python Examples for RuggedBoard-A5D2X

Python examples and step-by-step guides for using **[Eclipse MRAA](https://github.com/eclipse/mraa)** (libmraa v2.0.0) on the **RuggedBoard-A5D2X**. The board is an industrial single-board computer built on the Microchip **SAMA5D2** (ARM Cortex-A5) SOM. The examples cover the four basic peripheral interfaces, plus Wi-Fi setup.

| Interface | Guide | Script | What it does | Extra hardware |
|---|---|---|---|---|
| GPIO | [docs/gpio.md](docs/gpio.md) | [gpio_blink.py](examples/gpio_blink.py) | Cycles the 3 on-board LEDs | – |
| AIO (ADC) | [docs/aio.md](docs/aio.md) | [aio_read.py](examples/aio_read.py) | Reads a potentiometer: raw count, fraction, volts | Potentiometer |
| PWM | [docs/pwm.md](docs/pwm.md) | [pwm_fade.py](examples/pwm_fade.py) | Fades an LED by ramping the duty cycle | LED + 330 Ω |
| SPI | [docs/spi.md](docs/spi.md) | [spi_loopback.py](examples/spi_loopback.py) | MOSI→MISO loop-back self-test with pass/fail exit code | 1 jumper wire |
| Wi-Fi | [docs/wifi.md](docs/wifi.md) | – | Connects to WPA2 with `wpa_supplicant` + DHCP | – |

## Target platform

| | |
|---|---|
| Carrier board | RuggedBoard-A5D2X, rev. RB-A5D2X-V1.1 |
| SOM | PICM-001-A1 (Microchip SAMA5D2) |
| BSP | BSP-Yocto-A5D2X 2019-03-13: Yocto 2.5.2 *sumo* (commit `623b77885051`) |
| Bootloaders | AT91Bootstrap 3.8.12, U-Boot 2018.07 |
| Kernel | Linux 4.9.151 |
| Library | libmraa v2.0.0 with Python 3 bindings (platform reported as `Atmel SAMA5`) |

## Quick start

1. Boot the board from SD card (MMC) or NOR flash. Log in as `root` on the USB serial console (115200 8N1).
2. Copy the `examples/` scripts to `/data` on the board (see below).
3. Run one, for example `python3 /data/gpio_blink.py`.

The expected-output sections in `docs/` are based on runs on real hardware. The scripts were tidied up afterwards, so re-run them on your board and update the outputs if anything differs.

All scripts print the libmraa version and platform at start-up and exit cleanly on **Ctrl+C**, leaving outputs switched off.

### Copying files to the board

With the board and PC on the same network:

```sh
# from the PC (if the image has an SSH server)
scp examples/*.py root@<board-ip>:/data/

# or from the board, pulling from a TFTP server on the PC
cd /data && tftp -g -r gpio_blink.py <pc-ip>
```

## MRAA pin reference used here

| Function | MRAA number | Physical location |
|---|---|---|
| LED 1 / 2 / 3 | GPIO 61 / 62 / 63 | On-board LEDs |
| ADC input | AIO 6 | mikroBUS `AN` |
| PWM output | 72 | Connector M1, pin 16 |
| SPI | bus 0 | mikroBUS / expansion SPI (MOSI, MISO, SCK, CS) |
| 3V3 / GND | – | Expansion header pin 1 / pin 60 |

Check pin numbers against the RuggedBoard-A5D2X schematic for your board revision.

## Repository layout

```text
├── examples/   # Runnable Python 3 scripts (copy to the board)
└── docs/       # One guide per interface: wiring, steps, expected output, API summary
```

## Changelog

- Converted the plain-text notes into Markdown guides and standalone, runnable scripts.
- Corrected mismatches between code and documented output:
  - GPIO: the output showed pins 77/81/83, but the code used 61/62/63, and the comments were wrong.
  - AIO and PWM: the code printed nothing, or a different format from the one documented.
  - Script filenames were inconsistent.
- Fixed the Wi-Fi example. Its 7-character passphrase was invalid (WPA2 needs 8–63), and it now uses placeholders instead of real credentials. The configuration was simplified to WPA2/CCMP, and DHCP and verification steps were added.
- Added safe shutdown (LEDs and PWM off on exit), error handling, and a pass/fail exit code for the SPI test.
- Removed the unused copy of the upstream MRAA build system (CMake, Doxygen, Travis, Docker files). It referenced source directories that aren't in this repository, so it couldn't build. To build libmraa itself, use the [upstream repository](https://github.com/eclipse/mraa).

## Author

**P. Mohan Sai** – [GitHub](https://github.com/MohansaiPotnuru)
