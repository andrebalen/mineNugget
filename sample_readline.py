#!/usr/bin/env python
# -*- coding: utf-8 -*-
arq = open('cnpjotas.txt', 'r')
texto = arq.readlines()
for linha in texto :
    print(linha)
arq.close()
