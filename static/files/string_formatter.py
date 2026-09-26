first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio_message = input("Write a short bio message: ").strip()
user_name = f"{first_name[0]}{last_name}"
full_name = first_name.title() +" "+ last_name.title()
number_of_characters = len(f"{bio_message}")

print(f"Full name: {full_name}")
print(f"Your user name is: {user_name.lower()}")
print(f"{bio_message.replace("I am", "I'm")}")
print(f"Number of characters: {number_of_characters}")
