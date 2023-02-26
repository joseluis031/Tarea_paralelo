from time import sleep
from multiprocessing import Process, Pool
import random
import time


def scrape(url):
    print("Empezamos", url)
    duracion = round(random.random(), 3)
    sleep(duracion)
    print("Acabado", url, "en", duracion, "segundos")
    return url, duracion

urls = ["a.com", "b.com", "c.com", "d.com"]


def time_secuencial(urls):
    tiempo_inicial = time.time()
    output = []
    for url in urls:
        output.append(scrape(url))
    Tiempo = (time.time() - tiempo_inicial, "segundos")
    print("El tiempo total en programacion secuencial es: ", Tiempo)
