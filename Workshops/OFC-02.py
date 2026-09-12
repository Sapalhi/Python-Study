# OFC-02 - Build an Employee Profile Generator
first_name = 'John'
last_name = 'Doe'

full_name = first_name + ' ' + last_name #Combining Names

address = '123 Main Street'
address += ', Apartment 4B' # Adding to the address string

employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_years = 5
# Using str() to convert experience_years to a string and joined with other strings
experience_info = 'Experience: ' + str(experience_years) + ' years' 
print(experience_info)

position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3] # Slicing the string to get the department code. 
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11] # Interval [9:11)
print(initials)
last_three = employee_code[-3:] # Negative indexing
print(last_three)
