#! /usr/bin/python
#-*- coding: utf-8 -*-
import random
import string
import time
import sys

valor=int(sys.argv[1])
qtdUser=int(sys.argv[2])

def mkpass(valor,tanto):
    """
    Autor  : Danillo Souza  <danillo.silva@bowne.com>
    Versão : 0.1
    Data   : 08/06/2010 - 23:32
    
    Descrição: gera uma senha aleatória do tamanho especificado.
    
    Modificado  : Denis Moura <denisdmm@gmail.com>
    Data        : 20/11/103 - 14:00
    Acrescentado multiplas senhas     	
    """
    size=valor
    chars = []
    chars.extend([i for i in string.ascii_letters])
    chars.extend([i for i in string.digits])
    chars.extend([i for i in '\'"!$%&*()-_=+[{}]~,<.>;:'])
    
    senhas = []
    for j in range(tanto):
	passwd = ''

	for i in range(size):
        	passwd += chars[random.randint(0,  len(chars) - 1)]
        	
	        random.seed = int(time.time())
	        random.shuffle(chars)
        
	senhas.append(passwd)
    return senhas	

print(mkpass(valor,qtdUser) )


