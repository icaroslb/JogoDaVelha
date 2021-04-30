# Jogo da velha
# Por Icaro da Silva Barbosa (399002) e Breno Araujo de Lima (398583)

#Traducao das letras
letra = "ABC";
numero = "123";
dicionario = "012";
traduLetra = str.maketrans(letra, dicionario);
traduNumero = str.maketrans(numero, dicionario);


# Funcao do mapa
def Mapa(matriz, pontos1, pontos2):
	print( """
	
Jogador 1: %s	Jogador 2: %s
	  A  B  C
	1 %s |%s |%s  1
	  --+--+--
	2 %s |%s |%s  2
	  --+--+--
	3 %s |%s |%s  3
	  A  B  C
	""" % (pontos1, pontos2, matriz[0][0], matriz[0][1], matriz[0][2], matriz[1][0], matriz[1][1], matriz[1][2], matriz[2][0], matriz[2][1], matriz[2][2]) );


##Funcao da jogada
def jogada(matriz, simbolo, jogador): 
	posicao = input("\nJogador %s: " % (jogador)); ##Pede a posicao
	verificador = False; ## Cria um verificador
	while verificador == False: ##Laco para verificar a jogada
		posicao = posicao.upper(); ##Deixa tudo maiusculo para a manipulacao
		try:
			tamanhoTexto = len(posicao);	##Pega o tamanho das coordenadas
			alfaNumerico = posicao.isalnum();	##Verifica se a coordenada e alfanumerica
			if tamanhoTexto == 2 or (tamanhoTexto == 3 and not alfaNumerico):
				letra = posicao[0].isalpha(); ##Verifica se o primeiro caractere e letra ou numero
				if(letra):	##Se o primeiro caractere for letra
					coluna = posicao[0]; ##Pega o valor da coluna
					coluna = int(coluna.translate(traduLetra)); ##Converte posicao da coluna
					linha = posicao[tamanhoTexto-1]; ##Pega o valor da linha
					linha = int(linha.translate(traduNumero)); ##Converte em posicao da linha
				else:	##Se o primeiro caractere nao for letra
					coluna = posicao[tamanhoTexto-1];	##Pega o valor da coluna
					coluna = int(coluna.translate(traduLetra));	##Converte posicao da coluna
					linha = posicao[0];	##Pega o valor da linha
					linha = int(linha.translate(traduNumero));	##Converte em posicao da linha
				if matriz[linha][coluna] != " ":	##Verifica se a posicao e vazia
					print( "Jogada invalida!" );
					posicao = input("\nJogador %s: " % (jogador));
				else:		##Caso contrario, faz a jogada
					verificador = True;
					matriz[linha][coluna] = simbolo;
					return matriz;
			else:		##Nega se a posicao nao estiver escrita correta
				print( "Entrada invalida!" );
				posicao = input("\nJogador %s: " % (jogador))
		
		except: 	##Trata os erros
			print( "Entrada Invalida!" );
			posicao = input("\nJogador %s: " % (jogador));
			
			
			
##Funcao para verificar se alguem ganhou
def veriJogo(mapa, simbolo1, simbolo2):

	##Linhas
	linha = 0;
	possibilidade = False;
	formasGanhar = 0;
	while (linha <= 2 and not possibilidade): ##Verifica linha por linha
		coluna = 0;
		quantSimbolo1 = 0;
		quantSimbolo2 = 0;
		while (coluna <= 2 and not possibilidade): ##Verifica o simbolo de cada elemento da linha
			if (mapa[linha][coluna] == simbolo1): ##Se for igual do jogador
				quantSimbolo1 += 1;
			elif (mapa[linha][coluna] == simbolo2): ##Se for igual do inimigo
				quantSimbolo2 += 1;
			coluna += 1;
		if (quantSimbolo1 == 3): ##Verifica se a linha esta completa
			return True;
		elif (quantSimbolo1 == 2 and quantSimbolo2 == 0): ##Verifica se ha um 'xeque'
			possibilidade = True;
			formasGanhar += 1;
		linha += 1;
			
	##Colunas
	coluna = 0
	possibilidade = False
	while (coluna <= 2 and not possibilidade): ##Verifica coluna por coluna
		quantSimbolo1 = 0;
		quantSimbolo2 = 0;
		linha = 0;
		while (linha <= 2 and not possibilidade): ##Verifica o simbolo cada elemento da coluna
			if (mapa[linha][coluna] == simbolo1): ##Se for igual do jogador
				quantSimbolo1 += 1;
			elif (mapa[linha][coluna] == simbolo2): ##Se for igual do inimigo
				quantSimbolo2 += 1;
			linha += 1;
		if (quantSimbolo1 == 3): ##Verifica se a coluna estiver completa
			return True;
		elif (quantSimbolo1 == 2 and quantSimbolo2 == 0): ##Verifica se ha um 'xeque'
			possibilidade = True;
			formasGanhar += 1;
		coluna += 1;
	if (formasGanhar == 2): ##Verifica se ha 2 'xeques'
		return True;
	else:
	##Diagonal Primaria
		linha = 0;
		coluna = 0;
		quantSimbolo1 = 0;
		quantSimbolo2 = 0;
		while	(linha <= 2 and coluna <= 2): ##Verifica o simbolo de cada elemento da diagonal P
			if (mapa[linha][coluna] == simbolo1): ##Se for igual do jogador
				quantSimbolo1 += 1;
			elif (mapa[linha][coluna] == simbolo2): ##Se for igual do inimigo
				quantSimbolo2 += 1;
			linha += 1;
			coluna += 1;
		if (quantSimbolo1 == 3):	##Verifica se a diagonal P esta completa
			return True;
		elif (quantSimbolo1 == 2 and quantSimbolo2 == 0): ##Verifica se ha um 'xeque'
			formasGanhar += 1;
			if (formasGanhar == 2): ##Verifica se ha 2 'xeques'
				return True;
		
	##Diagonal Secundaria
		coluna = 0;
		linha = 2;
		quantSimbolo1 = 0;
		quantSimbolo2 = 0;
		while (linha >= 0 and coluna <= 2):	##Verifica o simbolo de cada elemento da diagonal S
			if (mapa[linha][coluna] == simbolo1):	##Se for igual do jogador
				quantSimbolo1 += 1;
			elif (mapa[linha][coluna] == simbolo2):	##Se for igual do inimigos
				quantSimbolo2 += 1;
			linha -= 1;
			coluna += 1;
		if (quantSimbolo1 == 3):	##Verifica se a diagonal S esta completa
			return True;
		elif (quantSimbolo1 == 2 and quantSimbolo2 == 0 and formasGanhar == 1):	##Verifica se ja ha um 'xeque'
			return True;


##Empate
def empate(mapa):
	linha = 0;
	while (linha <= 2):
		coluna = 0;
		while (coluna <= 2):
			if (mapa[linha][coluna] == " "):
				return True;
			coluna += 1;
		linha += 1;
	return False;

## Inicio do jogo
print( """

----------------------- Jogo da velha -------------------------
Desenvolvedores: Icaro da Silva Barbosa e Breno Araujo de Lima
Matricula: 399002 e 398583

Instrucoes:
Este e o jogo da velha. Neste jogo pode-se jogar com 2 pessoas.
Na primeira rodada o primeiro jogador escolhe com qual simbolo
ira jogar (se com o X ou com o O), apartir da segunda o jogador
que ganhar a anterior ira fazer a escolha.
No jogo, ira ser dado o mapa e o jogador da vez ira dar as
coordenas da posicao do espaco escolhido.
O sistema de pontos funciona da seguinte maneira:
  Se ganhar, o jogador recebe 1 ponto
  Se houver empate, o empate e contabilizado

""" );

input("\nTecle ENTER para continuar");

##Inicilizacao das variaveis
pontos1 = 0; ##Pontos do jogador 1
pontos2 = 0; ##Pontos do jogador 2
numEmpate = 0;
matrizMapa = [[" "," "," "], [" "," "," "], [" "," "," "]]; ##Vetor dos valores no mapa
controle1 = 1; ##Dizer que e o jogador 1
controle2 = 2; ##Dizer que e o jogador 2
vez = 1; ##Diz de quem e a vez
jogarNovamente = True; ##Diz se o jogador quer ou nao jogar novamente


while (jogarNovamente):
	pJogador = input("O jogador %s ira jogar com X ou O? " % (vez));	##Pede para inserir o simbolo
	pJogador = pJogador.upper(); ##Deixa a letra maiuscula
	while (pJogador != "X" and pJogador != "O"):	##Valida o valor
		print( "Valor invalido!" );
		pJogador = input("O jogador %s ira jogar com X ou O? " % (vez)); ##Pede para inserir o simbolo
		pJogador = pJogador.upper(); ##Deixa a letra maiuscula
	print( vez );
	if (vez == 1): ##Quando o primeiro a jogar for o jogador 1
		jogador1 = pJogador;
		if (jogador1 == "X"):	##Verifica se foi escolhido o X
			jogador2 = "O";	##Atribui o O ao outro jogador
		else:	##Quando o primeiro a jogar for o jogador 2
			jogador2 = "X";	##Atribui o X ao outro jogador
		print( "Jogador 1 = %s, jogador 2 = %s" % (jogador1, jogador2) );
	else:
		jogador2 = pJogador;
		if (jogador2 == "X"):	##Verifica se foi escolhido o X
			jogador1 = "O";	##Atribui o O ao outro jogador
		else:
			jogador1 = "X";	##Atribui o X ao outro jogador
		print( "Jogador 1 = %s, jogador 2 = %s" % (jogador1, jogador2) );
	
	## Jogo
	input("\nAperte ENTER para comecar o jogo");
	ganhar = False;
	jogPossi = True;
	while (not ganhar and jogPossi):
	
		##Vez do jogador 1
		if (not ganhar and vez == controle1 and jogPossi):
			Mapa(matrizMapa, pontos1, pontos2); ##Chama o mapa
			matrizMapa = jogada(matrizMapa, jogador1, controle1); ##Faz a jogada
			ganhar = veriJogo(matrizMapa, jogador1, jogador2); ##Verifica se alguem ganhou
			if (ganhar):
				pontos1 += 1;
				Mapa(matrizMapa, pontos1, pontos2); ##Chama o mapa
				print( "O jogador 1 ganhou!" );
			else:
				jogPossi = empate(matrizMapa);
				if (not jogPossi):
					numEmpate += 1;
					Mapa(matrizMapa, pontos1, pontos2); ##Chama o mapa
					print( "Empate!" );
				else:
					vez = controle2;
				
		##Vez do jogador 2
		elif(not ganhar and vez == controle2 and jogPossi):
			Mapa(matrizMapa, pontos1, pontos2); ##Chama o mapa
			matrizMapa = jogada(matrizMapa, jogador2, controle2); ##Faz a jogada
			ganhar = veriJogo(matrizMapa, jogador2, jogador1);
			if (ganhar):
				pontos2 += 1;
				Mapa(matrizMapa, pontos1, pontos2); ##Chama o mapa
				print( "O jogador 2 ganhou!" );
			else:
				jogPossi = empate(matrizMapa);
				if (not jogPossi):
					numEmpate += 1;
					Mapa(matrizMapa, pontos1, pontos2); ##Chama o mapa
					print( "Empate!" );
				else:
					vez = controle1;
	
	##Se que jogar novamente
	respostaConfirmacao = False;
	while (not respostaConfirmacao):	##Verifica se o jogador que jogar novamente			
		resposta = input("Voce quer jogar novamente (S/N): "); ##Pede a resposta do jogador
		resposta = resposta.upper(); ##Transforma a resposta em maiusculo
		if (resposta == "N"):	##Se ele responder nao, o jogo para
			jogarNovamente = False;
			respostaConfirmacao = True;
		elif (resposta == "S"): ##Se ele responder sim, o jogo limpa os campos
			matrizMapa = [[" "," "," "], [" "," "," "], [" "," "," "]];	#Limpa o campo para uma nova partida
			respostaConfirmacao = True;
		else: ##Se nao responder nem S nem N, ele invalida a resposta
			print( "Resposta invalida!" );

print( """
               Placar Geral:
  Jogador 1: %s	Jogador 2: %s	Empates: %s
			
""" % (pontos1, pontos2, numEmpate) );
