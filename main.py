import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(1999, 6, 27)

days_away = today - next_birthday

print(days_away)

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"My next birthday is {days_away} days away!")

import matplotlib.pyplot

