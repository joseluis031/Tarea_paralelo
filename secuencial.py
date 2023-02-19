import random
from time import sleep

urls = ["a.com", "b.com", "c.com", "d.com"]


def scrape(url):
    print("Empezamos", url)
    duracion = round(random.random(), 3)
    sleep(duracion)
    print("Acabado", url, "en", duracion, "segundos")
    return url, duracion

output = []
for url in urls:
    output.append(scrape(url))