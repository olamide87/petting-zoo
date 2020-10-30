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

from attractions import PettingZoo, SnakePit, Wetlands



def main():
    
    
    varmint_village = PettingZoo("Varmint Village")
    slither_inn = SnakePit('Slither Inn')
    bubbling_brook = Wetlands('Bubbling Brook')

     # swimmers
    myCatfish = Catfish("Wall Singer", "Big Catfish", "Catfish Nibbles")
    bubbling_brook.add_animal(myCatfish)

    # walkers
    miss_fuzz = Camel("Miss Fuzz", "domestic Camel", "morning", "Camel Feed")
    print(miss_fuzz.feed())
    varmint_village.add_animal(miss_fuzz)

    giddy_up = Bronco("Giddy Up", "Friendly Mustang", "afternoon", "Horse Chow")
    print(giddy_up.feed())
    varmint_village.add_animal(giddy_up)

     # slither-ers??
    slimy_stan = WaterSnake(
        "Slimy Stan", "Slimy Water Snake", "mice")
    print(slimy_stan.feed())
    slither_inn.add_animal(slimy_stan)



    print("******")
    varmint_village.get_animals()
    print("******")
    slither_inn.get_animals()
    print("******")
    bubbling_brook.get_animals()

main()
