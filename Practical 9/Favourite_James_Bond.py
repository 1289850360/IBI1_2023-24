def favorite_bond(year_born):  
    bond_actors = {  
        "Roger Moore": (1973, 1986),  
        "Timothy Dalton": (1987, 1994),  
        "Pierce Brosnan": (1995, 2005),  
        "Daniel Craig": (2006, 2021)  
    }  
  
    for actor, (start_year, end_year) in bond_actors.items():  
        if start_year <= year_born <= end_year:  
            return 'Your favorite James Bond actor is {}.'.format(actor)  

    return 'Sorry, we can not determine your favorite James Bond actor.'  

year_born = int(input('Please enter your year of birth: '))  
print(favorite_bond(year_born))
