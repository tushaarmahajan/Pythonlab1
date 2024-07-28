# Given dictionary of people
people = [
    {"name": "John Doe", "age": 30, "blood": "A+"},
    {"name": "Jane Smith", "age": 25, "blood": "B-"},
    {"name": "Emily Davis", "age": 40, "blood": "O+"},
    {"name": "Michael Brown", "age": 35, "blood": "AB-"},
    {"name": "William Johnson", "age": 28, "blood": "A-"},
    {"name": "Ema Wilson", "age": 22, "blood": "B+"},
    {"name": "Oliver Martinez", "age": 33, "blood": "O-"},
    {"name": "Sophia Anderson", "age": 27, "blood": "AB+"},
    {"name": "James Thomas", "age": 45, "blood": "A+"},
    {"name": "Isabella Lee", "age": 38, "blood": "B-"}
]

# Print each person's information
for person in people:
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"Blood Group: {person['blood']}")
    print("-" * 20)
