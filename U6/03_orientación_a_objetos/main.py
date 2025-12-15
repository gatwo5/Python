from clases import Guerrero, Mago

def main():
    guerrero = Guerrero("Excalibur", 100)
    guerrero2 = Guerrero("Mag", 100)
    mago = Mago("Mago de fuego", 100)

    mago.atacar(guerrero2)
    print(guerrero2.vida)

if __name__ == "__main__":
    main()