import random

def main():
    encoded_string = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽"
    for i in range(len(encoded_string)):
        print(chr(ord(encoded_string[i])>>8),end="")
        print(chr((ord(encoded_string[i]))-((ord(encoded_string[i])>>8)<<8)),end="")
        print (i,end="")


main()
