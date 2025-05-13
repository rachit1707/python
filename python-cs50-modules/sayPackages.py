import cowsay
import sys
from hello import hello

if len(sys.argv)==2:
    cowsay.trex(sys.argv[1])
    hello(sys.argv[1])