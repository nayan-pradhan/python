import time

print("Press 'Enter' to start\nPress 'Enter' again to lap\nPress 'Ctrl-C' to quit")
input()
print("Stopwatch Started!")
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        if lapNum == 1:
            print("Lap No:   Total Time   Lap Time\n")
        print("Lap #{}:      {}        {}".format(lapNum, totalTime, lapTime, end = ''))
        lapNum += 1
        lastTime = time.time()

except KeyboardInterrupt:
    finalTime = round(time.time() - startTime, 2)
    print("\nTotal Time Taken: {}".format(finalTime))