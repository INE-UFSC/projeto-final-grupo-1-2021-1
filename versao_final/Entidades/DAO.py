import pickle
from abc import ABC

class DAO(ABC):
    def __init__(self,datasource=''):
        self.__datasource = datasource
        self.__arrayCache = []
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__arrayCache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__arrayCache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, valor):
        self.__arrayCache.append(valor)
        self.__dump()
      
    def resetarCache(self, lista):
        self.__arrayCache = lista
        self.__dump
    
    def get_all(self):
        return self.__arrayCache
