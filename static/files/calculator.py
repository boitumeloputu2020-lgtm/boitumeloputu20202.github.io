Number_1 = float(input("Enter the first number: "))
Number_2 = float(input("Enter the second number: "))
if Number_2 == 0:
        print("ERROR!")
else:
        sum = Number_1 + Number_2 
        difference = Number_1 - Number_2
        multiplication = Number_1 * Number_2
        division = Number_1 / Number_2
        floor_division = Number_1 // Number_2
        modulus = Number_1 % Number_2
        print(f"Sum: {round(sum, 2)}")
        print(f"Difference: {round(difference,2)}")
        print(f"Muliplication: {round(multiplication,2)}")
        print(f"Division: {round(division,2)}")
        print(f"Floor division: {round(floor_division,2)}")
        print(f"Modulus: {round(modulus,2)}")


