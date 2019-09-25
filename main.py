import subprocess
proc=subprocess.Popen('/usr/bin/pactl set-sink-volume 5 35%', shell=True, stdout=subprocess.PIPE)
amixer_stdout=proc.communicate()
"""import alsaaudio
m = alsaaudio.Mixer()   # defined alsaaudio.Mixer to change volume
m.setvolume(50) # set volume
vol = m.getvolume()
print vol"""