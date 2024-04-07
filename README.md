# CPSC 2030 (Lab_09)

Tuesday, March 26th

**Due**: By the end of the day (Tuesday, April 9th)

**Instructions**  
For this lab, you will gain additional exposure to exceptions and serialization in Python (as well as working with .gitignore and debug configurations). I have provided you with starter code in `grades_processing.py` + `grades_reviewing.py`. You should ensure that the steps outlined below for the processing file are satisfied before moving to the reviewing phase.

You should satisfy the following requirements:
- Processing (`grades_processing.py`)
  - Implement the `process_grade()` function for the `Student` class.
    - This should calculate and return the average of the values in `self.grades`.
    - Use a try-except statement to capture invalid input with a `ValueError` exception block, print an informative statement, and return None.
  - Implement the `read_csv_data()` function.
    - This should accept a file path and use a context manager (i.e. `with open()`)
    - Use a try-except statement to capture invalid input for a file that does not exist and print an informative statement.
    - Returns a list of a list of strings.
  - Implement the steps for data processing
    - Once the csv file is read, we will have a list of all students in the `students` list. 
    - The `mode` variable is keyed off args passed in from the `launch.json` file. (If you are not using VS Code, you will need to manually modify the `mode` function from None to `review` and then `probation`.)
    - If the mode is review, iterate over all students and append each instance of the Student class to the `for_review` list if the student has an average grade of None.
    - If the mode is probation, iterate over all students and append the ID + Average properties as a dictionary to the `academic_probation` list, if the student has an average grade below 50 and the `is_improving` property is False.
  - Implement the steps for data export
    - If the mode is review, export the `for_review` variable to the identified JSON file (`for_review.json`).
    - If the mode is probation, export the `academic_probation` variable to the identified JSON file (`academic_probation.json`).
    - If the mode is anything else, export the entire collection of students to the identified pkl file (`all_students.pkl`).
- Reviewing (`grades_reviewing.py`)
  - Implement the `read_pkl_data()` function that returns a list of instances of the Student class from the identified file (`all_students.pkl`).
    - Use a try-except statement to capture invalid input for a file that does not exist and print an informative statement.
  - Implement the `read_json_data()` function that returns a list of float numbers from the identified file (`academic_probation.json`).
    - The academic probation file contains student IDs and grade averages. We want to extract only the grade average in this function. 
    - Use a try-except statement to capture invalid input for a file that does not exist and print an informative statement.
- .gitignore
  - The current gitignore file is set to ignore CSV files in any commits.
  - Modify this file so that it also ignores any output files (.json and .pkl) that are created in this lab. 
