#!/bin/bash

apt update
apt dist-upgrade
apt install git python-pip -y
pip install adafruit-ws2801

mkdir /home/pi/logs && chown pi.pi /home/pi/logs && chmod 755 /home/pi/logs
echo "@reboot date >>/home/pi/logs/cron.log 2>&1 && cd /home/pi && rm -rf /home/pi/blink && until ping -c 2 github.com ; do sleep 1; done ; echo "Server responding" >>/home/pi/logs/cron.log 2>&1 && git clone https://github.com/DXorSX/blink.git >>/home/pi/logs/cron.log 2>&1 && cd /home/pi/blink && python2.7 -u runner.py >>/home/pi/logs/runner.log #Do not modify: runner.py start" | sudo crontab -u pi -
