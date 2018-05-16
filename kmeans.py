# -*- coding: utf-8 -*-
import os
import sys
import math
import numpy

'''
    DOCSTRING:
        Class representando o algoritmo k-means.
        TODO
            Treinamento:
                    - Inicialização dos centroids
                    - Cálculo dos novos centroids
                    - Aceitar n-dimensoes
            Interface pra receber os dados - CLI
'''


class Point:
    def __init__(self, *args, **kwargs):
        self.dimensions: int

    def distanceSquare(self):
        return

class Cluster(Point):
    def __init__(self, k, **kwargs):
        self.k: [int] = k
        self.


class Kmeans(Cluster):
    def __init__(self, base_dados, k, colunas):
        self.K: int
    
    # calcular a distância euclidiana
    def distance(self, points: [int]) -> [int]:
        pass    #return math.sqrt((point2[0]- point1[0])**2  + (point2[1]-point1[1])**2)

    # inicialização dos centroids
    def initialize_centroids(self, data: [int]) -> [int]:
        pass        
    

if __name__ == "__main__":
    pass