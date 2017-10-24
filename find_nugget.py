#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Licença: GPLv3

from bs4 import BeautifulSoup
import urllib2
# para usar expressoes regulares
import re
# para usar itens do sistema
import os
import sys

url = "https://www.receitaws.com.br/v1/cnpj/" #site de consulta a cnpjs da receita

# abre o arquivo dos cnpjs a serem testados um a um passado como parametro
f = sys.argv[1]

for line in open(f, 'r'):
#    if re.search(search_term, line):
	new_url = url+line # TODO melhorando essa concatenacao, vide 
#https://pt.stackoverflow.com/questions/187589/qual-%C3%A9-a-melhor-forma-de-concatenar-strings-em-python
	if line != None: # se tem boi na linha consulta
	    content = urllib2.urlopen(new_url).read()
	    soup = BeautifulSoup(content)
	    print '---------- cnpj: ' + line
            email = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', soup.prettify())
            if email != None:
	       print (email)
#           fone = re.compile('([0-9]{2} [0-9]{5}.[0-9]{4})', soup.prettify())
            fone = re.findall('(\S+[0-9]\S+)\S+ +[0-9]\S+.\S+[0-9]', soup.prettify())
            if fone != None:
	       print (fone)
            if line == None:
            	print 'no matches found'

#f.close()

print 'concluido!'
