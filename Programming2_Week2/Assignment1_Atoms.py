class Atom:
    def __init__(self, symbol, atoms, neutr):
        self.symbol = str(symbol)
        self.atoms = int(atoms)
        self.neutrons = int(neutr)
        self.protons = int(0)
        self.mass = int(0)

    def proton_number(self):
        self.protons = self.atoms - self.neutrons
        return self.protons

    def mass_number(self):
        self.mass = int(sum([self.atoms, self.neutrons]))
        return self.mass

    def isotope(self, neutrons):
        self.neutrons = neutrons

    def __lt__(self, other):
        if self.protons == other.protons:
            return self.mass_number() < other.mass_number()

    def __le__(self, other):
        if self.protons == other.protons:
            return self.mass_number() <= other.mass_number()

    def __ge__(self, other):
        if self.protons == other.protons:
            return self.mass_number() >= other.mass_number()

    def __gt__(self, other):
        if self.protons == other.protons:
            return self.mass_number() > other.mass_number()

# protium = Atom('H', 1, 1)
# print(protium.n_neutrons)
# protium.isotope(3)
# print(protium.n_neutrons)

protium = Atom('H', 1, 1)
deuterium = Atom('H', 1, 2)
oxygen = Atom('O', 8, 8)
tritium = Atom('H', 1, 2)
tritium.isotope(3)

assert tritium.neutrons == 3
assert tritium.mass_number() == 4
assert protium < deuterium
assert deuterium <= tritium
assert tritium >= protium
print(oxygen > tritium)  # <-- this should raise an Exception