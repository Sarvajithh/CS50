import cowsay 
import sys


if len(sys.argv) ==2:
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, Mommy")
    cowsay.cheese("hello, Daddy")