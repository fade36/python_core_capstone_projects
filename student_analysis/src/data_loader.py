import csv


def load_data(path):
    selected_columns = [
        "school",
        "sex",
        "age",
        "address",
        "studytime",
        "failures",
        "schoolsup",
        "internet",
        "absences",
        "G1",
        "G2",
        "G3",
    ]

    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")

        students = []

        for row in reader:
            student = {
                column: row[column]
                for column in selected_columns
            }
            students.append(student)

    return students
