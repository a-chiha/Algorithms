import random
import itertools 
import permutations

def distance_tour(aTour):
    return sum(distance_points(aTour[i-1], aTour[i]) for i in range(len(aTour)))

              
aCity=complex

def distance_points(first,seound):
    return abs(first-seound)

def generate_cities(number_of_citites):
    seed = 111
    width=500
    height=300
    random.seed(seed)
    return frozenset(aCity(random.randint(1,width),random.randint(1,height))
                     for c in range(number_of_citites))

def brute_force(cities):
    return shortest_tour(itertools.permutations(cities))

def shortest_tour(tours):
    return min(tours,key=distance_tour)

def greedy_algorithm(cities,start=None):
    city_=start or first(cities)
    tour=[city_]
    unvisited = set(cities-{city_})
    while unvisited:
        city_=nearest_neighbor(city_,unvisited)
        tour.append(city_)
        unvisited.remove(city_)
    return tour

def first(collection): return next(iter(collection))

def nearest_neighbor(city_a, citites):
    return min(citites,key=lambda city_: distance_points(city_,city_a))

import matplotlib.pyplot as plt


def visualize_tour(tour,style='bo-'):
    if len(tour) > 1000:
        plt.figure(figsize=(15,10))
        start=tour[0:1]
        visualize_segment(tour+start,style)
        visualize_segment(start,'rD')
def visualize_segment(segment,style='bo-'):
    plt.plot([X(c)for c in segment],[Y(c)for c in segment],style,clip_on=False)
    plt.axis('scaled')
    plt.axis('off')
def X(city):
    return city.real
def Y(city):
    return city.imag

from time import time
from collections import Counter

def tsp(algorithm,cities):
    t0=time()
    tour=algorithm(cities)
    t1=time()
    assert Counter(tour)==Counter(cities)
    visualize_tour(tour)
    print("{}:{} => tour length {:.0f} (in {:.3f} sec)".format(name(algorithm), len(tour), distance_tour(tour), t1-t0))


def name(algorithm):
    return algorithm.__name__.replace('_tsp','')


tsp(greedy_algorithm,generate_cities(2000))