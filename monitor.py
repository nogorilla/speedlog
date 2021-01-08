import speedtest
import datetime
import csv

s = speedtest.Speedtest()

with open('test.csv', mode='w', newline='') as speedcsv:
    w = csv.DictWriter(speedcsv,
                       fieldnames=['time','downspeed','upspeed'])
    w.writeheader()

    while True:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        w.writerow({
            'time': time,
            'downspeed': downspeed,
            'upspeed': upspeed
        })
        print(f"time: {time}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
