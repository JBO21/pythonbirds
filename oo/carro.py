
""""
Exemplo:
>>> motor = Motor()
>>> motor.velocidade

>>> motor.acelerar()
>>> motor.velocidade

>>> motor.acelerar()
>>> motor.velocidade

>>> motor.acelerar()
>>> motor.velocidade

>>> motor.frear()
>>> motor.velocidade

>>> motor.frear()
>>> motor.velocidade

>>>#testando direção
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Oeste
>>>direcao.girar_a_direita()
>>>direcao.valor
'Norte'
>>>direcao.girar_a_esquerda()
>>>direcao.valor
'Oeste'
>>>direcao.girar_a_esquerda()
>>>direcao.valor
'Sul'
>>>direcao.girar_a_esquerda()
>>>direcao.valor
'Leste'
>>>direcao.girar_a_esquerda()
>>>direcao.valor
'Norte'
 >>> carro = Carro(direcao, motor)
 >>> carro.calcular_velocidade()
 0
 >>> carro.acelelar()
 >>> carro.calcular_velocidade()
1
>>> carro.acelelar()
 >>> carro.calcular_velocidade()
2
>>> carro.frear()
 >>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita_dict = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dict = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]