#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licença: GPLv3

from bs4 import BeautifulSoup
import urllib2
# para usar expressoes regulares
import re
# para usar itens do sistema
import os
import sys
#import csv
import time

url = "https://www.receitaws.com.br/v1/cnpj/" #site de consulta a cnpjs da receita
count = 0
#if sys.argv[1] == None:
#    print 'inclua uma lista de cnpjs para serem verificados'

# abre o arquivo dos cnpjs a serem testados um a um passado como parametro
f = sys.argv[1]

for line in open(f, 'r'):
        if count >= 1:
            time.sleep(2)
            count = 0
#    if re.search(search_term, line):
	new_url = url+line # TODO melhorando essa concatenacao, vide 
#https://pt.stackoverflow.com/questions/187589/qual-%C3%A9-a-melhor-forma-de-concatenar-strings-em-python
	if line != None: # se tem boi na linha consulta
	    content = urllib2.urlopen(new_url).read()
	    soup = BeautifulSoup(content)
##	    print '---------- cnpj: ' + line
            email = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', soup.prettify())
#            fone = re.findall('([0-9]{2}\S+ +[0-9]{5}\S+.\S+[0-9]{4}\S)', soup.prettify())
            situacao = re.findall('ATIVA', soup.prettify())
#            fone = re.findall('\d{2}..\d{4}.\d{4}', soup.prettify())
            fone = re.findall('\d{2}..\d{4}.\d{3}.', soup.prettify())
#            fone = re.findall('(\+[1-9]{2}\d+)\+ \+[2-9][0-9]{3,4}\d+-\+[0-9]{4}\d', soup.prettify())
#            capital = re.findall('[0-9]\S+.\S+[0-9]', soup.prettify())
#            capital = re.match('(*)+(capital_social)+(*))', soup.prettify())
#            capital = re.findall('\d{2}..\d{5}.\d{4}', soup.prettify())
#           print '---------------- resumo ----------------'
            print soup.prettify()[200:500]
#            print (str(line).strip() + ',' + str(email) + ',' + str(situacao) + ',' + str(fone) + ',' + str(capital.group(0)))
            count = count+1
        if line == None:
            print 'no matches found'

