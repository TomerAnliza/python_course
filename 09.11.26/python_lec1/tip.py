bill = float(input("what is the bill?"))
tip_percentage = int(input("what is the tip percentage?"))
diners = int(input("how many diners?"))


total_tip = bill * tip_percentage / 100

tip_per_diner = total_tip / diners




print("Total tip:", total_tip)
print("Tip per diner:", tip_per_diner)


if tip_per_diner > 20:
    print("The tip per diner is greater than $20.")
elif tip_per_diner < 5:
    print("The tip per diner is less than $5.")
else:
    print("The tip per diner is between $5 and $20.")
