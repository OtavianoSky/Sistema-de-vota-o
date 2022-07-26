from re import I
import Corpo

if __name__ == '__main__':
    V = Corpo.Votacao()
    V.adicionar_candidato()
    V.define_votantes()
    V.votar()
    V.mostra_resultado()