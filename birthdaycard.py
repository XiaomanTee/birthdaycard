print("What's participant's name?")
participant_name = input()
print("Enter year of birth: ")
year_of_birth = int(input())
print("enter the current year: ")
current_year = int(input())
print("Enter personalized message: ")
personalized_message = input()
print("What's sender's name?")
sender_name = input()

age = current_year - year_of_birth

print(f"{participant_name}, let's celebrate your {age} years of awesomeness!\nWishing you a day filled with joy and laughter as you turn {age}!")
print(f"\n{personalized_message}\n")
print(f"With love and best wishes,\n{sender_name}")
