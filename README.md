# Tsp

Camilo Andrés Rodríguez Garzón

This is an implementation of the TSP problem, this is solved with a couple of methods such as the nearest neighbor and the pilot method.


Requirements
------------
- [numpy](http://www.numpy.org/)
- [copy](https://docs.python.org/2/library/copy.html)
- [math](https://docs.python.org/2/library/math.html)
- [matplotlib](https://matplotlib.org/)

Install for linux
-------

```
   sudo make install
```

### Testing

The module can test for

`Tsp Pilot with:`
```
   python TspPilot.py

   python TspPilot.py pr439.tsp 2 2 10
```
and

`Tsp Nearest Neighbors with:`
```
   python Tsp.py

   python Tsp.py pr439.tsp
```

### Examples
```
python Tsp.py
```

![alt text](https://github.com/camilorodriguezga/Tsp/blob/master/image/greedy/greedy-berlin52.png)

Run
-------

You can run of basic example with:

```
   make
   
   make nearest_neighbor
   
   make pilot
```
