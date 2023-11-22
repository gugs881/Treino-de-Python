
"""
Created on Sat Nov 13 22:15:15 2021

@author: Gustavo

numero=int(input("Digite um valor:"))
if numero >= 100:
    print("Valor maior ou igual a cem")
else:
    print("Valor menor que cem")    

""
nota1=float(input("Digite a primeira nota:"))
nota2=float(input("Digite a segunda nota:"))
media=(nota1+nota2)/2
print('Media = ',media)
if media >=5:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")    
    ""
valor=int(input("Digite um valor:"))
resto= valor % 2
if resto==0:
    print("Número par")
else:
    print("Número ímpar")
      ""
altura=float(input("Digite uma Altura:"))
genero=int(input("[1]-para masculino\n[2]-para feminino\n Opção:"))
if genero==1:
    print("peso ideal", (72.7 * altura)-58)
else:
    print("peso não ideal")
if genero==2:
    print("peso ideal",(62.1* altura)-44.7)
else:
    print("peso não ideal")
      ""
senha=int(input("Digite uma senha:"))
if senha==123:
    print("Acesso liberado")
else:
    print("Acesso negado")    
    ""
numero=float(input("Digite um número:"))
if numero<0:
    print("número negativo")    
elif numero==0:
    print("numero nulo")
else:
    print("número positivo")    
""
a=float(input("Digite um número:"))
b=float(input("Digite um número:"))   
if a>b:
    print("O primeiro valor é maior")    
elif a==b:
    print("Os valores são iguais")    
else:
    print("O segundo valor é maior")    
    ""
compra=float(input("Digite o valor da compra:"))
venda=float(input("Digite o valor da venda:"))  
if compra>venda:
    print("Prejuízo")  
elif venda>compra:
    print("Lucro")  
else:
    print("Os valores são iguais")
    ""
    #exemplo de While
soma=0
ct=0
print("Digite[-1] para sair")
while True:
    nota=float(input("Nota do aluno:"))
    if nota==-1:
        break
    ct=ct+1
    soma=soma+nota
media=soma/ct
print("Media da turma:", media)
print("Quantidade de alunos:", ct)
""
soma=0
ct=0
print("Digite[0] para sair")
while True:
    valor=float(input("Digite um valor:"))
    if valor==0:
        break 
    resto= valor % 2
    if resto==0:
        soma=soma+valor
        ct=ct+1
media=soma/ct
print("A media dos numeros pares é:",media)
    ""

ct_impar=0
ct_par=0
soma_par=0
soma_impar=0

print("Digite[-1] para sair")
while True:
    valor=float(input("Digite um valor:"))
    if valor==-1:
        break
    if valor%2==0:
        soma_par=soma_par+valor
        ct_par=ct_par+1
    else:
        soma_impar=soma_par+valor
        ct_impar=ct_impar+1
if ct_par!=0:
    media_par=soma_par/ct_par
    print("Media dos pares:%.2f"%media_par)
else:
    print("Nao tem numero par")
if ct_impar!=0:
    media_impar=soma_impar/ct_impar
    print("Media dos impares:%.2f"%media_impar)
else:
    print("Nao tem numero impar")        
    ""


menor_valor=9999999999999
print("Digite[0] para sair")
while True:
    valor=int(input("Digite um valor:"))
    if valor==0:
        break
    if valor<menor_valor:
        menor_valor=valor
        print("O menor  valor é:", menor_valor)
    ""

maior_valor=0
menor_valor=9999999999999
print("Digite[-1] para sair")
while True:
    valor=int(input("Digite um valor:"))
    if valor==-1:
        break
    if valor<menor_valor:
        menor_valor=valor
        print("O menor  valor é:", menor_valor)   
    if valor>maior_valor:
       maior_valor=valor 
       print("Maior valor é:", maior_valor)
       ""

ct_masc=0
ct_fem=0
maior=0
menor=999999999
while True:
    altura=float(input("Digite uma altura:"))     
    if altura==0:
        break
    genero = input("Digite[m] para masculino, [f] para feminino:")
    if genero=="m":
        ct_masc=ct_masc+1
    else:
        ct_fem=ct_fem+1
    if altura<menor:
        menor=altura
    if maior<altura:
        maior=altura
print("Maior altura é:", maior)
print("Menor altura é:", menor)    
print("Número de homens", ct_masc)    
print("Número de mulheres", ct_fem)    
    ""
ct_candidato1=0
ct_candidato2=0
ct_candidato3=0
ct_nulo=0
ct_branco=0
while True:
    voto=int(input("Vote [1] para candidato1, [2] para candidato2, [3] para candidato3, [5] para nulo, [6] para voto em branco: "))
    if voto==-1:
        break
    if voto==1:
        ct_candidato1=ct_candidato1+1
    if voto==2:
        ct_candidato2=ct_candidato2+1
    if voto==3:
        ct_candidato3=ct_candidato3+1
    if voto==5:
        ct_nulo=ct_nulo+1
    if voto==6:
        ct_branco=ct_branco+1    
pct_total=ct_candidato1+ct_candidato2+ct_candidato3+ct_nulo+ct_branco
print("O total de votos do candidato 1 foi:", ct_candidato1)
print("O total de votos do candidato 2 foi:", ct_candidato2)        
print("O total de votos do candidato 3 foi:", ct_candidato3)    
print("O total de votos nulos foi:", ct_nulo)    
print("O total de votos em branco foi:", ct_branco)
pct_nulo=ct_nulo/pct_total*100
pct_branco=ct_branco/pct_total*100
print("Percentual de votos nulo é de:", pct_nulo)   
print("Percentual de votos em branco é de:", pct_branco)    
    ""
ct_menos5=0
ct_5a10=0
ct_mais10=0
total=0
salario_minimo=float(input("Digite um salario minimo:"))
print("Digite[0] para sair")
while True:
    salario=float(input("Digite um salario do funcionario:"))
    if salario==0:
        break    
    salario=float(input("Digite um salario do funcionario:"))
    if salario<5*salario_minimo:
        ct_menos5+=1
    
    if salario>=5*salario_minimo and salario<10*salario_minimo:
        ct_5a10+=1
    else:
        ct_mais10+=1   
    total=total+salario
print("O total é de:", total)
print("A quantidade de salarios entre 5 a 10 é de:", ct_5a10)        
print("A quantidade de salarios maior que 10 é de:", ct_mais10)     
print("A quantidade de salarios menor que 5 é de:",ct_menos5)       
""
maior_cnpj=0
maior_qde=0
print("Digite -1 para sair")
while True:
    cnpj=int(input("CNPJ:"))
    if cnpj==-1:
        break
    qtd=int(input("Quantidade de funcionários:"))
    if qtd>maior_qde:
        maior_qde=qtd
        maior_cnpj=cnpj
print("Maior CNPJ é:", maior_cnpj)
print("Maior quantidade é:", maior_qde)
""
valor_inicial=int(input("Digite o valor inicial:"))
valor_final=int(input("Digite o valor final:"))
if valor_inicial<=valor_final:
    for c in range(valor_inicial,valor_final+1,1):
        print(c)
else:
    for c in range(valor_inicial, valor_final-1, -1):
        print(c)
        ""

soma=0
ct=0
for c in range(1,5+1):
    nota=float(input("Nota do aluno:"))
    soma=soma+nota
    ct=ct+1
media=soma/ct
print("A media da turma é:%.2f" %media)
""
print("Farenheit|Celsius")
for farenheit in range(50,80+1,1):
    celsius=5/9*(farenheit-32)
print(farenheit,'      |',celsius)
print("{:2.1f}-{:8s}|{:2.3f}-{:3s}" .format(farenheit,"F", celsius,"C"))
""
for c in range(0,10+1):
    calculo=c*5
    print(c,"x5=" ,calculo)
""
#for aninhado
for c in range(1,6+1):    
   for i in range(1,6+1):     
    print(i,"+",c)
  ""
for c in range(0,1+1,1):
        for i in range(0,1+1,1):
            for b in range(0,1+1,1):
                print(c,i,b)
""
for c in range(00,7+1,1):
    for b in range(00,7+1,1):
        print(c,b)
""
l_voto= list()
print("Digite [1] para votar no candidato 1.")
print("Digite [2] para votar no candidato 2.")
print("Digite [3] para votar no candidato 3.")
print("Digite [5] para votar nulo")
print("Digite [6] para votar em branco")      
print("Digite [-1] para sair")
while True:
    voto=int(input("Escolha seu voto:"))
    if voto==-1:
        break
    l_voto.append(voto)
if len(l_voto)>0:
    print("O candidato votado foi o 1",l_voto.count(1))
    print("O candidato votado foi o 2",l_voto.count(2))
    print("O candidato votado foi o 3",l_voto.count(3))
    print("Seu voto foi nulo",l_voto.count(5))
    print("Seu voto foi em branco",l_voto.count(6))
    print("Percentual de votos nulos",l_voto.count(5)/len(l_voto)*100)
    print("Percentual de votos em branco",l_voto.count(6)/len(l_voto)*100)
""
l_nota=list()
print("Digite -1 para sair")
while True:
    nota=int(input("Digite uma nota:"))
    if nota==-1:
        break
    l_nota.append(nota)
maior_nota=max(l_nota)
menor_nota=min(l_nota)
print("Maior nota:",maior_nota)
print("Menor nota:", menor_nota)
print(f"Frequência maior nota:{l_nota.count(maior_nota)}")
print(f"Frequência menor nota:{l_nota.count(menor_nota)}")
""
#for com lista e colocado atraves do end=, na horizontal
nomes=list("fred,jao,pao")
for c in nomes:
    print(c, end='')
    ""
#função:def
def mostra_mensagem():
    print("Bem-vindo ao def do python")
if __name__=="__main__":
    mostra_mensagem()
    ""
def mostra_valor(p_valor):
    print("Valor:",p_valor)
if __name__=="__main__":
    mostra_valor(5)
    mostra_valor(28.5)
    ""
def calcula_dobro(valor_p):...

if __name__=="__main__":  
    valor=int(input("Digite um valor:"))
    valor_p=valor*2
    print("O valor digitado x2 foi:",valor_p)
    ""

#soma de valores def
def soma_valores(a,b):
   valor=a+b
   return valor

if __name__=="__main__":
    valor1=int(input("Valor um:"))
    valor2=int(input("Valor dois:"))
    valor_retorno=soma_valores(valor1,valor2)
    print("Soma =", valor_retorno)
    ""
def valor_absoluto(v):
   if v<0:
       valor_absoluto=-v
   else:
       valor_absoluto=v
   return valor_absoluto

if __name__=="__main__":
    valor1=float(input("Digite um valor:"))
    valor_retorno=valor_absoluto(valor1)
    print("Valor absoluto é de:", valor_retorno)
    ""
def soma(a,b):
    soma=a+b
    return soma
def subtrai(a,b):
     subtrair=a-b
     return subtrair
        
    


if __name__=="__main__":
    num1=int(input("Primeiro Valor:"))
    num2=int(input("Segundo Valor:"))
    num_retorno=soma(num1,num2)
    print("A soma é", num_retorno)
    print("A subtração é:", subtrai(num1,num2))
    ""
def soma(a,b):
    soma=a+b
    return soma
def subtrai(a,b):
     subtrair=a-b
     return subtrair
        
    


if __name__=="__main__":
    num1=int(input("Primeiro Valor:"))
    num2=int(input("Segundo Valor:"))
    opcao=int(input("[1] para somar,[2] para subtrair:"))
    if opcao==1:
     print("Soma",soma(num1,num2))    
    else:
        print("Subtração", subtrai(num1,num2))
        ""
def maximo(num1,num2):
    if num2>num1:
        maior=num2
    else:
        maior=num1
        return maior
if __name__=="__main__":
    valor1=int(input("Digite um valor:"))
    valor2=int(input("Digite um valor:"))
    valor_retorno=maximo(valor1,valor2)   
    print("O maior valor é:", valor_retorno)
    ""

def potencia(b,e):
    valor_potencia=1
    for c in range(1,e+1):
        valor_potencia*=b
        return valor_potencia
if __name__=="__main__":
    base=int(input("Digite um valor para a base:"))
    expoente=int(input("Valor do expoente:"))
    i=potencia(base,expoente)
    print("Potência:",i)
    ""
    
def multiplicar(a,b):
    multiplicar=a*b
    return multiplicar
def dividir(a,b):
     dividir=a/b
     return dividir
        
    


if __name__=="__main__":
    num1=int(input("Primeiro Valor:"))
    num2=int(input("Segundo Valor:"))
    opcao=int(input("[1] para multiplicar,[2] para dividir:"))
    if opcao==1:
     print("Multiplicar",multiplicar(num1,num2))    
    else:
        print("Dividir", dividir(num1,num2))  
    ""
 
valor = int(input("Digite um valor:"))
if valor >= 100:
    print("valor igual ou maior que 100")
else:
    print("valor menor que 100")
    ""
nota1 = float(input("nota 1:"))
nota2 = float(input("nota 2:"))    
media = (nota1+nota2)/2   
if media<5:
    print("Aluno Reprovado:")
else:
    print("Aluno aprovado")
    ""
valor = int(input("Digite um Valor:"))
resto = valor%2
if resto==0:
    print("numero par")
else:
    print("numero impar")
    ""
pesoh=0
pesom=0
altura=float(input("Digite uma altura:"))    
pesoh_ideal = (72.7* altura)-58
print("O peso ideal do homem é",pesoh_ideal)
pesom_ideal = (62.1*altura)-44.7
print("O peso ideal da mulher é",pesom_ideal)
    ""
altura=float(input("Digite uma altura:"))
genero=int(input("Digite [1] para masculino, Digite [2] para feminino:"))
if genero == 1:
    pesoh_ideal = (72.7* altura)-58
    print("O peso ideal do homem é",pesoh_ideal)
else:
    pesom_ideal = (62.1*altura)-44.7
    print("O peso ideal da mulher é",pesom_ideal)
    ""
senha=int(input("Digite uma senha:"))
if senha!=123:
    print("Senha Incorreta")
else:
    print("Acesso Liberado")
    ""
numero=int(input("Digite um número:"))
if numero==0:
    print("numero nulo")
elif numero<0:
    print("numero negativo")
else:
    print("numero positivo")
    ""
print("f|c")
f=float(input("Digite uma temperatura em farenheit:"))
for f in range(50,80+1,1):
    c=5/9*(f-32)
    print(f,'      |',c)
print("{:2.1f}{:8s}|  {:2.3f}{:3s}" .format(f,"farenheit",c,"celsius"))   
    ""
ct=0
soma=0
inicio=int(input("Digite um numero inicial:"))
fim=int(input("Digite um numero final:"))
for a in range(inicio,fim+1,2):   
    if a %2==0:
        ct= ct +1
        soma= soma+a
print("Soma:",soma)
""
for a in range(1,10+1,1):
    calculo=a*5
    print(a,"x 5=", calculo)
    ""
for a in range(1,21+1,2):
    print(a,end =" ")
    ""
lista = []


def menu():
    l_opcoes = ['c', 'r', 'u', 'd', 'e']
    print('[c]-Create')
    print('[r]-read')
    print('[u]-update')
    print('[d]-delete')
    print('[e]-exit')
    while True:
        opcao = input('Opção: ').lower()
        if opcao in l_opcoes:
            break
        else:
            print('Opção inválida, tente novamente')
    return opcao


def create():
    nome = input('Nome:')
    lista.append(nome)


def read():
    if lista != []:
        for indice, v in enumerate(lista):
            print(indice + 1, ' - ', v)
    else:
        print('Lista Vazia')


def update():
    if lista!=[]:
        read()
        try:
            p=int(input("Qual a posicao:"))
            novo_nome=input("Novo Nome:")
            lista[p]=novo_nome
        except IndexError as e:
            print("Posição inexistente(minha msg1):\n",e)
        except Exception as e:
            print("Error Exception: (minhamsg2)\n",e)
    else:
        print('Lista Vazia.')





def delete():
    if lista== []:
        print("Lista Vazia")
    else:
        print(lista)









if __name__ == '__main__':
    while True:
        op = menu()
        if op == 'c':
            create()
        elif op == 'r':
            read()
        elif op == 'u':
            update()
        elif op == 'd':
            delete()
        elif op == 'e':
            exit()
            
""
lista=[]
while True:
    print("Digite [-1] para sair")
    valor=float(input("Digite um valor:"))
    if valor==-1:
        break
    lista.append(valor)
    print("Quantidade de valores na lista",len(lista))
    print("Soma dos Valores:",sum(lista))
    print("Valor máximo", max(lista))
    print("Valor mínimo", min(lista))
    procura=float(input("Digite um Valor para Procura:"))
    if procura in lista:
        print("Valor encontrado")
        posicao=lista.index(procura)
        print("Indice da lista",posicao)
        print("Indice da lista", lista.index(procura))
    else:
        print('Valor não encontrado') 
    lista.sort()
    print("Ordem crescente:",lista)
    lista.reverse()
    print("Ordem decrescente:",lista)
    ""
class Aluno():                                     #projeto= class
    def __init__(self, nome, mensalidade, idade): #init=construtor
        self.nome=nome
        self.mensalidade=mensalidade
        self.idade=idade
    def get_nome(self):                     #get=consultar
        return self.nome
    def set_nome(self,novo_nome):           #set=alterar
        self.nome=novo_nome

    def get_mensalidade(self):                     #get=consultar
        return self.mensalidade
    def set_mensalidade(self,nova_mensalidade):           #set=alterar
        self.mensalidade=nova_mensalidade

    def get_idade(self):                     #get=consultar
        return self.idade
    def set_idade(self,nova_idade):           #set=alterar
        self.idade=nova_idade

    def mostra_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Mensalidade:", self.mensalidade)

    def retorna_dados(self):
        dados=f'{self.nome}, {self.mensalidade}, {self.idade}'  #concatenar
        return dados
if __name__=='__main__':
    aluno1=Aluno('jão', 1100.00,21)
    aluno2=Aluno('markola', 900.00,20)
    print("Aluno 1:")
    print("Nome:", aluno1.get_nome())
    print("Mensalidade:", aluno1.get_mensalidade())
    print("Idade:", aluno1.get_idade())

    print("Aluno 2:")
    print("Nome:", aluno2.get_nome())
    print("Mensalidade:", aluno2.get_mensalidade())
    print("Idade:", aluno2.get_idade())                                             #fim do get

    nome1='Roberto'                                                              #inicio do set
    aluno1.set_nome(nome1)
    print("Nome:", aluno1.get_nome())

    mensalidade1=1700
    aluno1.set_mensalidade(mensalidade1)
    print("Mensalidade:", aluno1.get_mensalidade())

    idade1=10
    aluno1.set_idade(idade1)
    print("Idade:", aluno1.get_idade())

    nome2='Luizito'
    aluno1.set_nome(nome2)
    print("Nome:", aluno2.get_nome())

    mensalidade2=4000
    aluno2.set_mensalidade(mensalidade2)
    print("Mensalidade:", aluno2.get_mensalidade())

    idade2=56
    aluno2.set_idade(idade2)
    print("Idade:", aluno2.get_idade())

    print("Mostra Dados", aluno1.retorna_dados())
    print("Mostra Dados", aluno2.retorna_dados())
 
    aluno1.mostra_dados()
    aluno2.mostra_dados()
    ""
class Funcionario(object):
    def init(self, cpf, nome, salario=0.0):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario
    def get_cpf(self):
        return self.cpf
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_salario(self):
        return self.salario
    def str(self):
        s = f"Nome: {self.nome}, CPF: {self.cpf}, salario: {self.salario:.2f}"
        return s
    def bonificacao(self):
        vlr_bonificcao = self.salario * 0.10
        return vlr_bonificcao
    def salario_total(self):
        total = self.salario + self.bonificacao()
        return total
class Gerente(Funcionario):
    def init(self, cpf, nome, salario, senha, gtd_gerencia=0):
        # self.cpf = cpf
        # self.nome = nome
        # self.salario = salario
        super().init(cpf, nome, salario)
        self.senha = senha
        self.gta_gerencia = gtd_gerencia
    # def get_cpf(self):
    #     return self.cpf
    # def get_nome(self):
    #     return self.nome
    # def set_nome(self, novo_nome):
    #     self.nome = novo_nome
    # def get_salario(self):
    #     return self.salario
    def get_gtd_gerencia(self):
        return self.gta_gerencia
    def autentica(self):
        senha = input("Senha")
        if self.senha == senha:
            print("Acesso permitido")
            return True
        else:
            print("Acesso negado.")
            return False
    def str(self):
        s1 = super().str()
        s = s1 + ",Qtd,: {}" .format(self.gta_gerencia)
        return s
    def salario_total(self):
        total = super().salario_total() + 500
        return total
if __name__ == 'main':
    f1 = Funcionario('123', 'Paulo', 1000.0)
    print(f1)
    print(f' - Funcinario 1:\nNome: {f1.get_nome()}')
    print(f'CPF: {f1.get_cpf()}')
    print(f' Salario:', f1.get_salario())
    g1 = Gerente('234', 'Paula', 300.0, 's1', 5)
    print(g1)
    print(f' - Gerente 1:\nCPF: {g1.get_cpf()}')
    print('Nome:', g1.get_nome())
    print(g1.str())
    r = g1.autentica()
    if r:
        pass
    print(r)
    # print(g1.autentica())
    # r = f1.autentica()
    print(g1.str())
    g2 = Gerente('34', 'Paulo', 5000.0, 'g2', 3)
    print('g2 - Nome:',g2.get_cpf())
    print('g2 - Nome:', g2.get_nome())
    print(g2.str())
    print('- Gerente 2:\nCPF:', g2.get_cpf())
    print('Nome:', g2.get_nome())
    bonificacao_f1 = f1.bonificacao()
    print("Bonificacao de f1", bonificacao_f1)
    print("bonificacao de g1", g1.bonificacao())
    print(f1.str())
    print(g1.str())
    print(vars(f1))
    print(f1.dict)
    print(vars(g1))
    print(g1.dict)
    print('Salario total:', f1.salario_total())
    print('Salario total:', g1.salario_total())
    r = g1.autentica()
    print(r)
    print('G2: ', g2.get_nome())
    print('str :', g1)
    ""
    
class veiculo(object):
    def __init__(self, valor, modelo, km=0):
        self.valor=valor
        self.modelo=modelo
        self.km=km

    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        self.valor=novo_valor

    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo=novo_modelo

    def get_km(self):
        return self.km
    def set_km(self, nova_km):
        self.km=nova_km

class carro(veiculo):
    def __init__(self, valor, modelo, km=0, qtd_portas=0):

        super().__init__(valor, modelo, km)
        self.qtd_portas=qtd_portas

    def get_qtd_portas(self):
        return self.qtd_portas
    def set_qtd_portas(self, nova_qtd_portas):
        self.qtd_portas=nova_qtd_portas
    def str(self):
        s=f'Valor:{self.valor}, Modelo:{self.modelo}, Km:{self.km}, Quantidade de portas:{self.qtd_portas}'
        return s
class moto(veiculo):
    def __init__(self, valor, modelo, km=0, cilindradas=0):

        super().__init__(valor, modelo, km)
        self.cilindradas=cilindradas

    def get_cilindradas(self):
        return self.cilindradas
    def set_cilindradas(self, nova_cilindradas):
        self.cilindradas=nova_cilindradas
if __name__=='__main__':
    c1= carro(300000, 'Porsche', 5000, 2 )
    c2= carro(700000, 'Ferrari',10000)
    c3= carro(1500000, 'Bugatti')

    print("Carro1")
    print("Valor:",c1.get_valor())
    print("Modelo",c1.get_modelo())
    print("Km:", c1.get_km())
    print("Quantidade de portas:", c1.get_qtd_portas())

    print("Carro2")
    print("Valor:",c2.get_valor())
    print("Modelo",c2.get_modelo())
    print("Km:", c2.get_km())

    print("Carro3")
    print("Valor:",c3.get_valor())
    print("Modelo",c3.get_modelo())

    m1= moto(50000,'Kawasaki', 8000, 1700 )
    m2= moto(60000, 'BMW', 7000, 1000)

    print("Moto1")
    print("Valor:",m1.get_valor())
    print("Modelo",m1.get_modelo())
    print("Km:", m1.get_km())
    print("Quantidade de cilindradas:", m1.get_cilindradas())

    print("Moto2")
    print("Valor:",m2.get_valor())
    print("Modelo",m2.get_modelo())
    print("Km:", m2.get_km())
    print("Quantidade de cilindradas:", m2.get_cilindradas())

    print(vars(c1))
    print(vars(c2))
    print(vars(c3))
    print(vars(m1))
    print(vars(m2))
    print("-----------------")
        ""

class pessoa():
    def __init__(self,nome, idade, endereço):
        self.nome=nome
        self.idade=idade
        self.endereço=endereço
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome=novo_nome
        
    def get_idade(self):
        return self.idade
    
    def set_idade(self, nova_idade):
        self.idade=nova_idade
        
    def get_endereço(self):
        return self.endereço 
    
    def set_endereço(self, novo_endereço):
        self.endereço=novo_endereço
        
    def str(self):
        str=f'Nome:{self.nome}, Idade:{self.idade}, Endereço:{self.endereço}'
        return str

if __name__=='__main__':
    pessoa1=pessoa('Gustavo',18,'Jardim Botanico')
        
    print("Pessoa")
    print("Nome:",pessoa1.get_nome())
    print("Idade:",pessoa1.get_idade())
    print("Endereço",pessoa1.get_endereço())
    
    nome1='Roberto'                                                              #inicio do set
    pessoa1.set_nome(nome1)
    print("Nome:", pessoa1.get_nome())
    
    idade1=25
    pessoa1.set_idade(idade1)
    print("Idade:",pessoa1.get_idade())
    
    endereço1="Aguas Claras"
    pessoa1.set_endereço(endereço1)
    print("Endereço:",pessoa1.get_endereço())



    print(vars(pessoa1))        
    """
class Aluno():                                     #projeto= class
    def __init__(self, nome, nmatricula, curso): #init=construtor
        self.nome=nome
        self.nmatricula=nmatricula
        self.curso=curso
    def get_nome(self):                     #get=consultar
        return self.nome
    def set_nome(self,novo_nome):           #set=alterar
        self.nome=novo_nome

    def get_nmatricula(self):                     #get=consultar
        return self.nmatricula
    def set_nmatricula(self,novo_nmatricula):           #set=alterar
        self.nmatricula=novo_nmatricula

    def get_curso(self):                     #get=consultar
        return self.curso
    def set_curso(self,novo_curso):           #set=alterar
        self.curso=novo_curso

    def mostra_dados(self):
        print("Nome:", self.nome)
        print("Número da Matricula:", self.nmatricula)
        print("Curso:", self.curso)

    def retorna_dados(self):
        dados=f'{self.nome}, {self.nmatricula}, {self.curso}'  #concatenar
        return dados

if __name__=='__main__':
    aluno1=Aluno('jão', 1100.00,'Medicina')
    aluno2=Aluno('markola', 9900.00,"Ciencia de Dados")
    print("Aluno 1:")
    print("Nome:", aluno1.get_nome())
    print("Matricula:", aluno1.get_nmatricula())
    print("Curso:", aluno1.get_curso())

    print("Aluno 2:")
    print("Nome:", aluno2.get_nome())
    print("Matricula:", aluno2.get_nmatricula())
    print("Curso:", aluno2.get_curso())                                           #fim do get

    nome1='Roberto'                                                              #inicio do set
    aluno1.set_nome(nome1)
    print("Nome:", aluno1.get_nome())

    nmatricula1=1700.98
    aluno1.set_nmatricula(nmatricula1)
    print("Matricula:", aluno1.get_nmatricula())

    curso1="Ciencia da computação"
    aluno2.set_curso(curso1)
    print("Curso:", aluno2.get_curso())

    print("Mostra Dados", aluno1.retorna_dados())
    print("Mostra Dados", aluno2.retorna_dados())
 
    aluno1.mostra_dados()
    aluno2.mostra_dados()