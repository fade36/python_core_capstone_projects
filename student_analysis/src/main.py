from data_loader import load_data
from time import sleep
import menu
import analysis

def main():
    path = "data/student-mat.csv"
    students = load_data(path)

    while True:
        menu.main_menu(students)
        option = input("Choose an option: ")

        match option:
            case "0": 
                print("Exiting program...")
                sleep(1)
                break
            case "1":
                stats = analysis.grade_statistics(students)
                if stats is None:
                    print("No student data available.")
                    return
                print(f"Total students: {stats['total']}")
                print(f"Columns available: {stats['fields']}")
                print(f"Average final grade: {stats['avg']}")
                print(f"Highest final grade: {stats['max']}")
                print(f"Lowest final grade: {stats['min']}")
            case _:
                print("Invalid option")

            

if __name__ == "__main__":
    main()
