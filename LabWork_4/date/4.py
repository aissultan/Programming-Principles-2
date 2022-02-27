from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
date1 = datetime.strptime('2018-09-12 17:34:12', '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.now()
print("%d seconds" %(date_diff_in_Seconds(date2, date1)))
