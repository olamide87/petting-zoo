from catfish import Catfish
from chicken import Chicken
from anaconda import Anaconda
from coralsnake import CoralSnake
from mallard import Mallard
from blackmamba import BlackMamba
from lamb import Lamb
from egret import Egret
from bronco import Bronco
from camel import Camel
from kingsnake import KingSnake
from blackswan import BlackSwan
from frog import Frog
from watersnake import WaterSnake



def main():
    myCatFish = Catfish("Wall Singer", "Chicken of the Sea", "Eats Garbage")

   # print(myCatFish)

    miss_fuzz = Camel("Miss Fuzz", "domestic Camel", "morning", "Camel Feed")
    print(miss_fuzz.feed())

    giddy_up = Bronco("Giddy Up", "Friendly Mustang", "afternoon", "Horse Chow")
    print(giddy_up.feed())



main()
