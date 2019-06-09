#!/bin/zsh

PID=$(/usr/bin/pgrep gnome-session)
echo $PID
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)
