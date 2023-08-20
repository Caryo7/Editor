import time
import keyboard as kb

def p(*args):
    kb.press_and_release(*args)
    time.sleep(0.5)

time.sleep(3)
p('control+s')
p('\n')
p('left')
p('\n')
time.sleep(1)
p('\n')
time.sleep(1)
p('control+w')
p('right')
p('\n')
time.sleep(1)
kb.press('control')
for i in range(10):
    p('plus')
kb.release('control')
