# AIO: read a potentiometer with the ADC

Reads an analog voltage on the mikroBUS **AN** pin with `mraa.Aio` and prints the raw count, the 0–1 fraction and the approximate voltage.

| | |
|---|---|
| Script | [`examples/aio_read.py`](../examples/aio_read.py) |
| MRAA pin | AIO 6 (mikroBUS `AN`) |
| Extra hardware | 10 kΩ potentiometer, 3 jumper wires |

## Wiring

| Potentiometer | Board |
|---|---|
| Wiper (middle pin) | mikroBUS `AN` |
| One outer pin | Expansion header pin 1 (3V3) |
| Other outer pin | Expansion header pin 60 (GND) |

> Keep the input between 0 V and 3.3 V. Don't connect 5 V to the ADC pin.

## Steps

```sh
root@ruggedboard-a5d2x:/data# python3 aio_read.py
```

Turn the potentiometer; the readings follow it. Press **Ctrl+C** to stop.

## Expected output

The values below are from the original test run, with the wiper at mid-travel:

```text
libmraa v2.0.0 on Atmel SAMA5
AIO 6: 10-bit ADC
ADC raw 0x1FB ( 507)  fraction 0.49560  ~1.635 V
ADC raw 0x1FC ( 508)  fraction 0.49658  ~1.639 V
ADC raw 0x1F0 ( 496)  fraction 0.48485  ~1.600 V
...
```

A mid-position wiper gives about half of full scale (≈ 512 of 1023). If you see `AIO 6 not available`, the ADC driver isn't enabled in the device tree.

## Key API

```python
adc = mraa.Aio(6)
adc.getBit()      # ADC resolution in bits
adc.read()        # raw integer count
adc.readFloat()   # normalised 0.0 .. 1.0
```
