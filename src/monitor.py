#!/usr/bin/python3

import speedtest
import datetime
import sqlite3
import os
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# TODO make location configurable
conn = sqlite3.connect(os.path.join(__location__, "../data/speedlog.db"))
c = conn.cursor()

def record():
    """ Record upload and download speed to sqlite """
    downspeed = 0.0
    upspeed = 0.0
    try:
        s = speedtest.Speedtest()
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        print(f"time: {time}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
    except:
        pass


    try:
        sql = "INSERT INTO speed (up, down) VALUES (?, ?)"
        c.execute(sql, (upspeed, downspeed))
        conn.commit()
    except:
        pass

if __name__ == "__main__":
    while True:
        record()
        time.sleep(120) # sleep for 2 minutes TODO make this configurable
