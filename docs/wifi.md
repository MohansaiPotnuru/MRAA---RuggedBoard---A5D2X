# Wi-Fi: connect to a WPA2 network

Steps to join a WPA/WPA2-PSK access point with `wpa_supplicant` on the Yocto BSP.

## 1. Configure the network

Edit `/etc/wpa_supplicant.conf`:

```sh
vi /etc/wpa_supplicant.conf
```

```conf
ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=0
update_config=1

network={
    ssid="YOUR_SSID"
    psk="YOUR_PASSPHRASE"      # WPA2 passphrase: 8-63 characters
    proto=RSN                  # RSN = WPA2
    key_mgmt=WPA-PSK
    pairwise=CCMP
    group=CCMP
}
```

> Use `proto=RSN` with `CCMP` (AES) for WPA2. If you must support a legacy WPA1/TKIP router, use `proto=WPA RSN`, `pairwise=CCMP TKIP` and `group=CCMP TKIP`.

## 2. Bring the interface up and connect

```sh
ip link set wlan0 up
wpa_supplicant -B -D nl80211 -i wlan0 -c /etc/wpa_supplicant.conf
udhcpc -i wlan0            # get an IP address via DHCP
```

## 3. Verify

```sh
wpa_cli -i wlan0 status    # wpa_state=COMPLETED when associated
ip addr show wlan0         # shows the leased IP address
ping -c 3 8.8.8.8
```

## Notes

- **Put Wi-Fi and Ethernet on different subnets.** If `eth0` and `wlan0` both get addresses in the same subnet, the kernel has two routes to that network. Replies can then leave through the wrong interface and connections fail. Unplug Ethernet or use a different subnet.
- If `wpa_supplicant` reports `Failed to initialize driver interface`, try `-D wext` instead of `-D nl80211`.
- Don't commit real SSIDs or passphrases to version control.
