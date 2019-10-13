from datetime import date


first_date = date(2019, 10, 14)
second_date = date(2019, 9, 14)

diff = first_date - second_date
print(diff.days)
