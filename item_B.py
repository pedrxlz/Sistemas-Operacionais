# Importando as bibliotecas de semáforo e threads.
from threading import Semaphore, Thread 

class Carteira():

# Método construtor da classe Carteira, para inicialização de parâmetros.
        def __init__(self): 
            self.saldo = 0 
            self.semaforo = Semaphore(1) # O parâmetro da função Semaphore, será a quantidade de threads que poderão passar.

        def incrementa(self):
            self.saldo += 1

        def calcula(self, v):
            with self.semaforo: # O comando with é uma espécie de abreviação do try catch, inicializa a variável e depois a fecha.
                for i in range(10000): # A cada chamada da função calcula(), será dada uma Thread como parâmetro, essa Thread irá entrar dentro do loop e chamando a função incrementa().
                    self.incrementa()
            print(f'Finalizando Thread: {v}')   # Comando with fecha a Thread.    
                
carteira = Carteira() # Criação de uma instância para Classe Carteira, inicializa com parâmetro de saldo = 0 e Semaphore(1)

# Criação de 5 Threads distintas, uma sendo inicializada após o término da anterior.
for v in range(1, 5): 
    thread = Thread(target=carteira.calcula, args=[v]) # Criação da Thread, argumento target aponta para qual função ela irá se associar, argumento args recebe o argumento da função carteira.calcula().
    print(f'\nInicializando Thread: {v}\n')
    thread.start() # Inicialização da Thread.

print(f'\nSaldo final: {carteira.saldo}') # Exibe o saldo final após todas as iterações.
