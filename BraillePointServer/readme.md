# Braille Point Gateway Server

this file is under construction

## ANDROID APP INSTALLATION

http://brltty.app/download.html#android

## Server installation
````bash
sudo apt-get install bluez python3-bluez xdotool
sudo apt install python3-rpi.gpio
````
## Run Server

```
cd BraillePointServer
sudo python3 main.py
```

## Help

The hardest part of this is getting the server installed and running. If you struggle to get the bluetooth to work, maybe this will help:

*This guide helped me a lot, original post: [Bluetooth Setup](http://blog.davidvassallo.me/2014/05/11/android-linux-raspberry-pi-bluetooth-communication/)*
> There are plenty of guides on the internet on how to get bluetooth working, but the only method that worked consistently for me is the following:
> Disable bluetooth pnat support as there seems to be a bug which stops proper operation with pnat enabled. Full details can be found here:  
> https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=690749

> A workaround is to add the following to /etc/bluetooth/main.conf:
```
DisablePlugins = pnat
```


### Permissions issues

This has been reported as helpful for sorting out permissions issues on Ubuntu 15.10. Thanks @jachym for providing the link:
https://code.google.com/p/pybluez/issues/detail?id=62

```shell
# TLDR
# Adding the --compat to the bluetooth server configuration. And restarting the bluetooth service
# SYSTEM D systems like REHL addopted it first, but now Ubuntu 15 also has
# List of OS's running SYSTEM D
# https://en.wikipedia.org/wiki/Systemd

sudo vim /usr/lib/systemd/system/bluetooth.service

# change this: ExecStart=/usr/libexec/bluetooth/bluetoothd
# to this: ExecStart=/usr/libexec/bluetooth/bluetoothd --compat
# Restart the bluetooth service
sudo service bluetooth restart

# Check that it has changed by running 
sudo service bluetooth status | grep -i --compat
```
