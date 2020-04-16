# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:11:22 2020

@author: Nandy
"""
import numpy as np

def ErrorModel(m,b,data):
    """
    f:x|--> mx+b
    data = {(x,y)}
    """
    n = len(data)
    return (1/n) *sum(((m*data[i][0]+b) - data[i][1] for i in range(n))^2)


def getData():
    """
    Fonction permettant de récupérer les données provenant du fichier csv
    """
    data = []
    #On récupère les données dans le fichier
    with open('IA_tp6_data.csv') as f:
        for row in f:
            row = row.replace("\n","") #on enlève les sauts de ligne
            row = row.split(',') #On sépare les valeurs
            row = [float(item) for item in row] #On converti les valeurs en flotant (car elles sont au départ ou forme de chaine de carractères)
            data.append(row)
    return data

#Définition du dataset
dataset = getData()

def BruteForce(data):
    meilleur_parametrage = (-50, -10)
    meilleure_erreur = ErrorModel(-50,-10,data)
    for m in np.linspace(-50, 50, (10**2)+1):
        for b in np.linspace(-10, 10, (10**2)+1):
            if(ErrorModel(m,b,data) < meilleure_erreur):
                meilleur_parametrage = (m, b)
                meilleure_erreur = ErrorModel(m,b,data)
    return meilleur_parametrage
