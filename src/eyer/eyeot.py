#! /usr/bin/python

# /etc/init.d/lircd stop
# mode2 -d /dev/lirc0
# /etc/init.d/lircd start
# apt-get install lirc liblircclient-dev
# http://www.stavros.io/posts/how-turn-your-raspberry-pi-infrared-remote-control/
# http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/
# mode2 -u /dev/lirc0
# irrecord -d /dev/lirc0 ./lircd.conf
# irrecord --list-namespace
# Follow the instructions and use the remote controller of the projector
# CHANGE NAME OF config to "projector"
#/etc/init.d/lirc start
#irsend SEND_ONCE project KEY_POWER
#irsend SEND_ONCE project KEY_VOLUMEUP
# To create raw codes (when the irrecord cant identify the raw, use the -m flag)
# mode2 -md /dev/lirc0 > raw_codes.raw
# send power button of air condition
# save the data, remove the first spaces (a long number) which is irrelevant
"""
root@raspberrypi:/home/tal# cat /etc/modules        
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.
# Parameters can be specified after the module name.

snd-bcm2835
lirc_dev
lirc_rpi gpio_in_pin=23 gpio_out_pin=22
"""

"""
root@raspberrypi:/home/tal# cat /etc/lirc/hardware.conf 
# /etc/lirc/hardware.conf
#
# Arguments which will be used when launching lircd
LIRCD_ARGS="--uinput"

#Don't start lircmd even if there seems to be a good config file
#START_LIRCMD=false

#Don't start irexec, even if a good config file seems to exist.
#START_IREXEC=false

#Try to load appropriate kernel modules
LOAD_MODULES=true

# Run "lircd --driver=help" for a list of supported drivers.
DRIVER="default"
# usually /dev/lirc0 is the correct setting for systems using udev 
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"

# Default configuration files for your hardware if any
LIRCD_CONF=""
LIRCMD_CONF=""
root@raspberrypi:/home/tal# 

"""

""" CONFIG FOR THE PROJECTOR

begin remote

  name  projector
  bits           16
  flags SPACE_ENC|CONST_LENGTH
  eps            30
  aeps          100

  header       9068  4450
  one           617  1641
  zero          617   508
  ptrail        612
  repeat       9063  2206
  pre_data_bits   16
  pre_data       0xE172
  gap          108122
  toggle_bit_mask 0x0

      begin codes
          KEY_POWER                0xE817
          KEY_VOLUMEUP             0x10EF
          KEY_VOLUMEDOWN           0x20DF
      end codes

end remote

"""

""" AIR CONDITION SAMPLE
begin remote

   name   acond
   flags RAW_CODES
   eps            30
   aeps          100

   ptrail          0
   repeat     0     0
   gap          40991

       begin raw_codes

           name power
     3025     3998      952      976     1924      987
      980      969      957      990      975      975
      964     1021      940      971      959      988
      960     1013      933      990      957      993
      981      964      983     1939     1910     1041
      954      976      954     1012      931     1018
      928      987      986      965      958      989
      934     1049      931     1014      984      936
      933     1043      901     1050      935     1043
      947      939      932     1044      977      941
      957     1971     1933     1014     2933     3980
      975      964     1933      998      976      968
      957      994      963     1011      935     1017
      897     1021      962     1012      958      959
      966     1021      896     1016      965     1016
      930     1988     1913     1012      899     1022
      961     1010      937     1013      903     1013
      966     1019      896     1014      930     1021
      930     1014      934     1017      931     1017
      964     1018      899     1015      968     1011
      936     1009      926      995      937     1979
     1964      964     2991     3947      934     1014
     1935      988      982      968      969     1008
      930     1014      904     1017      928     1027
      964     1008      925      993      965     1011
      924      994      958      991      928     1995
     1979      972      962      962      962     1006
      933      989      958      997      959     1021
      933     1002      904     1025      962     1011
      936     1010      931      989      962     1014
      929      992      967     1010      933     1016
      936     1015      922     1963     1941     1013
     3918
end raw_codes
end remote

"""

import os
import lirc

