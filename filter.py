import os
import csv
import re

class Filter():
    def __init__(self, file, frase):
        self.file = file
        self.search_frase = frase
        self.lista_twit=[]

    def filter_file(self):
#        self.lista_twit=[]
        with open(self.file, mode='r') as csvfile:
            self.reader = csv.reader(csvfile)
            for i in self.reader:
                for words in i:
                    x = re.search(self.search_frase, i[0], re.IGNORECASE)
                    if x is not None :
                        self.lista_twit.append(i)
                
            return self.lista_twit


if __name__=='__main__':
	f = Filter('twit.csv', 'test_frase')
	print(f.filter_file())
