#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def CriaZipModo1():
    shutil.make_archive('ArquivoCompactado','zip','/home/oseiasbeu/Documents/cursoDepythonLInkedin/arquivos_de_exercicios_descubra_o_python/Cap. 03');

# CriaZipModo1();

def CriaZipModo2():
    with ZipFile('ArquivoZipModo2','w') as novoZip:
        novoZip.write('NovoArquivoAlterado.txt');
        novoZip.write('NovoArquivo.txt');
        # novoZip.write('zipModo1.zip.zip');

# CriaZipModo2();

def RemoverArquivo():
    os.remove('ArquivoZipModo2');

RemoverArquivo();

