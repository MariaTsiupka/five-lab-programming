from enum import Enum

class GovernmentType(Enum):
    DEMOCRACY = 1
    REPUBLIC = 2
    AUTOCRACY = 3

class Country:
    def __init__(self, name: str = "", capital: str = "", code: int = 0, population: int = 1, area: float = 1.1, GDP: int = 1, government: GovernmentType = None):
        self.__name = name
        self.__capital = capital
        self.__code = code
        self.__population = population
        self.__area = area
        self.__GDP = GDP
        self.__government = government

    def get_name(self):
        return f'Name: {self.name}'

    def get_capital(self):
        return f'{self.__capital}'

    def get_code(self):
        return f'{self.__code}'

    def get_population(self):
        return f'Area:{self.__population}'

    def get_area(self):
        return f'Area: {self.__area}'

    def get_GDP(self):
        return f'GDP: {self.__GDP}'
    def get_government(self):
        return f'Government:{self.government}'

    def calculate_population_density(self):
        return self.__population/self.__area

    def __str__(self):
        return f'{self.get_name()}, {self.get_capital()}, {self.get_code()}, {self.get_population()}, {self.get_area()}, {self.get_GDP()}, {self.get_government()}'

    def __repr__(self):
        return f'Country({self.name!r}, {self.capital!r}, {self.__code!r}, {self.__population!r}, {self.__area!r}, {self.__GDP!r}, {self.government!r})'

    def __del__(self):
        print("Called destructor")

class Land:
    def __init__(self, name: str = ""):
        self.name = name
        self.countries = []

    def add_country(self, country):
        self.countries.append(country)

    def calculate_population_density(self):
        return sum(country.calculate_population_density() for country in self.countries)
    def sort_countries_by_GDP(self):
        return sorted(self.countries, key=lambda x: x._Country__GDP, reverse=True)

    def print_top_countries_by_GDP(self, top_count):
        sorted_countries = self.sort_countries_by_GDP()
        print(f'Top {top_count} countries by GDP:')
        for i, country in enumerate(sorted_countries[:top_count]):
            print(f'{i + 1}. {country.name} - GDP: {country._Country__GDP}')

    def choose_country(self, min_GDP, preferred_government):
        eligible_countries = [country for country in self.countries if country._Country__GDP >= min_GDP and country.government == preferred_government]

        if not eligible_countries:
            print("No eligible countries found.")
            return None

        return eligible_countries[0]

def main(inst1, inst2, inst3):
    for x in (inst1, inst2, inst3):
        x.print_all()

Country1 = Country("Ukraine", "Kyiv", +380, 43000000, 603628, 2000000, GovernmentType.REPUBLIC)
Country2 = Country("Poland", "Warsaw", +48, 37000000, 322575, 150000000, GovernmentType.REPUBLIC)
Country3 = Country("USA", "Washington", +1202, 331000000, 9834000, 0, GovernmentType.REPUBLIC)

europe = Land("Europe")
europe.add_country(Country1)
europe.add_country(Country2)
europe.add_country(Country3)

print(f"Population Density of Europe: {europe.calculate_population_density()}")

europe.print_top_countries_by_GDP(3)

chosen_country = europe.choose_country(min_GDP=10000000, preferred_government=GovernmentType.REPUBLIC)
if chosen_country:
    print(f"Chosen country: {chosen_country.name}")
