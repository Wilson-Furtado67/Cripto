# Este codigo visa recontruir a criptografia de Cesar
# Outras informaçoes
'''Em criptografia, a Cifra de César, também conhecida como cifra de troca, código de 
César ou troca de César, é uma das mais simples e conhecidas técnicas de criptografia. 
É um tipo de cifra de substituição na qual cada letra do texto é substituída por outra, que se 
apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, 
A seria substituído por D, B se tornaria E, e assim por diante. O nome do método é em homenagem a Júlio César,
que o usou para se comunicar com os seus generais.O processo de criptografia de uma cifra de César é frequentemente
incorporado como parte de esquemas mais complexos, como a cifra de Vigenère, e continua tendo aplicações modernas,
como no sistema ROT13. Como todas as cifras de substituição monoalfabéticas, a cifra de César é facilmente decifrada
e na prática não oferece essencialmente nenhuma segurança na comunicação.'''

def Tabu(lista):
    tab = []
    limite = len(lista)
    temp = lista
    for n in range(0,limite + 1):
        if n == 0:
            y = 1
        else:
            y = n
        tab.append(temp)
        temp = lista[-y:] + lista[:-y:]
    ord(tab)
    print(tab)
    pass

class Cesar:
    def __init__(self,lista_de_caracter = ''):
        if lista_de_caracter  == '':
            self.caracter = 'ABCDEFGHIJKLMNOPQRTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz '
        else:
            self.caracter = lista_de_caracter
        
    #def __str__(self): 
    #    forma = '{}'.format(self.mensagem)
    #    return forma
    
    def cifrar(self,salto,texto):    
        tamanho = len(texto)
        cifra = ''
        for index in range(tamanho):
            iPos = self.caracter.find(texto[index])
            fPos = salto + iPos
            run = True
            while run:
                if fPos >= len(self.caracter):
                    fPos = fPos - len(self.caracter) - 1
                else:
                    run =  False
            cifra += self.caracter[fPos]
        return cifra
        
    def cifrar_arquivo(self,passo,caminho_arquivo):
        with open(caminho_arquivo,'r') as arquivo, open('arquivo_cifrado.txt','a') as cifra:
            for linha in arquivo:
                var = self.cifrar(passo,linha)
                cifra.write(var)
                   
    def desCifrar(self,salto,texto):
        self.cifrar(-salto,texto)
        
class Vigenere:
    def __init__(self,mensagem,Password):
        self.mensagem = mensagem
        self.Password = Password
        Tabua = ''
    def cifrar_mensagem(self):
        pass

if __name__ == "__main__":
    teste = Cesar()
    teste.cifrar_arquivo(3,'./texo.txt')
    pass
