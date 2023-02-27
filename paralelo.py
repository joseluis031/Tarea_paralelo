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
    Tiempo_secuencial = ("son {} segundos".format(time.time() - tiempo_inicial))
    print("El tiempo total en programacion secuencial", Tiempo_secuencial)


def time_multiprocesamiento(urls):
    tiempo_inicial = time.time()
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()
    Tiempo_multi = ("son {} segundos".format(time.time() - tiempo_inicial))
    print("El tiempo total en programacion multiprocesamiento",Tiempo_multi)



# ejecuto en paralelo ambos programas
if __name__ == '__main__':
    p1 = Process(target=time_secuencial, args=(urls,))
    p2 = Process(target=time_multiprocesamiento, args=(urls,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    