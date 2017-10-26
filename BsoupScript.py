#coding=utf-8


import requests
from bs4 import BeautifulSoup
import unicodedata
import pandas as pd
import time


class Cao(object):




    def __init__(self):

        strnome = "NaN"
        stridade = "NaN"
        strsexo = "NaN"
        strraca = "NaN"
        strpelo = "NaN"
        strporte = "NaN"
        strdataent = "NaN"
        strdataob = "NaN"
        strdataadopcao = "NaN"
        strapadrinhavel = "NaN"
        strparadop = "NaN"
        strtempocat = "NaN"

        f = open('testfile.txt', 'r')
        line = f.readline()


        while line:
            line = f.readline()
            if 'Nome' in line:
                self.nome = line
                strnome = self.nome.replace("Nome:", "\n")


            if 'Idade' in line:
                self.idade = line
                stridade = self.idade.replace("Idade:", "")

            if 'Sexo' in line:
                self.sexo = line
                strsexo = self.sexo.replace("Sexo:", "")

            if 'Raca' in line:
                self.raca = line
                strraca = self.raca.replace("Raca:", "")

            if 'Pelo' in line:
                self.pelo = line
                strpelo = self.pelo.replace("Pelo:", "")

            if 'Porte' in line:
                self.porte = line
                strporte = self.porte.replace("Porte:", "")

            if 'Data de Entrada na Instituicao' in line:
                self.dataent = line
                strdataent = self.dataent.replace("Data de Entrada na Instituicao:", "")

            if 'Data de Obito' in line:
                self.dataob = line
                strdataob = self.dataob.replace("Data de Obito:", "")

            if 'Data de Adopcao' in line:
                self.dataadopc = line
                strdataadopcao = self.dataadopc.replace("Data de Adopcao:", "")

            if 'Apadrinhavel' in line:
                self.apad = line
                strapadrinhavel = self.apad.replace("Apadrinhavel?", "")

            if 'Para Adopcao?' in line:
                self.paraadop = line
                strparadop = self.paraadop.replace("Para Adopcao?", "")

            if 'Tempo Aproximado' in line:
                self.tempcat = line
                strtempocat = self.tempcat.replace("Tempo Aproximado em Cativeiro:", "")


        file = open("testfile1.txt", "a")

        file.write(strnome.rstrip() + "\t")

        file.write(stridade.rstrip() + "\t")

        file.write(strsexo.rstrip() + "\t")

        file.write(strraca.rstrip() + "\t")

        file.write(strpelo.rstrip() + "\t")

        file.write(strporte.rstrip() + "\t")

        file.write(strdataent.rstrip() + "\t")

        file.write(strdataob.rstrip() + "\t")

        file.write(strdataadopcao.rstrip() + "\t")

        file.write(strapadrinhavel.rstrip() + "\t")

        file.write(strparadop.rstrip() + "\t")

        file.write(strtempocat.rstrip() + "\t")



for _ in range (7000,12050):
    str1 = str(_)
    time.sleep(5)
    page = requests.get("http://www.portugalzoofilo.net/caes/cao.jsp?animal_id=" + str1, allow_redirects=False)
    soup = BeautifulSoup(page.content, 'html.parser')

    print page

    mydivs = soup.findAll("div", class_="dados")
    for element in mydivs:
        c = element.get_text()
        normal = unicodedata.normalize('NFKD', c).encode('ASCII', 'ignore')


        f = open('testfile.txt', 'w')
        f.write(normal.encode('utf8'))
        f.close()

    Cao()