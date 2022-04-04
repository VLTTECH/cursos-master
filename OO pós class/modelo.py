class Programa:

    def __init__(self,nome, ano):
       self._nome = nome
       self.ano = ano
       self._like = 0
    
    @property
    def likes(self):
        return self._like

    def dar_like(self):
        self.like +=1
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter    
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    
    def __init__(self, duracao, nome, ano):
        super().__init__(nome, ano)
        self.duracao = duracao
        
class Serie(Programa):
    def __init__(self, temporadas, ano, nome):
        super().__init__(nome, ano)
        self.temporadas = temporadas
      



