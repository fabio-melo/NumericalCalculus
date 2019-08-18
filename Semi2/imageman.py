#%%




import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from imageio import imread


def load_image(file):
	try: 
		img = imread(file)
		return img
	except:
		raise Exception("erro no processamento do arquivo")

def crypto_key():
  # montar a tabelinha-solução
  keys = [[] for x in range(26)]

  # testar variaveis e montar sistema de solução
  for x in range(256):
    for y in range(256):
      for z in range(256):
        res = x * 0.02 + y  * 0.04 + z * 0.04
        if res % 1 == 0:
          vals = [x,y,z]
          keys[int(res)].append(vals)
  return keys

class Message():
  def __init__(self, msg):
    self.msg = msg.upper()
    self.current = 0
    self.keys = crypto_key()

  def next(self):
    if self.current < len(self.msg):
      char = self.msg[self.current]
      if char.isalpha():
        ind = ord(char) - 65
        self.current += 1
        return random.choice(self.keys[ind])
      else:
        self.current += 1
        return [255,255,255]
    else:
      return False

class BreakIt(Exception): pass



def encrypt_message(msg,img):
  try:
    img = img.copy()
    for y in range(img.shape[0]):
      for x in range(img.shape[1]):
        a = msg.next()
        if a:
          #print(a)
          #print(chr(round(a[0] * 0.02 + a[1]  * 0.04 + a[2] * 0.04) + 65))
          img[y,x] = a
        else:
          #print("endmessage")
          raise BreakIt 
  except BreakIt:
    return img

def decrypt(img):
  text = ""
  for y in range(img.shape[0]):
    for x in range(img.shape[1]):
      a = img[y,x]
      char = chr(int(round(a[0] * 0.02 + a[1]  * 0.04 + a[2] * 0.04) + 65))

      text += char

  
  print(text)

text = """DONT EVER TELL ME THAT IT ISNT POSSIBLE TO DO SOMETHING LIKE THAT"""

image = plt.imread('Semi2/1up256.jpg')

txt = Message(text)
img2 = encrypt_message(txt,image)

plt.imshow(img2)
decrypt(img2)


#  {chr(int(res) + 65)}

#%%
