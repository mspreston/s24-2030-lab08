# original dataset retrieved from https://github.com/kvinlazy/Dataset/blob/master/grades.csv
# modified with certain perturbations

import csv, json, pickle, random, sys

class Student:
    def __init__(self, id, grades):
        self.id = id
        self.grades = grades
        self.average = self.process_grade()
        self.is_improving = self.grades[1] < self.grades[3] and self.grades[3] < self.grades[5]

    def process_grade(self) -> float:
        pass

def read_csv_data(file_path) -> list[list[str]]:
    pass

if __name__ == "__main__":
    # Only `grades.csv` is a valid option, but your code should use exceptions to prevent the program from crashing
    # Do not modify code below this line -- only add where pass statements are present
    students = []
    filenames = ["grades.csv", "missing.csv", "answers.csv"]
    data = []

    while (len(data) == 0):
        filename = random.choice(filenames)
        data = read_csv_data(filename)
    
    for entry in data:
        students.append(Student(entry[0], entry[1:]))

    # Data Processing
    mode = None
    if (len(sys.argv) > 1):
        mode = sys.argv[1]
    
    if mode == "review":
        pass
    elif mode == "probation":       
        pass

    # Data Export
    if mode == "review":
        json_file = "for_review.json"

        pass
    elif mode == "probation":
        json_file = "academic_probation.json"
        pass
    else:
        pickle_file = "all_students.pkl"
        pass        
        