class Atom:
    def __init__(self, symbol, protons, neutrons):
        self.protons = protons
        self.neutrons = neutrons
        self.symbol = symbol

    def proton_number(self):
        return self.protons

    def mass_number(self):
        return self.protons + self.neutrons

    def isotope(self, neutrons):
        self.neutrons = neutrons

    def symbol(self):
        return self.symbol


    def __lt__(self, other):
        if self.__class__ != other.__class__:
            return False
        if self.protons != other.protons:
            raise ValueError('You cannot compare different kind of elements')

        return self.mass_number() < other.mass_number()

        return self.protons == other.protons  \
                and self.neutron < other.neutrons

    def __le__(self, other):
        if self.__class__ != other.__class__:
            return False
        if self.protons != other.protons:
            return False

        return self.mass_number() <= other.mass_number()

protium = Atom('H', 1, 1)
deuterium = Atom('H', 1, 2)
oxygen = Atom('O', 8, 8)
tritium = Atom('H', 1, 2)
tritium.isotope(3)

assert tritium.neutrons == 3
assert tritium.mass_number() == 4
#assert protium > deuterium, 'protium should be less than deuterium'
assert deuterium <= tritium
assert tritium >= protium
#print (oxygen > tritium)


class Molecule:
    def __init__(self, formula=[]):
        self.formula = formula

    def __add__(self, other):
        if other.__class__ != self.__class__:
            raise ValueError("Added molecule must be of type Molecule")
        return Molecule(self.formula + other.formula)

    def __str__(self):
        rv = ''
        for atom,num in self.formula:
            if num == 1:
                rv += atom.symbol
            else:
                rv += f'{atom.symbol}{num}'

        return rv


    def __repr__(self):
        return self.__str__()


hydrogen = Atom('H', 1, 1)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)

water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
print (water)
print (co2)
h2oc2 = water + co2
print (h2oc2)

class Chloroplast:
    hydrogen = Atom('H', 1, 1)
    carbon = Atom('C', 6, 6)
    oxygen = Atom('O', 8, 8)

    def __init__(self):
        self.water = 8
        self.co2 = 8

    def add_molecule(self, item):
        if item.__repr__() not in ['CO2','H2O']:
            raise ValueError('Item must be either CO2 of H2O')

        if item.__class__ != Molecule:
            raise ValueError('illegal type')

        #item.__repr__() == 'H2O' and self.water += 1
        #item.__repr__() == 'CO2' and self.co2 += 1
	if item.__repr__() == 'H20':\
	    self.water += 1
	else:
	    self.co2 += 1


        if (self.water>=12 and self.co2>=6):
            self.water -= 12
            self.co2 -= 6
            suger = Molecule([ (carbon,6), (hydrogen,12), (oxygen,6) ])
            o2 = Molecule([ (oxygen,2) ])
            water = Molecule([ (hydrogen,2), (oxygen, 1) ])
            return [(suger, 1), (o2,6), (water,6)]
        else:
            return []

    def __str__(self):
        return f'Chloroplast with {self.water} H2O-molecules and {self.co2} CO2-molecules'


demo = Chloroplast()
els = [water, co2]
while (True):
    print ('\nWhat element would you like to add?')
    print ('[1] Water')
    print ('[2] carbondioxyde')
    print ('[x] Quit')
    print ('Please enter your choice: ', end='')
    try:
        foo = input()
        if foo=='x':
            print ('bye')
            break

        choice = int(foo)
        res = demo.add_molecule(els[choice-1])
        print (res)

        if (len(res)==0):
            print (demo)
        else:
            print ('\n=== Photosynthesis!')
            print (res)
            print (demo)

    except Exception:
        print ('=== That is not a valid choice.')






            



        

        
