import hashlib

bu=b'FREEMAN'

h=hashlib.sha256(bu).hexdigest()

print('picoCTF{1n_7h3_|<3y_of_'+h[4]+h[5]+h[3]+h[6]+h[2]+h[7]+h[1]+h[8]+'}')
