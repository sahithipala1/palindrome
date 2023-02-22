import datetime

today = datetime.date.today()

holiday = datetime.date(year=2023, month=10, day=23)

if holiday > today:
    print("Coming soon 🤣")
elif holiday < today:
    print("Hope you enjoyed it")
else:
    print("Yeah, its holiday time 🥰")

