#!/usr/bin/env python
import math
import os

FILE = 'Syncing_Feeling.avi'
TIME = 3*60 + 10
DURATION = 4

for i in range(0, int(math.ceil(TIME / DURATION))):
  start = i * DURATION
  end = start + DURATION
  start_fmt = '00:{:02}:{:02}'.format(int(start / 60), start % 60)
  out_file = start_fmt.replace(':','-')

  os.system('ffmpeg -i {} -ss {} -t 4 {}.mp3'.format(FILE, start_fmt, out_file))
  os.system('ffmpeg -i {} -ss {} -t 4 {}.avi'.format(FILE, start_fmt, out_file))
  os.system('ffmpeg -i {} -ss {} -f image2 -vframes 1 {}.png'.format(FILE, start_fmt, out_file))
