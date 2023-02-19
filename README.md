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
y con la funcion map se puede ejecutar la funcion scrape a cada url de la lista de urls
Este codigo puede llegar a ser mas optimo que el codigo en secuencial
