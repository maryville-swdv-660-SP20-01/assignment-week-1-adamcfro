# import dependencies
import emoji
import pyfiglet

# Create a banner that displays a welcome message
banner = pyfiglet.figlet_format("Hello there!")

print(f"{banner}\nWelcome to the Body Mass Index Calculator!\n")

# get weight and inches to compute BMI
weight = int(input("What is your weight in pounds? "))
inches = int(input("What is your height in inches? "))

bmi = (703 * weight) / (inches ** 2)

# if BMI is good give a thumbs up, otherwise give thumbs down
if bmi >= 18.5 and bmi <= 24.9:
    emoji_symbol = emoji.emojize(":thumbs_up:")
else:
    emoji_symbol = emoji.emojize(":thumbs_down:")

# display BMI calculations
print(
    f"\nBMI Calculations:\n\nUnderweight: BMI < 18.5\nNormal weight: BMI 18.5 - 24.9\nOverweight: BMI 25 - 29.9\nObesity: BMI > 30\nYour BMI is {bmi:.2f} {emoji_symbol}")

input("\nPress any button to exit.")
