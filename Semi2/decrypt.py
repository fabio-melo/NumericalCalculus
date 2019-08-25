#%%




import random, re
import numpy as np
import matplotlib.pyplot as plt


x1 = 0.02
x2 = 0.04
x3 = 0.04

def decrypt(img, x1, x2, x3):
  """ DESCRIPTOGRAFAR A IMAGEM """
    
  text = ""
  for y in range(img.shape[0]):
    for x in range(img.shape[1]):
      a = img[y,x]
      if np.all(np.equal(a,255)): text += ' '
      else: text += chr(int(round((a[0] * x1 + a[1]  * x2 + a[2] * x3) + 65)))

  return text


image = plt.imread('encrypt.bmp')

plt.imshow(image)
print(decrypt(image,x1,x2,x3))

#plt.imsave('encrypt.jpg',img2)
#with open('code.txt','w') as f:
#  f.write(dec)

#  {chr(int(res) + 65)}

#%%
