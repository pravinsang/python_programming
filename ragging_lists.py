# Ragging Lists
# Nested lists with inner lists of varying lengths are called ragged lists.
drinking_times_by_day = [["9:02", "10:17", "13:52", "18:23", "21:31"],
    ["8:45", "12:44", "14:52", "22:17"],
    ["8:55", "11:11", "12:34", "13:46",
    "15:52", "17:08", "21:15"],
    ["9:15", "11:44", "16:28"],
    ["10:01", "13:33", "16:45", "19:00"],
    ["9:34", "11:16", "15:52", "20:37"],
    ["9:01", "12:24", "18:51", "23:13"]]

for day in drinking_times_by_day:
    for drinking_time in day:
        print(drinking_time, end=" ")
    print()