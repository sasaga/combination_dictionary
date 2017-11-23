#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor samir sanchez garnica @sasaga92
import argparse
import socket
import sys
import platform
import os.path
from time import time



def script_colors(color_type, text):
    color_end = '\033[0m'

    if color_type.lower() == "r" or color_type.lower() == "red":
        red = '\033[91m'
        text = red + text + color_end
    elif color_type.lower() == "lgray":
        gray = '\033[2m'
        text = gray + text + color_end
    elif color_type.lower() == "gray":
        gray = '\033[90m'
        text = gray + text + color_end
    elif color_type.lower() == "strike":
        strike = '\033[9m'
        text = strike + text + color_end
    elif color_type.lower() == "underline":
        underline = '\033[4m'
        text = underline + text + color_end
    elif color_type.lower() == "b" or color_type.lower() == "blue":
        blue = '\033[94m'
        text = blue + text + color_end
    elif color_type.lower() == "g" or color_type.lower() == "green":
        green = '\033[92m'
        text = green + text + color_end
    elif color_type.lower() == "y" or color_type.lower() == "yellow":
        yellow = '\033[93m'
        text = yellow + text + color_end
    elif color_type.lower() == "c" or color_type.lower() == "cyan":
        cyan = '\033[96m'
        text = cyan + text + color_end
    elif color_type.lower() == "cf" or color_type.lower() == "cafe":
        cafe = '\033[52m'
        text = cafe + text + color_end
    else:
        return text
    return  text

def banner_welcome():
    banner = '''

	██████╗ ██╗ ██████╗ ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗███╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
	██╔══██╗██║██╔════╝██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
	██║  ██║██║██║     ██║     ██║   ██║██╔████╔██║██████╔╝██║██╔██╗ ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║
	██║  ██║██║██║     ██║     ██║   ██║██║╚██╔╝██║██╔══██╗██║██║╚██╗██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
	██████╔╝██║╚██████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██║██║ ╚████║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
	╚═════╝ ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
					                                                               version: 1.0
					                                               Autor: Samir Sanchez Garnica
					                                                                  @sasaga92
                                                                     
    '''
    return script_colors('lgray',banner)

def combination_dicci(diccionario_1, diccionario_2, separador, domain, name_salida):
	name = []
	archivo_name = open(diccionario_1, "r")
	for linea_name in archivo_name.readlines():
		name.append(linea_name.rstrip('\n'))
		archivo_name.close() 

	apellido = []
	archivo_apellido = open(diccionario_2, "r")
	for linea_ape in archivo_apellido.readlines():
		apellido.append(linea_ape.rstrip('\n'))
		archivo_apellido.close() 


	name_arch_salida = open (name_salida,'w')
	for indice_name in range(len(name)):
		for indice_ape in range(len(apellido)):
			name_arch_salida.write(name[indice_name]+separador+apellido[indice_ape]+domain+'\n')
	name_arch_salida.close()

	if os.path.isfile(name_salida):
		return True
	else:
		return False
	tiempo_final = time()

def main():
    print banner_welcome()
    parser = argparse.ArgumentParser()
    parser.add_argument("--dic1", dest="dict1", help="introducir el primer diccionario de palabras", required=True)
    parser.add_argument("--dic2", dest="dict2", help="introducir el segundo diccionario de palabras", required=True)
    parser.add_argument("--sep", dest="sep", help="Introducir un separador de linea entre ambas frases", required=True)
    parser.add_argument("--domain", dest="domain", help="introducir el dominio para el generador de correos", required=True)
    parser.add_argument("--output", dest="output", help="nombre del archivo de salida con los nuevos datos", required=True)
    args = parser.parse_args()


    if args.dict1 and args.dict2 and  args.sep and args.domain  and args.output:
    	if combination_dicci(args.dict1, args.dict2, args.sep, args.domain, args.output):
    		print script_colors("lgray","diccionario "+script_colors("blue",args.output)+" generado correctamente: ")
    	else:
    		print script_colors("red","El diciconario "+script_colors("blue",args.output)+" generado correctamente: ")

    else:
        print script_colors("yellow","[-] ") + script_colors("c", "Requiere parametros obligatorios ")
        exit(0)

if __name__ == '__main__':
    main()  
