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
    return (1/n) *sum((((m*data[i][0]+b) - data[i][1])**2 for i in range(n)))


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


def dJdm(m,b, data):
    """
    Renvoie la fonction m'|--> dJ/dm' évalué en m
    """
    n = len(data)
    return -(2/n) * sum( data[i][0] * (data[i][1] - (m * data[i][0] +b)) for i in range(n))

def dJdb(m,b, data):
    """
    Renvoie la fonction b'|--> dJ/db' évalué en b
    """
    n = len(data)
    return -(2/n) * sum(data[i][1] - (m * data[i][0] +b) for i in range(n))

def GradientStep(curent_b, curent_m, data, learningRate):
    """
    Effectue une étape de la descente de gradient
    """
    b_gradient = dJdb(curent_m, curent_b, dataset)
    m_gradient = dJdm(curent_m, curent_b, dataset)
    
    new_b = curent_b - (learningRate * b_gradient)
    new_m = curent_m - (learningRate * m_gradient)
    return (new_b, new_m)

def GradientDescent(data, starting_b, starting_m, learningRate, numIterations):
    """
    Effectue la descente de gradient
    """
    b = starting_b
    m = starting_m
    for i in range(numIterations):
        b,m = GradientStep(b,m, data, learningRate)
    return (b,m)