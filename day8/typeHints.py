'''Type Hint Untuk Fungsi'''

'''Bentuk Standar Fungsi

Permasalahan Pada Fungsi

def fungsi(parameter):
    print(parameter**2)

fungsi(1)
fungsi("Ucup")
fungsi(True)
'''

# Penggunaan Fungsi Type Hints
import string

def pangkat(argument:int) -> int:
    output = 10**argument
    return output

hasil = pangkat("Ucup")
print(hasil)

def display(argument:string):
    print(argument)

display("Ucup")