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
                menu.menu_1(students)
                while input("Type 0 to go back: ") != "0":
                    print("-"*55)
                    menu.menu_1(students)
                    print("-"*55)
            case "2":
                index = int(input("Student number: "))
                analysis.get_student(students, index-1)
                while input("Type 0 to go back: ") != "0":
                    print("-"*55)
                    analysis.get_student(students, index-1)
                    print("-"*55)
            case "3":
                analysis.get_avg(students)
                while input("Type 0 to go back: ") != "0":
                    print("-"*55)
                    analysis.get_avg(students)
                    print("-"*55)
            case "4":
                analysis.top_ten(students)
                while input("Type 0 to go back: ") != "0":
                    print("-"*55)
                    analysis.top_ten(students)
                    print("-"*55)
            case "5":
                menu.menu_5()
                filters = {}
                choice = input("Select filter (0 to finish): ")     
                while choice != "0":
                    if choice == "1":
                        filters["school"] = input("Type school: ")
                    elif choice == "2":
                        filters["age"] = int(input("Type age: "))
                    elif choice == "3":
                        filters["studytime"] = int(input("Type studytime: "))
                    elif choice == "4":
                        filters["G3"] = int(input("Type final grade: "))
                    else:
                        print("invalid option")
                    choice = input("Select filter (0 to finish): ")
                analysis.filter_students(students,filters)
            case "6":
                menu.menu_6()
                option = input("Select option: ")
                match option:
                    case "1":
                        grades = analysis.studytime_to_finalGrade(students)
                        menu.result_menu_6_1(grades)
            case _:
                print("Invalid option")

            

if __name__ == "__main__":
    main()
