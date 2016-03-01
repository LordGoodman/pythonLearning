# -*- coding: utf-8 -*-
from pymongo import MongoClient
from numpy import *
import json,operator

client = MongoClient()
db = client.test
    
def query2Mat():
    cursor = db.dating.find()
    returnMat = zeros((cursor.count(),3))
    classVector = []
    index = 0 
    for document in cursor:
        returnMat[index,:] =document['ffMiles'],document['percentTats'],document['iceCream']
        classVector.append(int(document['charming']))
        index += 1
    return returnMat,classVector