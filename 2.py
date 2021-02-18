class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def calculate_mass(self, mass_for_cm, blade_thickness):
        return self._length * self._width * mass_for_cm * blade_thickness


road_1 = Road(20, 5000)
print(f'{road_1.calculate_mass(25, 5) / 1000} т')
