def city_country(city, country, population=0):
    if population != 0:
        full_name = city + ', ' + country + ' - população ' + population
    else:
        full_name = city + ', ' + country
    return full_name.title()
