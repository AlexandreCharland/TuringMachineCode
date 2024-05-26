#This program takes an odd prime number and return the amount of solution of the following modular equation
#x^2 == p-2 mod p
import sys

#bitInput = sys.argv[1]
#tape = " "+bitInput+" "
tape = " 10 "

def a(tape, i):
    if (tape[i] != " "):
        a(tape, i+1)
    else:
        b(tape, i-1)

def b(tape, i):
    if (tape[i] == "0"):
        print("The number isn't an odd prime")
    elif (tape[i] == "1"):
        tape = tape[:i]+"0"+tape[i+1:]
        c(tape, i-1)
    else:
        print("No number were inputed")

def c(tape, i):
    if (tape[i] == "0"):
        d(tape, i-1)
    elif (tape[i] == "1"):
        e(tape, i-1)
    else:
        print("One is not a prime number")

def d(tape, i):
    if (tape[i] == "0"):
        f(tape, i+1)
    elif (tape[i] == "1"):
        tape = tape[:i]+"0"+tape[i+1:]
        qr(tape, i+1)
    else:
        print("One is not a prime number")

def e(tape, i):
    if (tape[i] == "0"):
        qa(tape, i-1)
    elif (tape[i] == "1"):
        qr(tape, i+1)
    else:
        print(tape)

def f(tape, i):
    tape = tape[:i]+"1"+tape[i+1:]
    qa(tape, i-1)

def qa(tape, i):
    if (tape[i] != " "):
        tape = tape[:i]+"0"+tape[i+1:]
        qa(tape, i-1)
    else:
        print(tape)

def qr(tape, i):
    if (tape[i] != " "):
        tape = tape[:i]+"0"+tape[i+1:]
        qr(tape, i-1)
    else:
        print(tape)

a(tape, 1)