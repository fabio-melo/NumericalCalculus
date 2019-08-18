#%%
import random

# montar a tabelinha-solução
key = [[] for x in range(26)]

# testar variaveis e montar sistema de solução
for x in range(256):
  for y in range(256):
    for z in range(256):
      res = x * 0.02 + y  * 0.04 + z * 0.04
      if (res % 1 == 0):
        key[int(res)].append(f"{chr(int(res) + 65)} -X = {x}, Y = {y}, Z = {z} == {res} \n")

#reduzir os resultados para apenas uma solução por letra
#crypto_key = [random.choice(x) for x in tbl]

#salva num arquivo
with open('nice.txt','w') as f:
  for x in key:
    f.writelines(x)




# cripto



#%%