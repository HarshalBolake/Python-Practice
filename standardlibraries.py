import datetime

now = datetime.datetime.now()
# print(now)

today = datetime.date.today()
# print(today)

time = datetime.datetime.now().time()
# print(time)

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)



from pathlib import Path
path = Path("document")/"notes.txt"
print(path)