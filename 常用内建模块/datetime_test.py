from datetime import datetime, timedelta

now = datetime.now()

print(now)

print(type(now))

dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)

print(dt.timestamp())

t = 1429417200.0

print(datetime.fromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

print(cday)

print(now.strftime('%a, %b %d %H:%M'))

print(now + timedelta(hours=10))