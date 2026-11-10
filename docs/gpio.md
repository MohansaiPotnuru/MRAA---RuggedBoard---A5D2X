# GPIO: blink the on-board LEDs

Cycles the three user LEDs on the RuggedBoard-A5D2X through a simple pattern using `mraa.Gpio`.

| | |
|---|---|
| Script | [`examples/gpio_blink.py`](../examples/gpio_blink.py) |
| MRAA pins | 61, 62, 63 (on-board LEDs, see board schematic) |
| Extra hardware | none |

## Steps

1. Boot the board from SD card or NOR flash and log in on the serial console.
2. Copy the script to `/data` on the board (see [copying files](../README.md#copying-files-to-the-board)).
3. Run it:

   ```sh
   root@ruggedboard-a5d2x:/data# python3 gpio_blink.py
   ```

The LEDs step through `(1,0,1) → (0,1,0) → (0,0,1)`, one step per second. Press **Ctrl+C** to stop; the script switches all LEDs off on exit.

## Expected output

```text
libmraa[145]: libmraa version v2.0.0 initialised by user 'root' with EUID 0
libmraa[145]: gpio: platform doesn't support chardev, falling back to sysfs
libmraa[145]: libmraa initialised for platform 'Atmel SAMA5' of type 20
libmraa v2.0.0 on Atmel SAMA5
gpio 61 configured as output
gpio 62 configured as output
gpio 63 configured as output
LEDs (1, 0, 1)
LEDs (0, 1, 0)
LEDs (0, 0, 1)
...
```

The `libmraa[...]` lines come from the library itself. *"falling back to sysfs"* is normal on this kernel (v4.9), which has no GPIO character-device support.

## Key API

```python
gpio = mraa.Gpio(61)       # MRAA pin number
gpio.dir(mraa.DIR_OUT)     # or mraa.DIR_IN
gpio.write(1)              # 1 = high, 0 = low
value = gpio.read()        # for inputs
```
