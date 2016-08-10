'''
2016-08-11 Version 0.2
Made by indosm
'''
import indosMachine as im
import sys
def main(file):
    f = open(file,"r")
    data = f.read().split()
    proc = im.Var(data)
    proc.run()
if __name__ == "__main__":
    if len(sys.argv) !=2 :
        print("Usage : python count.py [textfile]")
        sys.exit(0)
    main(sys.argv[1])
