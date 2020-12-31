from datetime import timedelta, datetime
import time

print ("----------x----------x----------x----------x----------x----------")
print ("New Year's Countdown")
print ("Press CTRL+C to exit")
print ("----------x----------x----------x----------x----------x----------")

try:
	while True:
		date_now = datetime.today()
		date_now_timestamp = int(date_now.timestamp())

		new_year_date = datetime(year=date_now.year+1, month=1, day=1, hour=0, minute=0, second=0)
		new_year_timestamp = int(new_year_date.timestamp())

		remaining_time_sec = new_year_timestamp - date_now_timestamp

		remaining_time = timedelta(seconds=remaining_time_sec)
		remaining_days = remaining_time.days 
		remaining_sec = remaining_time.seconds

		remaining_min, remaining_sec = divmod(remaining_sec, 60)
		remaining_hrs, remaining_min = divmod(remaining_min, 60)

		if remaining_days:
			if remaining_days > 1:
				remaining_days = "{} days".format(remaining_days)
			else:
				remaining_days = "{} day".format(remaining_days)
		else:
			remaining_days = ""

		if remaining_hrs:
			if remaining_hrs > 1:
				remaining_hrs = "{} hours".format(remaining_hrs)
			else:
				remaining_hrs = "{} hour".format(remaining_hrs)
		else:
			remaining_min = ""

		if remaining_min:
			if remaining_min > 1:
				remaining_min = "{} minutes".format(remaining_min)
			else:
				remaining_min = "{} minute".format(remaining_min)
		else:
			remaining_min = ""

		if remaining_sec:
			if remaining_sec > 1:
				remaining_sec = "{} seconds".format(remaining_sec)
			else:
				remaining_sec = "{} second".format(remaining_sec)
		else:
			remaining_sec = ""

		print("Time remaining: {} {} {} {}".format(remaining_days, remaining_hrs, remaining_min, remaining_sec), end="\r")

		time.sleep(1)

except KeyboardInterrupt:
	exit()
