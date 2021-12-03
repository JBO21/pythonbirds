class Pessoa:
    def __init__(self, nome = None, idade = 37):
        self.nome = nome


    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('zÉ')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Jackson'
    print(p.nome)
    print(p.idade)