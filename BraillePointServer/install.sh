#!/bin/bash


apt install -y git
cd /opt/autoupdate
rm -rf /usr/bin/python
ln -s python3 /usr/bin/python
rm -rf BraillePointGateway
git clone https://github.com/gsandro/BraillePointGateway
cd BraillePointGateway
git checkout  master


cat > braille-server.service << EOF
[Unit]
Description="Service for Braille Output"
Wants=bluetooth.service
After=bluetooth.service

[Service]
Type=simple
ExecStart=/opt/autoupdate/BraillePointGateway/BraillePointServer/src/main.py > /opt/braille-server.log 2>&1
WorkingDirectory=/opt/autoupdate/BraillePointGateway/BraillePointServer/src/

[Install]
WantedBy=multi-user.target

EOF

rm -f /etc/systemd/system/breaille-server.service
systemctl reload
mv braille-server.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable braille-server
systemctl start braille-server
