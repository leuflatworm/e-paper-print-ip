# e-paper-print-ip
This script print RaspberryPi's IP address when booting.

Print IP address, OS and last update.

Dipendence

python3

# How to use
go to home (if you want to use another account, you can change directory)

```
cd /home/pi/
```

download waveshare sample code

```
wget https://www.waveshare.com/w/upload/3/3f/2.13inch-e-paper-hat-b-code.7z

git clone https://github.com/leuflatworm/e-paper-print-ip.git
```

Move etc/systemd/system,home/pi/Raspberrypi/python3,opt to each directory

```
mv etc/systemd/system/* /etc/systemd/system/
mv home/pi/Raspberrypi/python3/* /home/pi/Raspberrypi/python3/
mv opt/* /opt/
```

enable print-ip.service

```
sudo systemctl enable print-ip.service
```
