# Escova
Projeto desenvolvido para aprimorar conceitos básicos de programação em Python. 
## Motivação
**Escova** é uma jogo de baralho que sempre joguei com minha família.
## Conceitos Iniciais do Jogo
Escova pode ser jogado por dois ou quatro jogadores, com com 40 cartas: 10 de cada naipe: 1,2,3,4,5,6,7,Q,J,K, com valores de 1 até 10, respectivamente. A carta de valor 7 de ouros é chamada de *belo*. 
Inicialmente são distribuídas quatro cartas para a mesa e três cartas por jogador. O jogador mão (à direita de quem dá as cartas) inicia o jogo. Cada jogador joga uma carta por vez, recolhendo uma combinação de cartas que totalize valor 15 (independente do naipe) com a sua (por exemplo, rei de paus com cinco de copas). Quando o jogador limpar a mesa (i.e, quando todas as cartas somam 15), ele consegue uma escova (vale um ponto). Após um jogador jogar, segue-se para o jogador a sua direita. Após todos jogarem suas três cartas, distribui-se mais três cartas por jogador até o final do baralho. Somente no começo deposita-se carta diretamente do baralho para a mesa. 
Ao final do baralho, o jogador com mais cartas ganha um ponto. O jogador com mais cartas de ouro ganha um ponto. O jogador com o belo ganha um ponto. O jogador com a maior primeira também contabiliza um ponto. A primeira é a soma da maior carta numérica de cada naipe.  
O jogo é decidido por pontos, sendo 15 a pontuação a ser atingida para ganhar. Em caso de empate decide-se pela maior pontuação. 

## escova.py
O código simula uma partida de escova entre dois jogadores: você e o computador. Em nível inicial, programou-se o computador para jogar uma carta aleatória em sua mão e escolher uma opção aleatória de jogada. 
