default : nearest_neighbor

.PHONY : install
install :
	apt-get update
	apt-get install -y wget libpng12-dev libfreetype6-dev python-dev python-tk
	apt-get upgrade -y python-dev
	pip install NumPy setuptools pyparsing pytz cycler six backports.functools_lru_cache subprocess32
	chmod +x install_freetype.sh
	./install_freetype.sh
	pip install matplotlib
	
.PHONY : nearest_neighbor
nearest_neighbor :
	python nearestneighbors.py

.PHONY : pilot
pilot :
	python pilot.py

.PHONY : random_search
random_search :
	python randomsearch.py

.PHONY : evolutionary_strategy
evolutionary_strategy :
	python evolutionarystrategy1+1.py

.PHONY : simulated_annealing
simulated_annealing :
	python simulatedannealing.py

