#
# Lendo arquivos com funções do Python
#

class lerArquivo():
    def __init__(self):
        self.mensagemDeCriacao = "--------------INICIANDO SCRIPT----------------"
        self.mensagemDeFinalizacao = "-------------FIM DO SCRIPT----------------"
    
    def lerArquivo(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo;
        print("...............Iniciando leitura do arquivo.................");
        arquivo = open(self.nomeArquivo, 'r');
        if(arquivo.mode == 'r'):
            conteudo = arquivo.read();
            print(conteudo);
        else:
            print("ERRO NA LEITURA DO ARQUIVO!")
        arquivo.close();
        print("...............Fim da leitura do arquivo.................");

    def lerArquivoLinhaALinha(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo
        print("...............Iniciando leitura linha a linha.................");
        arquivo = open(self.nomeArquivo,'r');
        if(arquivo.mode == 'r'):
            conteudoArquivo = arquivo.readlines();
            for conteudo in conteudoArquivo:
                print(conteudo);
        else:
            print("ERRO NA LEITURA DO ARQUIVO!")
        arquivo.close();
        print("...............Fim da leitura do arquivo.................");
    
def leituraDeArquivo(fileName):
    lerArq = lerArquivo();
    lerArq.mensagemDeCriacao;
    lerArq.lerArquivoLinhaALinha(fileName);  
    lerArq.mensagemDeFinalizacao;


leituraDeArquivo("Atos.txt");