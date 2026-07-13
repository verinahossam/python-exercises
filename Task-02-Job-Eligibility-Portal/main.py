# Job Eligibility Portal

# Welcome Message
message = "Welcome to the Job Eligibility Portal"
print(message.center(50))

# Get Applicant Information
python_skill = input("Do you know Python? (yes/no): ").strip().lower()
experience = int(input("Enter your years of experience or number of projects: ").strip())
education = input(
    "Do you have a Computer Science degree or Bootcamp certificate? (yes/no): "
).strip().lower()

# Check Eligibility
is_eligible = python_skill == "yes" and (
    experience >= 2 or education == "yes"
)

# Display the Result
print(" Job Eligibility ".center(40, "="))

if is_eligible:
    print("Congratulations! You have been accepted to the next interview stage.")
else:
    print("Sorry, your current qualifications do not match the job requirements.")
