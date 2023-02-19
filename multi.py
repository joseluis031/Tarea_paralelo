from multiprocessing import Pool
from time import sleep
import random


def scrape(url):
    print("Empezamos", url)
    duracion = round(random.random(), 3)
    sleep(duracion)
    print("Acabado", url, "en", duracion, "segundos")
    return url, duracion

urls = ["a.com", "b.com", "c.com", "d.com", "e.com"]

if __name__ == "__main__":
    pool = Pool(processes=4)
    output = pool.map(scrape, urls)
    pool.close()
    
    print()
    for i in output:
        print(i)