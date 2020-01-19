import emoji
import pyfiglet

banner = pyfiglet.figlet_format("Hello there!")
print(banner)

print("Welcome to the Body Mass Index Calculator!\n")

weight = int(input("What is your weight in pounds? "))
inches = int(input("What is your height in inches? "))
bmi = (703 * weight) / (inches ** 2)

if bmi < 18.5:
    your_emoji = emoji.emojize(":thumbs_down:")
elif bmi >= 18.5 and bmi <= 24.9:
    your_emoji = emoji.emojize(":thumbs_up:")
elif bmi >= 25 and bmi <= 29.9:
    your_emoji = emoji.emojize(":thumbs_down:")
else:
    your_emoji = emoji.emojize(":thumbs_down:")

print("\nBMI Calculations:\n\nUnderweight: BMI < 18.5\nNormal weight: BMI 18.5 - 24.9\nOverweight: BMI 25 - 29.9\nObesity: BMI > 30")

print(f"\nYour BMI is {bmi:.2f} {your_emoji}")

input("\nPress any button to exit.")
