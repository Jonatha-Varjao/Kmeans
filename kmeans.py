# -*- coding: utf-8 -*-
import os
import sys
import math
import timeit
from random import randint
import csv

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

"""
    Classe onde representara minhas instancias da base de dados
"""
class Dado:
        
    def __init__(self, *args, **kwargs):
        self.ID = args
        self.dados = []

    def initialize_data(self, databaseRow):
        # inicializando o novo dado da leitura da linha do csv
        # TODO: generalizar qtd_atributos para qualquer base de dados....
        _newData = Dado(str(databaseRow[0]))
        for dados in range(1,len(databaseRow)-3):
            try:
                _newData.dados.append(float(databaseRow[dados]))
            # ultimo dado é char, então a conversao pra erro 
            # solta exceção ValueError
            except ValueError:
                _newData.dados.append((databaseRow[dados]))
        return _newData
      

class Cluster:
    
    def __init__(self, centroids: int):
        self.k = centroids
        self.center = []

    def initialize_centroids(self, Instancias:[object]):
        # randomizar 1 controlado e 1 com sindrome down
        centroid1 = Instancias[randint(1,376)]
        centroid2 = Instancias[randint(377,758)]
        self.center.append(centroid1)
        self.center.append(centroid2)

    def euclidian_distace(self, instancia:object, centroid:object)-> float:
        distance = 0.0
        for i in range(len(instancia)-1):
            distance += (instancia[i] - centroid[i])**2
        return math.sqrt(distance)

    def mean_centroids(self, centroids:object):
        new_centroid = []
        atribute_sum = 0.0
        qtd_instacias = len(centroids)
        qtd_atributos = len(centroids[0])-1
        for j in range(qtd_atributos):
            for i in range(qtd_instacias):
                #somo os atributos
                atribute_sum += centroids[i][j]
            new_centroid.append( atribute_sum/qtd_instacias )
            atribute_sum = 0.0
        return new_centroid

    def treshoulding_stop(self, centroidAtual, novoCentroid):
        treshoulding = 0.0
        for i in range(len(centroidAtual)-1):
            treshoulding += abs(centroidAtual[i] - novoCentroid[i])
        treshold = treshoulding/(len(centroidAtual)-1)
        if treshoulding < 0.02:
            # print("Centroid Atual", centroidAtual)
            # print("Novo Centroid", novoCentroid)
            return True


    def run(self, Instancias: object, centroids: object):
        tempo_start = timeit.default_timer()
        new_centroid0 = []
        new_centroid1 = []
        # iteração entre as instancias da base
        while True:
            # calculo das instancias nos seus respectivos clusteres
            for actual_instance in Instancias:
                distC0 = self.euclidian_distace(actual_instance, centroids[0])
                distC1 = self.euclidian_distace(actual_instance, centroids[1])
                # atribuição das instancias em seus 
                # respectivos centroids
                if distC0 < distC1:
                    new_centroid0.append(actual_instance)
                else:
                    new_centroid1.append(actual_instance)
            # recalculo os centroids
            new_centroid0 = self.mean_centroids(new_centroid0)
            new_centroid1 = self.mean_centroids(new_centroid1)
            # atribuição das classes aos novos centroids
            new_centroid0.append('Control')
            new_centroid1.append('Ts65Dn')
            # verifico se houve convergencia
            if self.treshoulding_stop(centroids[0], new_centroid0) and self.treshoulding_stop(centroids[1], new_centroid1):
                break
                # quebro o laço do while.
                # e testo a base de testes.
            # swap entre os clusteres
            centroids.clear()
            centroids.append(new_centroid0.copy())
            centroids.append(new_centroid1.copy())
            new_centroid0.clear()
            new_centroid1.clear()
        # Testar a Base de Dados de Teste
        #print(centroids)
        tempo_stop = timeit.default_timer()
        tempo_stop = tempo_stop - tempo_start
        return self.validate(centroids, tempo_stop)

    def validate(self, centroids, tempoTreinamento):
        tempo_start = timeit.default_timer()
        Teste = csv_to_object("data/Data_Cortex_Teste.csv")
        erro = 0
        # Loop da Validacao do Teste
        for actual_instance in Teste:
            #print("Instancia Atual {} Centroid 0 {} Centroid 1 {} ".format(actual_instance, centroids[0], centroids[1]))
            distC0 = self.euclidian_distace(actual_instance, centroids[0])
            distC1 = self.euclidian_distace(actual_instance, centroids[1])
            # atribuição das instancias em seus 
            # respectivos centroids/classes
            if distC0 < distC1:
                if actual_instance[-1] != centroids[0][-1]:
                    erro += 1    
            else:
                if actual_instance[-1] != centroids[1][-1]:
                    erro += 1    
        erro = erro*100/len(Teste)
        tempo_final = timeit.default_timer()
        tempo_final = tempo_final - tempo_start
        print("Porcetagem de Acerto: {} %\nPorcetagem de Erro: {} %\nTempo de Treinamento: {} %\nTempo de Classificacao: {}".format( 100-erro, erro, tempoTreinamento, tempo_final))

"""
    Função pra salvar as instancias do csv em estruturas.
"""
def csv_to_object(databasePath):
    data = Dado()
    Instancias = []    
    with open(databasePath) as db:
        csvfile = csv.reader(db, delimiter=',')
        next(csvfile)
        for line in csvfile:
            data = data.initialize_data(line)
            Instancias.append(data.dados)
    return Instancias


if __name__ == "__main__":
    pass