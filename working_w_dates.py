# For interchange of data between application I would prefer to use something like ISO8601, which uses the 'Z' suffix for UTC:

import datetime
import pytz
import calendar
# naive date/time (don't have enough info about timezones or daylight savings time)
# aware
d = datetime.date(2018, 1, 21)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.weekday()) # Monday: 0 Sunday: 6
print(tday.isoweekday()) # Monday: 1 Sunday: 7
print(tday.year)

# Date +/- timeDelta = anotherDate
tdelta = datetime.timedelta(days=7)
print(tday+tdelta)
print(tday-tdelta)

# Date +/- anotherDate = timeDelta
egy = datetime.date(2018, 2, 1)
till_egyday = egy-tday
print(till_egyday.total_seconds())

############################################################

t = datetime.time(23, 11, 55, 564434)
# .....................................
############################################################

dt = datetime.datetime(2018, 2, 2, 3, 14, 55, 565333)
print(dt)
print(dt.date())
print(dt.time())

rtday = datetime.datetime.today()
print(rtday)
print(dt - rtday)

dt_today = datetime.datetime.today() # timezone is none
dt_now = datetime.datetime.now() # timezone can be set
dt_utcnow = datetime.datetime.utcnow() # gives us UTC time

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)
################################################################
# timezone aware date
dt2=datetime.datetime(2018, 2, 2, 3, 14, 55, tzinfo=pytz.UTC)
print(dt2)
dt_utc = datetime.datetime.now(tz=pytz.UTC) # timezone can be set
print(dt_utc)
# list all timezones
for tz in pytz.all_timezones:
    print(tz)
dt_qa = dt_utc.astimezone(pytz.timezone('Asia/Qatar'))
print(dt_qa)


qatar_naive = datetime.datetime.now()
qatar_tz = pytz.timezone('Asia/Qatar')

dt_qa = qatar_tz.localize(qatar_naive)
print(dt_qa)
dt_egy = dt_qa.astimezone(pytz.timezone('Egypt'))
print(dt_egy)

print(dt_qa.isoformat())
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print(dt_qa.strftime('%a, %b %d, %Y'))
print(datetime.datetime.strptime('Tue, Jan 23, 2018', '%a, %b %d, %Y'))
# arrow package for easy dealing with datetime in python

###################################################################################

balance = 5000
interest_rate = 13*.01
monthly_payment = 500

