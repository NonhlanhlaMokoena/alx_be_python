#Weather Recommendation Program. This script will ask the user about the current weather conditions and provide clothing recommendations based on the input.

#Step 1: Prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

#Step 2: Provide clothing recommendations and output
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
      