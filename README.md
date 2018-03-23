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
   python pilot.py

   python pilot.py pr439.tsp 2 2 10
```
and

`Tsp Nearest Neighbors with:`
```
   python nearestneighbors.py

   python nearestneighbors.py pr439.tsp
```

`Tsp Random Search with:`
```
   python randomsearch.py

   python randomsearch.py pr439.tsp

   python randomsearch.py pr439.tsp 200
```

`Tsp Evolutionary Strategy (1+1) with:`
```
   python evolutionarystrategy1+1.py

   python evolutionarystrategy1+1.py pr439.tsp

   python evolutionarystrategy1+1.py pr439.tsp 200
```

`Tsp Simulated Annealing with:`
```
   python simulatedannealing.py

   python simulatedannealing.py pr439.tsp

   python simulatedannealing.py pr439.tsp 200
```

### Examples
```
python nearestneighbors.py
```

![alt text](https://github.com/camilorodriguezga/Tsp/blob/master/image/greedy/greedy-berlin52.png)

```
python pilot.py
```

![alt text](https://github.com/camilorodriguezga/Tsp/blob/master/image/semipilot/semipilot-berlin52-2-2.png)

Run
-------

You can run of basic example with:

```
   make
   
   make nearest_neighbor
   
   make pilot

   make random_search
```

References
-----------

*  Vob Stefan, Fink Andreas and Duin Cees (2005) Looking Ahead with the Pilot Method.  
