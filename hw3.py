from abc import ABC, abstractmethod

# Абстрактный класс Камеры
class Camera(ABC):
    def __init__(self, temperature: float, pressure: float):
        self.temperature = temperature
        self.pressure = pressure

    @abstractmethod
    def process(self):
        pass

# Камера получения аммиака
class AmmoniaProductionCamera(Camera):
    def __init__(self, temperature, pressure, impurities, catalyst):
        super().__init__(temperature, pressure)
        self.impurities = impurities  # % примесей
        self.catalyst = catalyst  # Объект-катализатор

    def process(self):
        print("Процесс получения аммиака запущен.")

# Камера катализаторного окисления аммиака
class OxidationCamera(Camera):
    def __init__(self, temperature, pressure, oxygen_percentage, catalyst):
        super().__init__(temperature, pressure)
        self.oxygen_percentage = oxygen_percentage
        self.catalyst = catalyst

    def process(self):
        print("Процесс катализаторного окисления аммиака запущен.")

# Камера абсорбции диоксида азота
class AbsorptionCamera(Camera):
    def __init__(self, temperature, pressure, filter):
        super().__init__(temperature, pressure)
        self.filter = filter  # Объект фильтра

    def process(self):
        print("Процесс абсорбции запущен.")

# Камера концентрации азотной кислоты
class ConcentrationCamera(Camera):
    def __init__(self, temperature, pressure):
        super().__init__(temperature, pressure)

    def process(self):
        print("Процесс концентрации азотной кислоты запущен.")

# Абстрактный класс Катализатора
class Catalyst(ABC):
    def __init__(self, name):
        self.name = name

class IronOxideCatalyst(Catalyst):
    def __init__(self):
        super().__init__("Оксид железа")

class TinBasedCatalyst(Catalyst):
    def __init__(self):
        super().__init__("Катализатор на основе олова")

class MolybdenumCatalyst(Catalyst):
    def __init__(self):
        super().__init__("Катализатор на основе молибдена")

class PlatinumCatalyst(Catalyst):
    def __init__(self):
        super().__init__("Платина")

class RutheniumCatalyst(Catalyst):
    def __init__(self):
        super().__init__("Рутений")

# Класс Фильтра
class Filter:
    def __init__(self, brand, model, contamination_level):
        self.brand = brand
        self.model = model
        self.contamination_level = contamination_level  # % загрязненности

    def replace(self):
        self.contamination_level = 0
        print("Фильтр заменен.")

# Класс Батч (партия) 
class Batch:
    def __init__(self, ammonia_catalyst, oxidation_catalyst):
        self.ammonia_catalyst = ammonia_catalyst
        self.oxidation_catalyst = oxidation_catalyst
