from array import *
def main():
    table = array('i', [1000, 2000, 3000, 4000, 5000, 8000,\ 10000, 20000, 30000, 50000])
    sum = 0
    while True:
        number = int(input("enter number: "))
        if number == -999: