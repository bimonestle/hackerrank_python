def catAndMouse(x: int, y: int, z: int) -> str:
    catA = abs(x - z)
    catB = abs(y - z)
    winner = ''

    if catA < catB:
        winner = 'Cat A'
    elif catA == catB:
        winner = 'Mouse C'
    else:
        winner = 'Cat B'
    
    print(winner)
    return winner

catAndMouse(1, 2, 3)
catAndMouse(1, 3, 2)