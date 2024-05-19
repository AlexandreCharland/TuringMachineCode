#This program calculate the remainder of the input mod 3
import sys

bitInput = sys.argv[1]
tape = " "+bitInput+" "

def a(tape, i):
    if (tape[i] == "0"):
        a(tape, i+1)
    elif (tape[i] == "1"):
        b(tape, i+1)
    else:
        print(tape)

def b(tape, i):
    if (tape[i] == "0"):
        c(tape, i+1)
    elif (tape[i] == "1"):
        tape = tape[:i]+"0"+tape[i+1:]
        d(tape, i-1)
    else:
        print(tape)

def c(tape, i):
    if (tape[i] == "0"):
        tape = tape[:i]+"1"+tape[i+1:]
        d(tape, i-1)
    elif (tape[i] == "1"):
        tape = tape[:i]+"0"+tape[i+1:]
        e(tape, i-1)
    else:
        print(tape)

def d(tape, i):
    if (tape[i] == "0"):
        d(tape, i-1)
    else:
        tape = tape[:i]+"0"+tape[i+1:]
        a(tape, i+1)

def e(tape, i):
    if (tape[i] == "0"):
        tape = tape[:i]+"1"+tape[i+1:]
        e(tape, i-1)
    else:
        tape = tape[:i]+"0"+tape[i+1:]
        a(tape, i+1)

a(tape, 1)