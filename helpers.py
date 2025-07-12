import base64
import cv2
import numpy as np

def carrega(path_arquivo):
    try:
        with open(path_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro para carregar arquivo: {e}")

def salva(path_arquivo, conteudo):
    try:
        with open(path_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro para salvar arquivo: {e}")            