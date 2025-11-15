#!/usr/bin/env python3

"""Weather Recommendation Program"""

user_selection = input("What's the weather like today? (sunny/rainy/cold):");

if user_selection == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_selection == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user_selection == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")