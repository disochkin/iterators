import json


class UrlIterator:

    def __init__(self, base_url, link_array):
        self.base_url = base_url
        self.countries = link_array
        self.limit = len(link_array)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            full_url = f'{self.base_url}/{self.countries[self.counter].replace(" ","_")}'
            self.counter += 1
            return full_url
        else:
            raise StopIteration


with open('countries.json', 'r', encoding='utf-8') as fh:
    data = json.load(fh)
    countries = []
    for item in data:
        countries.append((item["name"]["common"]))

    print(countries)

for country in UrlIterator("https://en.wikipedia.org/wiki", countries):
    print(country)
