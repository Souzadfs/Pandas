
import pandas as pd

# Cadastro da loja

cadastro_a = { 'id': ['AA2930', 'BB4563', 'CC254', 'DD7879'],
              'Nome': ['Denis', 'Debora', 'Analice','Lara'],
              'idade':[34,33,10,16],
              }

cadastro_a = pd.DataFrame(cadastro_a, columns= ['id', 'Nome', 'idade'])
print(cadastro_a)


# cadastro_b

cadastro_b= { 'id': ['AA74630', 'BB4543', 'CC544', 'DD7949'],
              'Nome': ['João', 'Denise', 'Ana Laura','Lauriete'],
              'idade':[44,43,19,17] 
              }

cadastro_b = pd.DataFrame(cadastro_b, columns=['id', 'Nome', 'idade'])
print(cadastro_b)

