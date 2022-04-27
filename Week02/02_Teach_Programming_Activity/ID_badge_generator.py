print("Please enter the following information: \n")
first_name = input("First name: ")
last_name = input("Last name: ")
email_address = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job Title: ")
ID_number = input("ID Number: ")

#extra stuff for strech challenge -------------------------------->
hair = input("Hair color: ")
eye_color = input("Eye color: ")
get_month = input("Enter month (ex.'January'): ")
get_training = input("Did you complete the training? yes/no: ")
#----------------------------------------------------------------->
print()
print("The ID Card is:")
print("----------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.title()}")
print(f"ID: {ID_number}")
print()
print(f"{email_address.lower()}")
print(f"{phone_number}")
print()

# this is also the extra stuff for strech challenge -------------->
print(f"{'Hair: ' + hair:<20} Eyes: {eye_color}")
print(f"{'Month: ' + get_month:<20} Training: {get_training}")
print("----------------------------------------")
