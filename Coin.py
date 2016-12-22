#!/usr/bin/env python

# Insert import statements along with dcstring below
import random


class coin(object):
    """docstring for coin."""

    def __init__(self):
        self.face = 0
        self.flipped =[0,0]

    def flip (self, i):
        c = 0
        while c < i:
            self.face = random.randint(0,1)
            self.getFace()
            if self.face == 1:
                self.flipped[0] += 1
            else:
                self.flipped[1] += 1

            c += 1

    def getFace(self):
      if self.face == 1:
        print("Heads")
      else:
        print("Tails")

def main():
  x = coin()
  flips = int(input("How many times would you like to Flip this coin?"))
  x.flip(flips)
  print("Heads: {0} Tails: {1} Total: {2}".format(x.flipped[0], x.flipped[1], x.flipped[0]+x.flipped[1]))

main()
