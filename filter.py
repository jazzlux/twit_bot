import os
import csv

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
                    if self.search_frase in words:
                        self.lista_twit.append(i)
                    else:
                        pass
            return self.lista_twit


if __name__=='__main__':
	f = Filter('twit.csv', 'Director')
	print(f.filter_file())
