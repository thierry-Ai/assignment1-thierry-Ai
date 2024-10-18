#Solution to question 2 goes here
def identify_mushroom():
    # Question 1: Does it have gills?
    gills = input("Does your mushroom have gills? (yes/no): ").strip().lower()

    # Question 2: Does it grow in a forest?
    forest = input("Does your mushroom grow in a forest? (yes/no): ").strip().lower()

    # Question 3: Does it have a ring?
    ring = input("Does your mushroom have a ring? (yes/no): ").strip().lower()

    # Question 4: Does it have a convex cup?
    convex_cup = input("Does your mushroom have a convex cup? (yes/no): ").strip().lower()

    # Determine the mushroom based on the answers
    if gills == "no":  # Only Cepe de bordeaux has pores, the others have gills
        if forest == "yes":
            print("Your mushroom is Cepe de Bordeaux.")
        else:
            print("Invalid input. Cepe de Bordeaux grows in the forest.")
    elif gills == "yes":
        if forest == "yes":
            if ring == "yes":
                if convex_cup == "yes":
                    print("Your mushroom is Amanite Tue-mouches.")
                else:
                    print("Your mushroom is Coprin Chevelu.")
            elif convex_cup == "yes":
                print("Your mushroom is Pied Bleu.")
            else:
                print("Your mushroom is Girolle.")
        elif forest == "no":
            if ring == "yes" and convex_cup == "yes":
                print("Your mushroom is Agaric Jaunissant.")
            else:
                print("Invalid input for meadow-growing mushrooms.")
    else:
        print("Invalid input.")
