# countries = input().split(", ")
# capitals = input().split(", ")
# result= {print (f"{countries[i]} - > {capitals[i]}") for i in range(len(countries))}

countries = input().split(", ")
capitals = input().split(", ")

result = {country:capital for country, capital in zip(countries, capitals)}

[print(f"{country} -> {capital}") for country, capital in result.items()]