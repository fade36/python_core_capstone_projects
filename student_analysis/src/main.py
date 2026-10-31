from data_loader import load_data
from time import sleep
import menu
import analysis
import exporter

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
                menu.menu_1(stats)
                print("-"*55)
                while input("Type 0 to go back: ") != "0":
                    print("-"*55)
                    menu.menu_1(stats)
                    print("-"*55)
            case "2":
                try:
                    index = int(input("Student number: "))
                    student = analysis.get_student(students, index-1)
                    print(student)
                    opt = int(input("Type Student number or '0' to go back: "))
                    while opt != 0:
                        print("-"*55)
                        student = analysis.get_student(students, opt-1)
                        print(student)
                        print("-"*55)
                        opt = int(input("Type Student number or '0' to go back: "))
                except:
                    print("Not a number")
            case "3":
                avgs = analysis.get_avg(students)
                menu.show_grade_averages(avgs)
                print("-"*55)
                while input("Type 0 to go back: ") != "0":
                    print("-"*55)
                    menu.show_grade_averages(avgs)
                    print("-"*55)
            case "4":
                tops = analysis.top_ten(students)
                menu.show_tops(tops)
                print("-"*55)
                while input("Type 0 to go back: ") != "0":
                    print("-"*55)
                    menu.show_tops(tops)
                    print("-"*55)
            case "5":
                menu.menu_5()
                filters = {}
                choice = input("Select filter (0 to finish): ")   
                while choice != "0":
                    if choice == "1":
                        if "school" not in filters:
                            filters["school"] = []
                        filters["school"].append(input("Type school: "))
                        print("-"*55) 
                    elif choice == "2":
                        if "age" not in filters:
                            filters["age"] = []
                        filters["age"].append(int(input("Type age: ")))
                        print("-"*55)  
                    elif choice == "3":
                        if "studytime" not in filters:
                            filters["studytime"] = []                        
                        filters["studytime"].append(int(input("Type studytime: ")))
                        print("-"*55)  
                    elif choice == "4":
                        if "G3" not in filters:
                            filters["G3"] = []
                        filters["G3"].append(int(input("Type final grade: ")))
                        print("-"*55)  
                    else:
                        print("invalid option")
                        print("-"*55)  
                    choice = input("Select filter (0 to finish): ")
                filtered_students = analysis.filterr(students,filters)
                print("-"*55) 
                menu.result_menu_5(filtered_students)
            case "6":
                while True:
                    menu.menu_6()
                    option = input("Select option: ")
                    if option == "0":
                        break
                    match option:
                        case "1":
                            grades = analysis.studytime_to_finalGrade(students)
                            menu.result_menu_6_1(grades)
                        case "2":
                            absence_avg = analysis.continuous_field(students, "absences")
                            menu.result_menu_6_235(absence_avg, "Absences")
                        case "3":
                            failures_avg = analysis.continuous_field(students, "failures")
                            menu.result_menu_6_235(failures_avg, "Failures")
                        case "4":
                            schoolsup = analysis.discrete_field(students, "schoolsup")
                            menu.result_menu_6_4(schoolsup)
                        case "5":
                            internet = analysis.discrete_field(students, "internet")
                            menu.result_menu_6_235(internet, "Internet")
                        case _:
                            print("Invalid option")
                            continue
                    print("-"*55)
                    result_option = input("Type '0' to go back: ")
                    print("-"*55)
                    while result_option != "0":
                        print("Invalid option")
                        result_option = input("Type '0' to return to Analysis menu: ")
            case "7":
                summary = {
                    "dataset_overview": analysis.grade_statistics(students),
                    "average_grade": analysis.get_avg(students),
                    "top_students": analysis.top_ten(students),
                    "study_time/final_grade": analysis.studytime_to_finalGrade(students),
                    "absences/final_grade": analysis.continuous_field(students, "absences"),
                    "failures/final_grade": analysis.continuous_field(students, "failures"),
                    "schoolsup/final_grade": analysis.discrete_field(students, "schoolsup"),
                    "internet/final_grade": analysis.discrete_field(students, "internet")
                }
                exporter.json_export("data/data.json", summary)
            case _:
                print("Invalid option")

            

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
