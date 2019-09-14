#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil

class manipulaArquivos():
    def __init__(self):
        self.mensagemInicial = "--------------------------------INICIANDO SCRIPT--------------------------------"
        self.mensagemFinal = "------------------------------FINALIZANDO SCRIPT--------------------------------"
        
    def copiaArquivo(self, nomeArquivoProcurado):
        self.nomeArquivoProcurado = nomeArquivoProcurado
        
        if path.exists(self.nomeArquivoProcurado):
            print('Arquivo Encontrado!');
            pathAtual = path.realpath(self.nomeArquivoProcurado);
            novoPath  = pathAtual+'.bkp';
            shutil.copy(pathAtual,novoPath);
            shutil.copystat(pathAtual,novoPath);
        else:
            print("ERRO: Arquivo não encontrado!!!")
            
    def mudaNomeArquivo(self, nomeArquivoRenomear, novoNome):
        self.nomeArquivoRenomear = nomeArquivoRenomear
        self.novoNome = novoNome
        
        if path.exists(self.nomeArquivoRenomear):
            print('Arquivo Encontrado');
            os.rename(self.nomeArquivoRenomear, self.novoNome);
        else:
            print("ERRO: Arquivo não encontrato!!!")


def fileManipulation(nomeArquivo, novoNome):
    nomeArquivo = nomeArquivo;
    novoNome = novoNome;
    fl = manipulaArquivos();
    print(fl.mensagemInicial);
    fl.copiaArquivo(nomeArquivo);
    fl.mudaNomeArquivo(nomeArquivo, novoNome);
    print(fl.mensagemFinal);
    
    
    
    
    
fileManipulation('NovoArquivo.txt','novoArquivo2.txt.bkp')