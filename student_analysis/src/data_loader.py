import csv

def load_data(path):
    selected_columns = [
        "school","sex","age","address","studytime","failures",
        "schoolsup","internet","absences","G1","G2","G3"
    ]

    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")

        students = []

        for row in reader:
            student = {}

            for column in selected_columns:
                if column in row:
                    if row[column].isdigit():
                        student[column] = int(row[column])
                    else:
                        student[column] = row[column]
            students.append(student)

    return students