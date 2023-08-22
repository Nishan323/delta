# creating a dictionary
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome",
  "England": "London"
}

print(country_capitals)
# Valid dictionary

my_dict = {
  1: "Hello",
  (1, 2): "Hello Hi",
  3: [1, 2, 3]
}

print(my_dict)

# Invalid dictionary
# Error: using a list as a key is not allowed

my_dict = {
  1: "Hello",
  [1, 2]: "Hello Hi",
}

print(my_dict)