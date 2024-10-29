class Veiculo:  # classe principal 
    def movimentar(self):
        print('O veiculo está em movimento')

class Carro(Veiculo): # Subclasse 
    def movimentar(self):
        print('Carro está dirigindo')
        
class Moto(Veiculo): # subclasse 
    def movimentar(self):
        print('Moto está acelerando')
        
# determinando objeto, e imprimindo
carro = Carro()
moto = Moto()

carro.movimentar()
moto.movimentar()  
