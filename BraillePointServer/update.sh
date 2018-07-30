#!/bin/bash

systemctl stop braille-server
cd /opt/autoupdate/BraillePointGateway
git pull
git checkout master

systemctl start braille-server


