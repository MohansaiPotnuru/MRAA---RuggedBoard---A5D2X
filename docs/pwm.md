# PWM: fade an LED

Ramps the PWM duty cycle from 0 % to 100 % over and over, fading an external LED.

| | |
|---|---|
| Script | [`examples/pwm_fade.py`](../examples/pwm_fade.py) |
| MRAA pin | 72 (connector **M1**, pin 16) |
| Extra hardware | LED + 330 Ω resistor |

## Wiring

| LED | Board |
|---|---|
| Anode (+, long leg), through the 330 Ω resistor | M1 pin 16 |
| Cathode (−) | M1 pin 8 (GND) |

## Steps

```sh
root@ruggedboard-a5d2x:/data# python3 pwm_fade.py
```

The LED brightens over about 5 s, then starts again from off. **Ctrl+C** sets the output to 0 and disables PWM.

## Expected output

```text
libmraa v2.0.0 on Atmel SAMA5
duty 0.000000
duty 0.010000
duty 0.020000
...
duty 0.049995
...
```

`pwm.read()` returns the duty cycle the driver actually applied. Small differences such as `0.049995` instead of `0.05` come from the hardware timer resolution at a 700 µs period.

## Key API

```python
pwm = mraa.Pwm(72)
pwm.period_us(700)   # period in microseconds (~1.43 kHz)
pwm.enable(True)
pwm.write(0.25)      # duty cycle 0.0 .. 1.0
pwm.read()           # current duty cycle
```
