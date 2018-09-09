import time
now = time.time()
print(round(now,2))

print('Start...')
input()
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time() -startTime,2)
        print('Lap #%s: %s (%s)' % (lapNum,totalTime,lapTime),end='')
        lapNum += 1
        lapTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')