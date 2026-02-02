from datetime import datetime
from datetime import timedelta
from datetime import timezone

its_day = datetime.today()
print(its_day)

mydatetime = datetime.fromtimestamp(1706551390)
print(mydatetime, type(mydatetime))

ordinal_day = 365 # Порядковий номер дня
dt = datetime.fromordinal(ordinal_day)
print(dt)
day_number = datetime.today().toordinal()
print(f'Порядковий номер сьогоднішнього дня: {day_number}')

current_datetime = datetime.now()
print("Поточна дата і час:", current_datetime)

print(its_day == current_datetime)

incoming_date = "Aug 24, 1991"
dt_incoming_date = datetime.strptime(incoming_date, '%b %d, %Y')
print(dt_incoming_date)
dt_incoming_time_out = datetime.strftime(dt_incoming_date, "%H:%M:%S and %Y-%m-%d")
print(dt_incoming_time_out)


dt_01 = "19:45:23"  # Germany
dt_02 = "20:00:22"
dt_03 = "20:00:27"
dt_04 = "20:45:23"  # Kyiv

def to_hour(time_in_hour:str):
    return datetime.strptime(time_in_hour, "%H:%M:%S")

string_date_array = [dt_01, dt_02, dt_03, dt_04]

new_dt = []
for t in string_date_array:
    new_dt.append(to_hour(t))

dt_01_alex, dt_02_nata, dt_03_jena, dt_04_rost = new_dt
print(dt_01_alex, dt_02_nata, dt_03_jena)

diff_time = dt_02_nata - dt_01_alex
print("Diff", diff_time, type(diff_time))

if dt_02_nata - dt_01_alex >= timedelta(minutes=14):
    print("FAIL")
else:
    print("pass")

some_delta = timedelta(days=999999)
print(current_datetime + some_delta)
print(dt_01_alex-dt_02_nata)

d = datetime.today()
print(d)
print(d.isocalendar())
print(d.isoformat())
print(d.isoweekday())
print(d.timetuple())
print(d.weekday())
dd = d.replace(year=2023, day=12)
print(dd)

td = timedelta(days=5, hours=3, minutes=30)
print(td)
total_seconds = td.total_seconds()
print(total_seconds)
'''
1000000 == 2 week
1000000000 == 32 years
'''

big_td = timedelta(seconds=1000000000)
print(big_td)
print(11574/365)
