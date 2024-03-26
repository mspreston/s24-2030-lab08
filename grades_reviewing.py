# original dataset retrieved from https://github.com/kvinlazy/Dataset/blob/master/grades.csv
# modified with certain perturbations

import json, pickle, sys
from grades_processing import Student

def read_json_data(file_path) -> list[float]:
    pass

def read_pkl_data(file_path) -> list["Student"]:
    pass

if __name__ == "__main__":
    file_name = sys.argv[1]

    # Task 1:
    if "json" in file_name:
        data = read_json_data(file_name)

        print(f"The lowest grade average is {round(min(data),2)}.")
        print(f"The mean grade average is {round(sum(data)/len(data),2)}.")
        print(f"The highest grade average is {round(max(data),2)}.")
    elif "pkl" in file_name:
        all_students = read_pkl_data(file_name)
        grade_dict = {"A": 0, "B": 0, "C": 0, "D": 0}

        for student in all_students:
            avg = student.average

            if avg is None:
                continue
            elif avg > 90:
                grade_dict["A"] += 1
            elif avg > 80:
                grade_dict["B"] += 1
            elif avg > 70:
                grade_dict["C"] += 1
            elif avg > 60:
                grade_dict["D"] += 1
        
        print(f"Grade Distribution: {grade_dict['A']} A, {grade_dict['B']} B, {grade_dict['C']} C, and {grade_dict['D']} D.")
    else:
        print("File Type Not Supported")
        exit
    