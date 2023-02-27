# Tarea_paralelo

El link de este repositorio es el siguiente:[GitHub](https://github.com/joseluis031/Tarea_paralelo.git)

## Codigo en secuencial

```
import random
from time import sleep

urls = ["a.com", "b.com", "c.com", "d.com"]


def scrape(url): 
    print("Empezamos", url)
    duracion = round(random.random(), 3)
    sleep(duracion)
    print("Acabado", url, "en", duracion, "segundos")
    return url, duracion

output = [] #se agrega el resultado a una lista vacia
for url in urls:
    output.append(scrape(url))
```

En este codigo podemos ver que cada solicitud se espera hasta que se acabe
para dar paso a la siguiente solicitud.
Es un codigo mas simple.

## Codigo en multiproceso

```
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
```

En este codigo podemos ver como se crea un grupo de procesos (Pool) con 4 procesos 
y con la funcion map se puede ejecutar la funcion scrape a cada url de la lista de urls.
Este codigo puede llegar a ser mas optimo que el codigo en secuencial

## Codigo en paralelo 

```
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
```

Si se necesita rapidez y tenemos una gran lista de elementos, el codigo en paralelo
puede llegar a ser el mas optimo. Por el contrario, el codigo en secuencial puede 
llegar a ser mas util ya que es mas facil.

En este ejercicio podemos ver que a la hora de la ejecucion en paralelo, siempre tarda 
menos en ejecutarse el codigo en multiproceso, como podemos ver a continuacion
### Ejecucion del codigo en paralelo

```
Empezamos a.com
Empezamos a.com
Empezamos b.com
Empezamos c.com
Empezamos d.com
Acabado a.com en 0.053 segundos
Acabado a.com en 0.59 segundos
Empezamos b.com
Acabado c.com en 0.39 segundos
Acabado b.com en 0.432 segundos
Acabado d.com en 0.606 segundos
El tiempo total en programacion multiprocesamiento son 0.8823111057281494 segundos
Acabado b.com en 0.932 segundos
Empezamos c.com
Acabado c.com en 0.161 segundos
Empezamos d.com
Acabado d.com en 0.759 segundos
El tiempo total en programacion secuencial son 2.485687732696533 segundos
```
