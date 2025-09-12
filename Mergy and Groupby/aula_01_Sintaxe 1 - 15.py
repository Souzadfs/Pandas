
import pandas as pd

# Cadastro da loja

cadastro_a = { 'id': ['AA2930', 'BB4563', 'CC254', 'DD7879'],
              'Nome': ['Denis', 'Debora', 'Analice','Lara'],
              'idade':[34,33,10,16],
              }

cadastro_a = pd.DataFrame(cadastro_a, columns= ['id', 'Nome', 'idade'])
print(cadastro_a)

print('-------------------------------------------------')


# cadastro_b

cadastro_b= { 'id': ['AA74630', 'BB4543', 'CC544', 'DD7949'],
              'Nome': ['João', 'Denise', 'Ana Laura','Lauriete'],
              'idade':[44,43,19,17] 
              }

cadastro_b = pd.DataFrame(cadastro_b, columns=['id', 'Nome', 'idade'])
print(cadastro_b)

#Registro da compra

print('-------------------------------------------------')


# Dados com 10 elementos em cada coluna
compra = {
    'id': ['AA74630', 'BB4543', 'CC544', 'DD7949', 'AA2930', 'BB4563', 'CC254', 'DD7879', 'EE1234', 'FF5678'],
    'data': ['20/08/25', '25/02/24', '30/11/23', '01/01/25', '15/07/24', '10/06/25', '05/05/24', '12/12/23', '08/03/25', '22/09/24'],
    'valor': [100, 252, 360, 100, 145, 200, 175, 300, 220, 180]
}

# Criação do DataFrame
compra = pd.DataFrame(compra, columns=['id', 'data', 'valor'])

# Exibição
print(compra)
