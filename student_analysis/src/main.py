from data_loader import load_data


def main():
    path = "data/student-mat.csv"
    students = load_data(path)

    print(f"Loaded students: {len(students)}")
    print(f"Selected columns: {len(students[0])}")
    print("Columns:", ", ".join(students[0].keys()))

    print("\nFirst student:")
    first_student = students[0]

    for column, value in first_student.items():
        print(f"{column}: {value}")


if __name__ == "__main__":
    main()
