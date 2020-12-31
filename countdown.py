import datetime
import time

loop_bool = True
while loop_bool:
	current_time = time.strftime("%H:%M:%S", time.localtime())
	if (current_time == "19:27:30"):
		print("TRUE")
		loop_bool = False
	else:
		print("FALSE")
	print(current_time)
