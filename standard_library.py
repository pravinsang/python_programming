from datetime import datetime, timedelta, timezone

print(datetime.now())
dt = datetime(2024, 8, 12, 14, 30, 0)
future_date = dt + timedelta(days= 5)
print(future_date)
utc_now = datetime.now(timezone.utc)
print(utc_now)
print(utc_now.astimezone())