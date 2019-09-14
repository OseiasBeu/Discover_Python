#
# Escrevendo arquivos com funções do Python
#
class ManipulandoArquivos():
    def __init__(self):
        self.mensagemDeCriacao = "...Iniciando script..."
        self.mensagemDeTermino = "...FIM DO SCRIPT..."
    
    def EscreveArquivo(self, nomeDoArquivo, ext, mensagemDeTexto):
        self.nomeDoArquivo = nomeDoArquivo
        self.ext = ext
        self.mensagemDeTexto = mensagemDeTexto
        arquivo = open(self.nomeDoArquivo+"."+self.ext, "w+")
        arquivo.write("%s\r\n" %(self.mensagemDeTexto))
        arquivo.close()

    def AlterandoArquivo(self, nomeDoArquivo, ext, mensagemDeInclusao):
        self.nomeDoArquivo = nomeDoArquivo
        self.ext = ext
        self.mensagemDeInclusao = mensagemDeInclusao
        arquivo = open(self.nomeDoArquivo+"."+ self.ext, "a+")
        arquivo.write("%s\r\n" %(self.mensagemDeInclusao))
        arquivo.close()


def criandoArquivo(nomeArquivo, exten, msg):
    meuarquivo = ManipulandoArquivos()
    print(meuarquivo.mensagemDeCriacao)
    Escrevendo = meuarquivo.EscreveArquivo(nomeArquivo,exten, msg)
    print(meuarquivo.mensagemDeTermino)


def alteraArquivo(nomeDoArquivo, exten, msg):
    meuArquivo = ManipulandoArquivos()
    print(meuArquivo.mensagemDeCriacao)
    Alterando = meuArquivo.AlterandoArquivo(nomeDoArquivo,exten,msg)
    print(meuArquivo.mensagemDeTermino)



    
#criandoArquivo('Atos','txt','Vamos causar um alvoroço na terra!!!')

alteraArquivo('Atos','txt','Esses homens que têm causado alvoroço por todo o mundo, agora chegaram aqui[...]')