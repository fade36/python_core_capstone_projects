def main_menu(students):
    print("=" * 55)
    print("Student Perfomance Analyzer".center(55))
    print("=" * 55)
    print()
    print("-"*22 + " Main Menu " + "-"*22)
    print()
    print("1. Show Dataset overview")
    print("2. Show student information")
    print("3. Analyze grades")
    print("4. Find top students")
    print("5. Filter students")
    print("6. Analyze study habits")
    print("7. Export results")
    print("0. Exit")
    print()
    print("-"*55)

def menu_1(stats):
    if stats is None:
        print("No student data available.")
        return
    print(f"Total students: {stats['total']}")
    print(f"Columns available: {stats['fields']}")
    print(f"Average final grade: {stats['avg']}")
    print(f"Highest final grade: {stats['max']}")
    print(f"Lowest final grade: {stats['min']}")

def show_grade_averages(avgs):
    if avgs is None:
        print("No student data availeble")
        return
    for grade, average in avgs.items():
        print(f"Average {grade}: {average}")

def show_tops(tops):
    for index, student in tops:
        print(f"Student #{index} : ({student['G3']},{student['G2']},{student['G1']})")

def menu_5():
    print("="*55)
    print("1. Filter by school")
    print("2. Filter by age")
    print("3. Filter by study time")
    print("4. Filter by final grade")
    print("="*55)

def result_menu_5(count, indexes):
    if count == 0:
        print("-"*55)
        print("There is no matches!")
        print("-"*55)
        return
    for index in indexes:
        print(f"Student #{index} matches!")

def menu_6():
    print("="*19 + " Analyze Habits " + "="*20)
    print("1. Compare study time with final grades")
    print("2. Compare absences with final grades")
    print("3. Compare previous failures with final grades")
    print("4. Compare school support with final grades")
    print("5. Compare internet access with final grades")
    print("0. Back to menu")
    print("="*55)

def result_menu_6_1(grades):
    print("=" *17 + " StudyTime Analysis " + "="*18)
    print()
    for i in range(1,5):
        if i == 1:
            print("Study time: < 2 hours/week")
        elif i == 2:
            print("Study time: 2-5 hours/week")
        elif i == 3:
            print("Study time: < 5-10 hours/week")
        else:
            print("Study time: 10+ hours/week")
        print(f"Students: {len(grades['group'+str(i)])}")
        if len(grades['group'+str(i)]) == 0:
            print()
            continue
        print(f"Average final grade: {round(sum(grades['group'+str(i)]) / len(grades['group'+str(i)]),2)}")
        print(f"Minimum grade: {min(grades['group'+str(i)])}")
        print(f"Maximum grade: {max(grades['group'+str(i)])}")
        print()

def result_menu_6_235(dictionary, field):
    print("=" *18 + f" {field} analysis " + "="*18)
    for key in dictionary:
        print(f"{field}: {key}, Final avg grade: {dictionary[key][0]}, Student count: {dictionary[key][1]}")
    print("=" *55)

def result_menu_6_4(schoolsup_avg):
    print("=" *15 + " School Support Analysis " + "="*15)
    for yes_no in schoolsup_avg:
        print(f"School support: {yes_no}, Final avg grade: {schoolsup_avg[yes_no][0]}, Student count: {schoolsup_avg[yes_no][1]}")
    print("=" *55)
