import operator

class Votacao():
    def __init__(self):
        self.candidatos = {}
        self.votantes = 0
        self.inicio = False

    # adiciona aqueles que irão concorrer.
    def adicionar_candidato(self):

        # caso a votação já tenha se iniciado, não é possivel adicionar novos candidatos.
        if self.inicio == False:
            repetir = True

            # adiciona candidatos o quanto o usuário queiser.
            while repetir == True:
                
                candidato = int(input('Digite o número do candidato que você quer adicionar: '))
                self.candidatos[candidato] = 0
                acao = input('Adicionar mais um candidato? (S/N) ')

                if acao.upper() == 'N':
                    repetir = False
            print(self.candidatos)

        else:
            print('Não se pode adicionar candidatos após a votação iniciar')

    # define a quantidade de pessoas que podem votar.
    def define_votantes(self):
        acao = int(input('Quantas pessoas podem votar?'))
        self.votantes = acao

    # busca e remove o candidato digitado.
    def remover_candidato(self):
        if self.inicio == False:
            candidato = int(input('Digite o número do candidato que você quer remover: '))
            del self.candidatos[candidato]
        else:
            print('Não se pode remover candidatos após a votação iniciar')

    # adiciona votos ao candidato pelo seu número.
    def votar(self):
        
        if self.votantes > 0:
            while self.votantes > 0:
                # assim que o primeiro voto é dado, a votação é iniciada.
                self.inicio = True

                candidato = int(input('Digite o número do candidato que você quer votar: '))
                self.candidatos[candidato] += 1

                print(f'Você votou no candidato de número {candidato}, agora ele tem {self.candidatos[candidato]} votos.')
                self.votantes = self.votantes - 1

        else:
            print('Todas as pessoas já votaram')

    #função em processamento, deve: comparar os valores de cada chave do dicionário dos candidatos e dizer o maior (vencedor).
    def mostra_resultado(self):
        max_key = max(self.candidatos.items(), key=operator.itemgetter(1))[0]
        print(f'O candidato de núemro {max_key} é o grande vencedor com total de {self.candidatos[max_key]} votos')

    


#Atlas1000