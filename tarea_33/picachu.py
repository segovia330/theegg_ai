
# usar clases

class Pokemon:
    
    def __init__(self):
        self.vida = 100

    def set_params(self, ataque, name):
        self.ataque = ataque
        self.name = name

    def recibe_ataque(self, ataque):
        self.vida = self.vida - ataque

    def win(self):
        print(self.name, ' wins!!!!')



turno = 1
pikachu = Pokemon()
jigglypuff = Pokemon()
pikachu.set_params(55, 'Pikachu')
jigglypuff.set_params(45, 'JigglyPuff')

while (pikachu.vida > 0 and jigglypuff.vida > 0):
    if turno == 1:
        jigglypuff.recibe_ataque(pikachu.ataque)
        turno = 0
        print('J ', jigglypuff.vida)

    else:
        pikachu.recibe_ataque(jigglypuff.ataque)
        turno = 1
        print('P ', pikachu.vida)

if pikachu.vida <= 0:
    jigglypuff.win()
else:
    pikachu.win()


