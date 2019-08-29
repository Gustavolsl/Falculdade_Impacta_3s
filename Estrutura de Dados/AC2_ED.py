'''
EXPLICACAO
Uma pilha é uma estrutura de dados que tem um "topo".

Ela guarda quantos elementos quisermos, mas só podemos ver/retirar
o elemento do topo.

Quando adicionamos um elemento, adicionamos no topo.

Em uma pilha a operação "colocar no topo" é chamada de "push",
e a operação "tirar do topo" é chamada de "pop".

Por exemplo:
    [] é uma pilha vazia.
    Se fizermos push(1), teremos a pilha [1] (1 no topo)
    Se fizermos push(2), push(5), teremos [1,2,5] (5 no topo)
    Se fizermos pop(), saiu o topo (5), e sobrou [1,2]
'''

'''
EXERCICIO

Continuando o exemplo, tinhamos [1,2].

Digamos que fazemos push(4), push(8). Como está a pilha? 
Responda na forma de uma lista na variavel pilha1
'''
pilha1=[1,2,4,8]

'''
EXERCICIO

Novo exemplo. Temos a pilha vazia []
Fazemos push(9),push(8),pop(),push(7),push(6),pop(). 

Como está a pilha? Responda na variavel pilha2.
'''
pilha2=[9,7]




'''
EXERCICIO

Novamente, começamos com uma pilha vazia.
E se fizermos 
push(9),push(8),push(7),push(6),pop(),pop(),pop() ?. 
'''
pilha3=[9]


'''
EXPLICACAO

Em python, podemos implementar o conceito de pilha usando uma lista, que têm as funções
append e pop

Por exemplo:

    >pilha = [] #inicializo uma pilha vazia
    >pilha.append(5)
    >pilha.append(8)
    >print(pilha)
    [5,8]
    >pilha.append(4)
    >pilha.append(3)
    >print(pilha)
    [5,8,4,3]
    >topo = pilha.pop()
    >print(topo)
    3
    >print(pilha)
    [5,8,4]

O append insere no final da lista e o pop tira do final da lista
'''

'''
EXPLICAÇÃO

Dá erro tentar tirar uma coisa que não está na pilha.

Exemplo:

    > pilha = []
    > pilha.append(3)
    > topo = pilha.pop()
    > print(topo)
    3
    > topo = pilha.pop()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: pop from empty list

Para evitar esse problema, precisamos aprender a verificar se uma pilha está 
vazia.

Basta ver quantos elementos tem na lista. len faz exatamente isso.
    > pilha = []
    > pilha.append(30)
    > pilha.append(40)
    > pilha.append(50)
    > len(pilha)
    3   #pilha tem os 3 elementos: 30,40,50. Posso tirar um
    > topo = pilha.pop()
    > print(topo)
    50
    > len(pilha)
    2   #pilha tem 2 elementos: 30,40. Posso tirar um
    > topo = pilha.pop()
    > print(topo)
    40
    > len(pilha)
    1   #pilha tem 1 elemento: 30. Posso tirar ele
    > topo = pilha.pop()
    > print(topo)
    30
    > len(pilha)
    0   #pilha está vazia. Se eu tentar tirar algum elemento, vai dar pau
'''

'''
EXERCICIO
Faça uma função pilha_vazia que retorna:
     True se a pilha está vazia;
     False se não está
'''
def pilha_vazia(pilha):
    if len(pilha) == 0:
        return True
    else:
        return False
   


'''
EXERCICIO

Faça uma função pilha_letras, que recebe uma string e vai colocando as letras
da string uma a uma em uma pilha. A cada letra que for colocada, sua
função deve tirar uma fotografia da pilha (chamando a função
fotografa com sua pilha como argumento: fotografa(pilha)).
Não tire uma fotografia da pilha vazia

Sua função deve retornar a pilha pronta

Vou deixar um rascunho pra você começar

def pilha_letras(texto):
    for letra in texto:                            | cada vez com a variavel 'letra' 
        print(letra)      |  esse código é           sendo uma das letras do texto
        print('ola')      |  executado várias vezes

'''

def pilha_letras(texto):
      pilha_letras=[]
      for letra in texto:
            pilha_letras.append(letra)
            if len(pilha_letras) != 0:
                  fotografa(pilha_letras)
      return pilha_letras
      




'''
EXERCICIO

Estamos quase prontos para fazer o exercicio principal da aula, a função
'balanceado'.

Primero, vamos fazer uma funcao que verifica se um determinado "abre" 
encaixa com um "fecha".

Por exemplo, "(" encaixa com ")", mas não encaixa com "]", "}", nem "(", nem "["
Por exemplo, "[" encaixa com "]", mas não encaixa com ")", "}", nem "(", nem "["
Na verdade, "(" só encaixa com ")", "[" só encaixa com "]" e "{" só encaixa com "}"

Faça uma função encaixa, que recebe duas strings, um "abre" e um "fecha", e retorna
True se eles encaixam (False se não encaixarem)
'''
def encaixa(abre, fecha):
      if abre == '(' and fecha == ')' or abre == '[' and fecha == ']' or abre == '{' and fecha == '}':
            return True
      else:
            return False
      
      

'''
EXPLICACAO

Uma sequencia de parenteses "(" ")", colchetes "[" "]" e chaves "{" "}" 
é dita balanceada se cada simbolo "aberto" é "fechado" 
em um momento apropriado 

Por exemplo
'([])' é uma sequencia balanceada
'([)]' não é balanceada
'([]' não é balanceada
')' não é balanceada
'' é balanceada

Como já discutimos, esse problema é interessante porque
tem uma correspondencia com o problema de validar um arquivo html,
onde as tags html abrem e fecham, como os parenteses.
'''

'''
EXERCICIO

Escreva uma funcao "balanceada" que recebe uma string e
retorna "True" se a string representa uma sequencia balanceada, 
"False" caso contrário.

Não deixe de olhar o arquivo pilhas_simulacao para entender/relembrar 
como o algoritmo deve funcionar

Sua função só vai receber parênteses, colchetes e chaves.
Não precisa se preocupar com nenhum outro caractere

'''

def balanceada(string):
      lista_de_caracter_abre = []
      retorno = ''
      if string != '':
            #pilha = pilha_letras(string)
            for caracter in string:
                  if caracter == '(' or caracter == '[' or caracter == '{':
                        lista_de_caracter_abre.append(caracter)
                  elif caracter == ')' or caracter == ']' or caracter == '}':
                        retorno = encaixa(lista_de_caracter_abre.pop(),caracter)
                        if retorno == False:
                              break
            return retorno
                        
                  


            
    
'''
EXERCICIO

Podemos fazer alguns upgrades na funcao balanceada:
    * Além de aceitar (, [ e {, queremos que ela aceite <, que será fechado com >
    * Se vier alguma letra/numero (ou qualquer outra coisa que nao seja (){}[]<> a funcao
    deve ignorar em vez de dar erro
    * Se a string for balanceada, a funcao deve calcular qual foi o **maximo** 
    tamanho da pilha. Esse valor deve ser "fotografado" uma unica vez, 
    no final da execucao. Sugiro que você vá calculando, sem saber se a string
    é balanceada ou não, mas tire a fotografia uma linha antes do "return true"
'''


  
import unittest
import hashlib
class TestStringMethods(unittest.TestCase):

    def test_001_var_pilha1(self):
        self.verifica_pilha(pilha1,'30683e81e541f4f031f50134b6c4df4fb2325fb6222265fffa004832')
    def test_002_var_pilha2(self):
        self.verifica_pilha(pilha2,'12f16a9f7220b8fbba114ca53fa589d2137060e48ef51f87ede96a7d')

    def test_003_var_pilha3(self):
        self.verifica_pilha(pilha3,'fc53f829aced039d8170455b2e1b24e1fa08bebfd5457257832257a4')

    def test_004_pilha_vazia(self):
        pilha_teste4 = [1,2,3]
        vazia =[]
        self.assertTrue(pilha_vazia(vazia))
        self.assertFalse(pilha_vazia(pilha_teste4))

    def test_005_pilha_letras(self):
        pilha_dada_por_aluno = pilha_letras('banana')
        correto = ['b', 'a', 'n', 'a', 'n', 'a']
        self.assertEqual(pilha_dada_por_aluno,correto)

    def test_006_pilha_letras_verifica_fotos(self):
        reseta_fotos()
        pilha_letras('banana')
        album_correto = [['b'], ['b', 'a'], ['b', 'a', 'n'], ['b', 'a', 'n', 'a'], ['b', 'a', 'n', 'a', 'n'], ['b', 'a', 'n', 'a', 'n', 'a']]
        album_execucao_da_funcao = fotografias


        if album_correto != album_execucao_da_funcao:
            print('Passei para sua função a palavra "banana".')
            print('Ela funcionou, mas não tirou as fotografias corretas')
            explica_erro(album_execucao_da_funcao,album_correto)
            self.fail('erro nas fotografias')


    def test_007_encaixa(self):
        self.assertTrue(encaixa('(',')'))
        self.assertTrue(encaixa('[',']'))
        self.assertTrue(encaixa('{','}'))
        self.assertFalse(encaixa('{',')'))
        self.assertFalse(encaixa('{',']'))
        self.assertFalse(encaixa('{','{'))
        self.assertFalse(encaixa('(',']'))
        self.assertFalse(encaixa('(','}'))
        self.assertFalse(encaixa('(','('))
        self.assertFalse(encaixa('[','}'))

    def test_008_primeiros_exemplos_balanceado(self):
        self.assertEqual(balanceada('([])'),True)
        self.assertEqual(balanceada('([]{})'),True)
        self.assertEqual(balanceada('([][])'),True)
        self.assertEqual(balanceada('([}[])'),False)
        self.assertEqual(balanceada('([}{])'),False)
        self.assertEqual(balanceada('([}{])'),False)
    
    def test_009_balanceado_mais_complexo(self):
        self.assertEqual(balanceada('([]'),False)
        self.assertEqual(balanceada('('),False)
        self.assertEqual(balanceada('((('),False)
        self.assertEqual(balanceada(')'),False)
        self.assertEqual(balanceada('(()))'),False)
        self.assertEqual(balanceada(''),True)

    def test_010_balanceado_upgrade_parenteses_angulares(self):
        self.assertEqual(balanceada('([]<>)'),True)
        self.assertEqual(balanceada('(<>{})'),True)
        self.assertEqual(balanceada('<[][]>'),True)
        self.assertEqual(balanceada('([}<>)'),False)
        self.assertEqual(balanceada('([><])'),False)
        self.assertEqual(balanceada('(<}{>)'),False)
        self.assertEqual(balanceada('<[]'),False)
        self.assertEqual(balanceada('<'),False)
        self.assertEqual(balanceada('>'),False)
    
    def test_011_balanceado_upgrade_letras_aleatorias(self):
        self.assertEqual(balanceada('([a]a<>i)'),True)
        self.assertEqual(balanceada('(<>g{g}j)'),True)
        self.assertEqual(balanceada('<[][]>'),True)
        self.assertEqual(balanceada('g(g[g}<>)'),False)

    def verifica_pilha(self,pilha,codigo_correto):
        codigo_resp_aluno = hashlib.sha224(str(pilha).encode('utf-8')).hexdigest()
        self.assertEqual(codigo_resp_aluno,codigo_correto)
    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)



fotografias = []
def reseta_fotos():
    global fotografias
    fotografias = []

def fotografa(elemento):
    try:
        copia = elemento.copy()
    except:
        copia = elemento
    fotografias.append(copia)

def explica_erro(album1,album2):

    print('')

    if len(album1) == 0 and len(album2) > 0:
        print('Você não tirou nenhuma fotografia')
        print('Primeira fotografia esperada:')
        print(album2[0])
        return

    
    tam_do_menor = min(len(album1),len(album2))
    diferentes = [i for i in range(tam_do_menor) if album1[i] != album2[i]]
    if len(diferentes) > 0:
        menor_diferente = min(diferentes)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('Sua primeira fotografia errada:')
        print(album1[menor_diferente])
        print('Era esperado:')
        print(album2[menor_diferente])
        return

    if len(album1) < len(album2):
        print('Você tirou fotografias a menos')
        print('Voce tirou '+str(len(album1))+ ' fotografias, mas era pra tirar ' + str(len(album2)))
        menor_diferente = len(album1)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('A primeira fotografia que faltou:')
        print(album2[menor_diferente])

    if len(album1) > len(album2):
        print('Você tirou fotografias a mais')
        print('Voce tirou '+str(len(album1))+ ' fotografias, mas era pra tirar ' + str(len(album2)))
        menor_diferente = len(album2)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('A primeira fotografia que sobrou:')
        print(album1[menor_diferente])
runTests()
