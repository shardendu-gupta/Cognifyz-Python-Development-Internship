temperature = float(input("Enter temperature: "))

con = input("Convert to (C/F): ").upper()

if con == "C":
    c = (temperature - 32) * 5 / 9
    print(f"Temperature in Celsius: {c:.2f}°C")

elif con == "F":
    f = (temperature * 9 / 5) + 32
    print(f"Temperature in Fahrenheit: {f:.2f}°F")

else:
    print("Invalid choice! Please enter C or F.")
