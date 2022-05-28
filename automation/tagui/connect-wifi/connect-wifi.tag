timeout 2
keyboard [win]d
if exist('no-internet.png')
 hover no-internet.png
 hover no-internet.png
 click no-internet.png
 if exist('wifi-off.png')
  keyboard [enter]
 wait 2
 keyboard [tab][enter]
 hover wifi.png
 keyboard [enter][tab][enter]
 // make sure you could connect the first wifi
 if exist('wifi-cancel.png')
  hover wifi-cancel.png
  // if the connecting process is too long tagui may capture the button cancel
  // this prevents timeout
  wait 10
 hover wifi-disconnect.png
 echo success