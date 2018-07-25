# Braille Point Gateway Server

## ANDROID APP INSTALLATION

http://brltty.app/download.html#android

## SERVER INSTALLATION

### Check Python Version
``` 
python3 --version
``` 

### Installing Python 3.6

#### Install the required build-tools 
``` 
sudo apt update && upgrade -y
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
```

#### Install Python
``` 
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
tar xf Python-3.6.5.tar.xz
cd Python-3.6.5
./configure
make
sudo make altinstall
```

### Installing Python-Bluethooth Library
``` 

```


## STARTING SERVER

Then to start the server, all you need to do is run the server with the following command from your terminal. As long as the server runs, you will be able to send commands to it. 

```
sudo ~/.blink/bluetooth_server.py
```

## HELP

The hardest part of this is getting the server installed and running. If you struggle to get the bluetooth to work, maybe this will help:

*This guide helped me allot, original post: [Bluetooth Setup](http://blog.davidvassallo.me/2014/05/11/android-linux-raspberry-pi-bluetooth-communication/)*
> There are plenty of guides in the internet on how to get bluetooth working, but the only method that worked consistently for me is the following:
> Disable bluetooth pnat support as there seems to be a bug which stops proper operation with pnat enabled. Full details can be found here:  
> https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=690749

> A workaround is to add the following to /etc/bluetooth/main.conf:
```
DisablePlugins = pnat
```


### Permissions Issues:
This has been reported as helpfull for sorting out permissions issues on Ubuntu 15.10. Thanks @jachym for providing the link:
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


### OTHER KNOWN ISSUES

I will try and document the known issues and fixes as they arise. 

Fedora 22 error:

```
File "/usr/lib64/python2.7/site-packages/bluetooth/bluez.py", line 176, in advertise_service
  raise BluetoothError (str (e))
bluetooth.btcommon.BluetoothError: (2, 'No such file or directory')
```

Fedora 22 Fix:
https://thatguy.co.za/Blog/Article/python-bluez-issues-since-upgrading-to-fedora-22

Pyhon3:
Unfortunately pybluez does not work properly on Python3, it was meant to be part of Python itself, but wasn't ported properly. For now the server **will only work on Python2.7**.
