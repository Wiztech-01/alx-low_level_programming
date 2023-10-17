#!/bin/bash
wget -P /tmp https://github.com/Wiztech-01/alx-low_level_programming/raw/master/0x18-dynamic_libraries/inject_code.so
export LD_PRELOAD=/tmp/libmask.so
