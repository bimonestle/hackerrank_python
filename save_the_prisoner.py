def saveThePrisoner(prisoners, candies, start):
    remaining_steps = candies % prisoners
    warning = start - 1 + remaining_steps
    
    while warning > prisoners:
      warning = (warning % prisoners)
    
    return warning