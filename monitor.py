import speedtest
import datetime
import sqlite3
conn = sqlite3.connect('speedlog.db')
c = conn.cursor()

s = speedtest.Speedtest()
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
downspeed = round((round(s.download()) / 1048576), 2)
upspeed = round((round(s.upload()) / 1048576), 2)
sql = "INSERT INTO speed (up, down) VALUES (?, ?)"
c.execute(sql, (upspeed, downspeed))
conn.commit()
print(f"time: {time}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")

