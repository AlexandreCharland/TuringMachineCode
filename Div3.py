#This program determine if the input is divisible by 3
import sys

bitInput = sys.argv[1]
tape = " "+bitInput+" "

def a(tape, i):
    if (tape[i] == "0"):
        a(tape, i+1)
    elif (tape[i] == "1"):
        b(tape, i+1)
    else:
        print("Accepted")

def b(tape, i):
    if (tape[i] == "0"):
        c(tape, i+1)
    elif (tape[i] == "1"):
        a(tape, i+1)
    else:
        print("Rejected")

def c(tape, i):
    if (tape[i] == "0"):
        b(tape, i-1)
    elif (tape[i] == "1"):
        c(tape, i-1)
    else:
        print("Rejected")

a(tape, 1)