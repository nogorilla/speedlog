import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import click
import sqlite3
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

conn = sqlite3.connect(os.path.join(__location__, "../data/speedlog.db"))
c = conn.cursor()

@click.command()
def graph():
    """ Print a graph of internet speeds """
    times = []
    download = []
    upload = []

    c.execute("SELECT * FROM speed")
    data = c.fetchall()

    for d in data:
        print(f"date: {d[1]}, up: {d[2]}, down: {d[3]}")
        times.append(str(d[1]))
        download.append(float(d[2]))
        upload.append(float(d[3]))

        plt.figure()
        plt.plot(times, download, label='download', color='r')
        plt.plot(times, upload, label='upload', color='b')
        plt.xlabel("date time")
        plt.ylabel("speed in Mb/s")
        plt.title("internet speed")
        plt.legend()
        plt.savefig("test_graph.jpg", bbox_inches='tight')

if __name__ == "__main__":
    graph()