#/usr/bin/env python

import pibrella, signal, time, os

first_long_press = False

def button_changed(pin):
  global time_start
  global first_long_press
  if pibrella.button.is_pressed():
    time_start = time.time()
  else:
    pibrella.lights.off()
    now = time.time() - time_start
    if now > 3:
      if first_long_press:
        print "Preparing to shut down!"
        pibrella.light.fade(100, 0, 2)
        time.sleep(3)
        print "Now really shutting down..."
        os.system("sudo shutdown -h now")
      else:
        print "First long press"
        first_long_press = True
        pibrella.lights.pulse()
    else:
      print "Nothing going on, move along"
      first_long_press = False

pibrella.button.changed(button_changed,100)

signal.pause()

