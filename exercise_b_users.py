# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)   /
# 2. Get Erik's hometown      /
# 3. Get the array of Erik's lottery numbers    /
# 4. Get the species of Avril's pet Monty   /
# 5. Get the smallest of Erik's lottery numbers   /
# 6. Return an array of Avril's lottery numbers that are even   /
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers /  
# 8. Change Erik's hometown to Edinburgh    /
# 9. Add a pet dog to Erik called "Fluffy"
# 10. Add another person to the users dictionary


users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}


# print(users["Jonathan"]["twitter"])

# print(users["Erik"]["home_town"])

# print(users["Erik"]["lottery_numbers"])

# print(users["Avril"]["pets"][0]["species"])

# print(min(users["Erik"]["lottery_numbers"]))

# print(users["Avril"]["lottery_numbers"])

# avril_lottery = []

# for number in users["Avril"]["lottery_numbers"]:
#   if (number % 2 == 0):
#     print(number, end = " ")
    

# users["Erik"]["lottery_numbers"].append(7)

# users["Erik"]["hometown"] = "Edinburgh"

# print(users["Erik"])

# users["Erik"]["pets"].append({"name": "Fluffy", "species": "dog"})


# print(users["Erik"]["pets"])


"Shaggy" = {
    "twitter": "scooby",
    "hometown": "spookyville",
    "pets": [
      {"name": "Scooby Doo", "species": "dog"}
    ]
}



# users["Shaggy"] = [
#   ["twitter"] = "scooby"
# ]
# print(users)