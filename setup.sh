#!/bin/bash

apt update
apt dist-upgrade
apt install git python-pip -y
pip install adafruit-ws2801
