from random import shuffle
from itertools import combinations
import random
from time import sleep

class Carta:
    """
    Elemento básico do jogo
    """
    def __init__(self,valor=1,naipe='o'):
        self.valor = valor
        self.naipe = naipe.upper()
        
    def __str__(self):
        if self.valor<=7:
            return '<'+str(self.valor)+','+self.naipe+ '>'
        elif self.valor==8:
            return '<Q,'+self.naipe+'>'
        elif self.valor==9:
            return '<J,'+self.naipe+'>'
        elif self.valor==10:
            return '<K,'+self.naipe+'>'

    def __repr__(self):
        return f'Carta(valor={self.valor},naipe={self.naipe})'
    
    def get_valor(self):
        return self.valor
    
    def get_naipe(self):
        return self.naipe
    
    def __add__(self,othercarta):
        return self.valor+othercarta.get_valor()

class Baralho:
    """
    Baralho de 40 cartas
    """
    def __init__(self):
        self.cartas = []
        for n in ['O','P','C','E']:
            for i in range(1,11):
                self.cartas.append(Carta(i,n))
        shuffle(self.cartas)

    def __repr__(self):
        return f'Baralho({len(self.cartas)} cartas)'
    
    def __str__(self):
        """
        Imprime o baralho
        """
        x = '\n\t####Baralho####\n\n'
        for i in range(len(self.cartas)):
            if i>0:
                x+='\t'
                if i%4==0:
                    x+='\n'
            x += f'Carta {i+1} ' + str(self.cartas[i])
        return x+'\n\n'

    def embaralhar(self):
        """
        Embaralha as 40 cartas    
        """
        shuffle(self.cartas)

    def contar_cartas(self):
        '''
        Retorna quantas cartas há no baralho
        '''
        return len(self.cartas)
    
    def remover_carta(self):
        """
        remove a última carta do baralho retornando a Carta removida
        """
        carta = self.cartas.pop()
        return carta

class Player:
    """
    Classe que representa cada jogador
    """
    def __init__(self,name = 'Jogador 1'):
        self.name = name
        self.cartas=[]
        self.mao=[]
        self.score=0

    def __str__(self):
        if len(self.mao)==0:
            return '\t\t'+self.name + ' sem cartas.\n'
        else:
            x='\tCartas na mão de ' + self.name +':\n'
            for carta in self.mao:
                x+='\t'+str(carta)
            return x+'\n'

    def get_name(self):
        return self.name

    def get_cartas(self):
        return self.cartas

    def get_cartas_mao(self):
        return self.mao
    
    def __repr__(self):
        return f'Jogador({len(self.mao)} cartas na mao,{len(self.cartas)} cartas)'
    
    def guardar_carta(self,carta):
        self.cartas.append(carta)
        
    def receber_carta(self,carta):
        self.mao.append(carta)

    def possui_carta(self,carta):
        """
        Verifica se o jogador está com a carta na mão, retornando valor lógico e posição
        """
        valor= False
        posicao=-1
        for i,x in enumerate(self.mao):
            if x.get_valor()==carta.get_valor() and x.get_naipe()==carta.get_naipe():
                valor = True
                posicao = i
        return valor, posicao

    def jogar_carta(self,carta):
        '''
        Se jogador possuir carta, retira da mão do jogador e retorna a carta.
        Se jogador não possui a carta, retorna None
        '''
        valor,i = self.possui_carta(carta)
        if valor:
            return self.mao.pop(i)
        else:
            return None

    def add_score(self,score):
        """
        Adiciona score ao score do jogador
        """
        self.score += score
        
    def contar_cartas(self):
        '''Conta quantas cartas jogador possui'''
        return len(self.cartas)

    def contar_ouro(self):
        '''contabiliza quantas cartas de ouro o jogador possui'''
        count=0
        for carta in self.cartas:
            if carta.get_naipe()=='O':
                count+=1
        return count

    def contar_primeira(self):
        '''contabiliza a soma da maior carta numérica de cada naipe'''
        maiores = [0,0,0,0] #[O,E,P.C]
        naipes = ['O','E','P','C']
        for carta in self.cartas:
            for i,n in enumerate(naipes):
                if carta.get_naipe()==n:
                    if carta.get_valor()<=7 and carta.get_valor()>maiores[i]:
                        maiores[i]=carta.get_valor()
        soma=0
        for i in range(len(maiores)):
            soma +=maiores[i]
        return soma

    def contar_belo(self):
        '''
        Verifica se jogardor esta com o belo (sete de ouro)
        retorna valor 0 ou 1
        '''
        valor = 0
        for carta in self.cartas:
            if carta.get_valor()==7 and carta.get_naipe()=='O':
                valor = 1
        return valor
    
    def zerar_cartas(self):
        """
        Zera a lista de cartas do jogador
        """
        self.cartas.clear()

class Mesa:
    """
    Mesa do jogo
    """
    def __init__(self):
        self.cartas = []

    def __str__(self):
        """
        Imprime a lista de cartas que estão na mesa
        """
        x = '\n\t\tCartas na Mesa\n\t'
        if len(self.cartas)==0:
            return '\tNão há cartas na mesa.\n'
        else:
            for i,carta in enumerate(self.cartas):
                x += str(carta)+'\t'
                if i%5==0 and i>0:
                    x += '\n\t'

        return x+'\n'

    def get_cartas(self):
        """
        Lista as cartas da mesa
        """
        return self.cartas
        
    def receber_carta(self,carta):
        """
        Recebe uma carta na mesa
        """
        self.cartas.append(carta)

    def carta_na_mesa(self,carta):
        """
        Verifica se a carta está na mesa, retornando False,-1 ou True,i,
        onde i é o índice onde a carta está
        """
        valor, posicao  = False,-1
        if len(self.cartas)==0:
            return False,-1
        else:
            for i,y in enumerate(self.cartas):
                if carta.get_naipe()==y.naipe and carta.get_valor()==y.get_valor():
                    valor=True
                    posicao=i
                    break
        return valor, posicao
    
    def retirar_carta(self,carta):
        """
        Retira uma carta da mesa, retornando a carta se está na mesa. Retorna None cc
        """
        y,i = self.carta_na_mesa(carta)
        if y:
            return self.cartas.pop(i)
        else:
            return None

    def jogadas(self):
        """
        Retona uma lista com as possibilidades de cartas para serem jogadas
        """
        menores = []
        maiores = []
        for x in self.cartas:
            if x.get_valor()<=7:
                menores.append(x)
            else:
                maiores.append(x)
        possibilidades =[]
        k = min(9,len(menores))
        if k>=3:
            for i in range(3,k+1):
                for lista in combinations(menores,i):
                    total = soma(lista)
                    if total==15:
                        possibilidades.append(list(lista))
        if len(maiores)>=1:
            k=min(5,len(menores))
            for carta in maiores:
                for i in range(1,k+1):
                    for lista in combinations(menores,i):
                        listar = list(lista)
                        total=carta.get_valor()+soma(listar)
                        if total==15:
                            listar.append(carta)
                            possibilidades.append(listar)
        return possibilidades
            
def soma(v):
    """
    retorna a soma de uma lista de Cartas
    """
    soma=0
    for i in range(len(v)):
        soma += v[i].get_valor()
    return soma

def carta_na_lista(lista,carta):
    '''
    Verifica se a carta está na lista.
    retorna valor_lógico, i
    '''
    valor,posicao = False,-1
    for i in range(len(lista)):
        if carta.get_valor()==lista[i].get_valor() and carta.get_naipe()==lista[i].get_naipe():
            valor = True
            posicao = i
    return valor, posicao

def imprimir_possibilidades(mesa,carta,aut = True,time=1.0):
    '''
    Imprime as possibilidades de jogadas com a carta na lista
    retorna uma lista com as cartas da jogada escolhida
    No caso de aut = True, retorna uma jogada automatizada
    Aguardar time to sleep
    '''
    lista = list(mesa.jogadas())
    lista2=[]
    for i in range(len(lista)):
        valor,posicao = carta_na_lista(lista[i],carta)
        lista[i][0],lista[i][posicao] = lista[i][posicao],lista[i][0] 
        if valor:
            lista2.append(lista[i])
    k = len(lista2)
    if k==0:
        print('\n\t\t### Não há jogadas disponíveis. ###')
        return []
    elif k==1:
        print('\tO lançe escolhido é:\n')
        x = '\t'
        for carta1 in lista2[0]:
            x += str(carta1)+'  '
        x+='\n'
        print(x)  
        return lista2[0]
    else:
        if aut:
            i = random.randint(0,k-1)
            print(f'\tO lance escolhido foi:\n')
            x = f'\t( {i+1} ) '
            for carta1 in lista2[i]:
                x += str(carta1)+'  '
            x+='\n'
            print(x)
            sleep(time)
        else:
            print('\tOs lançes possiveis são:\n')
            for i in range(k):
                x = f'\t( {i+1} ) '
                for carta1 in lista2[i]:
                    x += str(carta1)+'  '
                x+='\n'
                print(x)
            i=-1
        while not (i>=0 and i<k):
            try:
                i = int(input('Informe o lançe escolhido: \n\t'))-1
            except ValueError:
                i = int(input('Informe número do lance: \n\t'))-1
            if i<0 or i>=k:
                print('\n\t ###Erro, tentar novamente:')
        return lista2[i]

def colher_jogada(player, mesa_f,aut=True,time=1.0):
    '''
    Exibe as cartas do jogador e na mesa para que jogador escolha jogada
    Retorna a carta desejada. Se não houver cartas na mao, devolve None
    time = time to sleep
    '''
    print(mesa_f)
    print('\t\tCartas na mão de '+ player.get_name()+':')
    lista = player.get_cartas_mao()
    if len(lista)==0:
        return None
    elif not aut:
        for i in range(len(lista)):
            print(f'\t ( {i+1} ): {str(lista[i])}')
        i=-1
        while not (i>=0 and i<len(lista)):
            try:
                i = int(input('Informe qual carta jogar: \n\t'))-1
            except ValueError:
                i = int(input('Informe número da carta a jogar: \n\t'))-1
            if i<0 or i>=len(lista):
                print('Erro, tentar novamente.')
        return lista[i]
    else:
        for i in range(len(lista)):
            print(f'\t ( {i+1} ): <X,X>')
        i = random.randint(0,len(lista)-1)
        print(f'\t Jogada selecionada: '+str(lista[i]))
        sleep(time)
        return lista[i]

def rodada(player,mesa,pontuacao,lista_pegadas,aut=True,time=1):
    '''
    Uma rodada completa
    '''
    carta_jogada=colher_jogada(player,mesa,aut=aut,time=time)
    mesa.receber_carta(player.jogar_carta(carta_jogada))
    jogada_inteira=imprimir_possibilidades(mesa,carta_jogada,aut = aut,time=time)

    if len(jogada_inteira)>0:
        lista_pegadas.append(player.get_name())

    for carta in jogada_inteira:
        player.guardar_carta(mesa.retirar_carta(carta))
        if len(mesa.get_cartas())==0:
            print(f'\n\t\t### {player.get_name()} fez uma escova!!! ###\n')
            pontuacao[player.get_name()] += 1
    print('\n\t'+20*'-#'+'\n')
    if aut:
        sleep(time)


def contar_pontuacao(jogadores,pontuacao):
    """
    Averigua e contabiliza a pontuação dos jogadores com base nas cartas na mão dos jogadores
    Se a soma das cartas não foi 40, retorna Jogo inacabado
    Obs. Se jogo for em duplas, dar entrada numa lista dos dois jogadores que estão armazenando as cartas
    """
    num_players = len(jogadores) #deve ser sempre 2, mesmo se jogo for de dupla
    if num_players!= 2:
        return 'Quantidade de jogadores diferente de DOIS'
    else:
        if jogadores[0].contar_cartas()+jogadores[1].contar_cartas()!=40:
            return 'JogoInacabado'
        else:
            qtd_cartas = [player.contar_cartas() for player in jogadores]
            qtd_ouro = [player.contar_ouro() for player in jogadores]
            qtd_belo = [player.contar_belo() for player in jogadores]
            for i in range(num_players):
                if qtd_cartas[i]>20:
                    pontuacao[jogadores[i].get_name()] +=1
                    print(f'\t {jogadores[i].get_name()} ganhou carta.\n')
                if qtd_ouro[i]>5:
                    pontuacao[jogadores[i].get_name()] +=1
                    print(f'\t {jogadores[i].get_name()} ganhou ouro.\n')
                if qtd_belo[i]>0:
                    pontuacao[jogadores[i].get_name()] +=1
                    print(f'\t {jogadores[i].get_name()} ganhou belo.\n')
            if jogadores[0].contar_primeira() > jogadores[1].contar_primeira():
                pontuacao[jogadores[0].get_name()] +=1
                print(f'\t {jogadores[0].get_name()} ganhou primeira.\n')
            elif jogadores[0].contar_primeira() < jogadores[1].contar_primeira():
                pontuacao[jogadores[1].get_name()] +=1
                print(f'\t {jogadores[1].get_name()} ganhou primeira.\n')
            else:
                print('\tPrimeira empatada.\n')
            sleep(5)
    
def partida(jogadores, pontuacao):
    """
    Desenrolar de uma partida
    """
    deck = Baralho()
    mesa = Mesa()
    lista_pegadas=[]
    for jogador in jogadores:
        jogador.zerar_cartas()

    for i in range(4):
        mesa.receber_carta(deck.remover_carta())

    ## Virar o belo na mesa dando as cartas ganha um ponto
    for carta in mesa.get_cartas():
        if carta.get_naipe()=='O' and carta.get_valor()==7:
            pontuacao[jogadores[-1].get_name] += 1

    ## Verifica se a soma da mesa é 15, caso em que jogador que dá as cartas faz uma escova.
    if soma(mesa.get_cartas()) == 15:
        print(mesa)
        print(f'\t{jogadores[-1].get_name()} escovou!\n')
        num_cartas_mesa = len(mesa.get_cartas())
        for i in range(num_cartas_mesa):
            jogadores[0].guardar_carta(mesa.retirar_carta(mesa.get_cartas()[0]))
        
    num_rodada=0
    while deck.contar_cartas()>0:
        num_rodada += 1
        print('\t'+4*'-#'+f' {num_rodada}a RODADA '+4*'#-')
        for j in range(len(jogadores)):
            for i in range(3):
                jogadores[j].receber_carta(deck.remover_carta())

        for i in range(3):
            for j in range(len(jogadores)):
                if jogadores[j].get_name()=='Computador':
                    rodada(jogadores[j],mesa,pontuacao,lista_pegadas,aut=True,time=2.5)
                else:
                    rodada(jogadores[j],mesa,pontuacao,lista_pegadas,aut=False)

    print(f'\t* {lista_pegadas[-1]} levou as cartas de mesa.\n')

    num_last = -1
    for i in range(len(jogadores)):
        if jogadores[i].get_name()==lista_pegadas[-1]:
            num_last=i

    num_cart_mesa = len(mesa.get_cartas())
    for i in range(num_cart_mesa):
        jogadores[num_last].guardar_carta(mesa.retirar_carta(mesa.get_cartas()[0]))
    
    contar_pontuacao(jogadores,pontuacao)

    for player in jogadores:
        print(f'\tQuantidade de Cartas de {player.get_name()} = {player.contar_cartas()}')
        print(f'\tQuantidade de Ouros de  {player.get_name()} = {player.contar_ouro()}')
        print(f'\tPrimeira de {player.get_name()}  \t  = {player.contar_primeira()}')
        print(f'\tO 7 belo está com {player.get_name()} \t = {player.contar_belo()}') 
        print(f'\tA pontuação do jogador {player.get_name()} é {pontuacao[player.get_name()]}\n')
    sleep(5)

def ha_ganhadores(jogadores,pontuacao):
    """
    Verifica se há campeão: aquele que fizer 15 pontos. Em caso de empate em quinze ou mais pontos, deve-se jogar novamente
    retornar valor_lógico, nome_campeão
    """
    valor = False
    p0 = pontuacao[jogadores[0].get_name()]
    p1 = pontuacao[jogadores[1].get_name()]
    if p0>=15 and p0>p1:
        return False,jogadores[0].get_name()
    elif p1>=15 and p0<p1:
        return False,jogadores[1].get_name()
    else:
        return True,None

if __name__=='__main__':
    
    jogadores = [Player('Your_Name'),Player('Computador')]
    pontuacao = {} #Pontuação é um dicionário
    continuar = True 
    ganhador = '' 
    # Inicializa a pontuação
    for i in range(len(jogadores)):
        pontuacao[jogadores[i].get_name()] = 0
    
    print('\t\t### Inicia-se o jogo da escova ###\n')
    continuar,ganhador = ha_ganhadores(jogadores,pontuacao)
    while continuar:
        partida(jogadores,pontuacao)
        jogadores.append(jogadores.pop(0))
        continuar, ganhador = ha_ganhadores(jogadores,pontuacao)
    
    print(f'O ganhador foi {ganhador}.')