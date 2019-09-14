#
# Arquivo com exemplos de como trabalhar com paths
#

from os  import path
import time

def DadosArquivo():
    ArquivoExiste = path.exists('NovoArquivo.txt');
    EDiretorio    = path.isdir('NovoArquivo.txt');
    EArquivo      = path.isfile('NovoArquivo.txt');
    pathArquivo   = path.realpath('NovoArquivo.txt');
    pathRelativo  = path.relpath('NovoArquivo.txt');
    dataCriacao   = time.ctime(path.getctime('NovoArquivo.txt'));
    datamodificacao = time.ctime(path.getmtime('NovoArquivo.txt'));

    print(ArquivoExiste);
    print(EDiretorio);
    print(EArquivo);
    print(pathArquivo);
    print(pathRelativo);
    print(dataCriacao);
    print(datamodificacao);


DadosArquivo();
