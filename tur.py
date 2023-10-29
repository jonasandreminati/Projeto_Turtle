from turtle import Turtle
t= Turtle()

def obter_distancia():
    resposta=int(input('Quantos pixels andar?'))
    return resposta
def rotacionar(turtle):
    movimento_para_lado=input('Para qual lado rotacionar? "e:esquerda""d:direita""n:nao rotacionar')
    if movimento_para_lado== 'd':
        angulo_direita(turtle)
    elif movimento_para_lado=='e':
        angulo_esquerda(turtle)
        return
def angulo_direita(turtle):
    angulo=int(input('Quantos angulos rotacionar?'))
    t.right(angulo)
def angulo_esquerda(turtle):
    angulo2=int(input('Quantos angulos rotacionar?'))
    t.left(angulo2)


while True:
    direcao=input('Para qual direcao queremos ir? "f:frente" "t:trás" : ')
    if direcao== 'f':
        distancia=obter_distancia()
        rotacionar(t)
        t.forward(distancia)
    elif direcao== 't':
        distancia=obter_distancia()
        rotacionar(t)
        t.backward(distancia)
    resposta=input('continuar andando? ')
    if resposta not in ('sim','s'):
        break