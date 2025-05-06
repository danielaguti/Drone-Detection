#!/bin/bash
ssh pi@192.168.1.181 "echo '🚨 Drone detected at $(date)' >> /home/pi/drone_alert_log.txt"
