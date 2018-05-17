# -*- coding: utf-8 -*-
import os
from kmeans import Cluster, Dado, csv_to_object



if __name__ == "__main__":
    Instancias = csv_to_object("data/Data_Cortex_Treinamento.csv")
    # inicializando os clusteres
    # classificacao binária
    clusters = Cluster(2)
    clusters.initialize_centroids(Instancias)
    # loop do k-means
    clusters.run(Instancias, clusters.center)
    

