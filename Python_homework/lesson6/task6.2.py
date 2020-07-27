class Road:
    def __init__(self, _lenght, _widh):
        self._lenght = _lenght
        self._widh = _widh

    def asfalt_mass(self, _lenght, _widh, mass_sqm, thickness):
        self.mass_sqm = mass_sqm
        self.thickness = thickness
        print(
            f'Масса асфальта, необходимого для покрытия всего дорожного полотна составляет {_lenght * _widh * mass_sqm / 1000 * thickness:.2f} тонн')


road = Road(5000, 20)
road.asfalt_mass(5000, 20, 25, 5)

''' 2 способ '''


class Road2:
    def __init__(self, _lenght, _widh):
        self._lenght = _lenght
        self._widh = _widh


class Asfalt_mass(Road2):
    def __init__(self, _lenght, _widh, mass_sqm, thickness):
        super().__init__(_lenght, _widh)
        self.mass_sqm = mass_sqm
        self.thickness = thickness
        print(
            f'Масса асфальта, необходимого для покрытия всего дорожного полотна составляет {_lenght * _widh * mass_sqm / 1000 * thickness:.2f} тонн')


a = Asfalt_mass(5000, 20, 25, 5)
