# Importando as bibliotecas de semáforo e threads.
from threading import Semaphore, Thread 

class Carteira():

# Método construtor da classe Carteira, para inicialização de parâmetros.
        def __init__(self): 
            self.saldo = 0 
            self.semaforo = Semaphore(1) # O parâmetro da função Semaphore, será a quantidade de threads que poderão passar.

        def incrementa(self):
            self.saldo += 1

        def calcula(self):
            with self.semaforo: # O comando with é uma espécie de abreviação do try catch, inicializa a variável e depois a fecha.
                self.incrementa()
                
carteira = Carteira() # Criação de uma instância para Classe Carteira, inicializa com parâmetro de saldo = 0 e Semaphore(1)

# Então as 4 threads são inicializadas ao mesmo tempo, sendo bloqueadas pelo semáforo ao qual o parametro foi definido como 1,
# ou seja, apenas uma Thread poderá funcionar simultaneamente.
for v in range(10000):
    thread_1 = Thread(target=carteira.calcula,) # Criação da Thread, argumento target aponta para qual função ela irá se associar.
    thread_1.start() # Inicialização da Thread.

    thread_2 = Thread(target=carteira.calcula,)
    thread_2.start()
        
    thread_3 = Thread(target=carteira.calcula,)
    thread_3.start()

    thread_4 = Thread(target=carteira.calcula,)
    thread_4.start()
    
print(f'\nSaldo final: {carteira.saldo}') # Exibe o saldo final após todas as iterações.


















