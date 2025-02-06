number_of_students = int(input("Input the number of students that are registering: "))  # To request and accept from the user how many students are registering

text_file_name = "reg_form.txt"             

file_open = open(text_file_name, "w")       # To Open the file, redy to start writing

for i in range(number_of_students):         # To Loop for the number of students
    
    student_ID = input("Input the ID number of the student: ")   # To accept inputs from the user for student ID
   
    file_open.write(student_ID+"\n")         # To write the every entered student_ID to the opened text file
    
file_open.close()                            # To close the text file

print("\n The registration is completed, see the registration details - 'reg_form.txt'.")
