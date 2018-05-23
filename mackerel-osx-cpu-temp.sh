#!/bin/bash

name="osx.temperature.cpu"
count=`/usr/local/bin/osx-cpu-temp | sed -e "s/°C//"`
monitor_time=`date +%s`
echo -e "${name}\t${count}\t${monitor_time}\n"
