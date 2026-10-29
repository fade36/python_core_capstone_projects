def grade_statistics(students):
    if not students:
        return None
    grades = [student["G3"] for student in students]
    return {
        "max": max(grades),
        "min": min(grades),
        "avg": round(sum(grades) / len(grades),2),
        "total": len(students),
        "fields": len(students[0])
    }

def get_student(students, index):
    if index < 0 or index >= len(students) or not students :
        return None
    return students[index]

def get_avg(students):
    if not students:
        return None
    return {
        "G1": round(sum((student["G1"] for student in students)) / len(students),2),
        "G2": round(sum((student["G2"] for student in students)) / len(students),2),
        "G3": round(sum((student["G3"] for student in students)) / len(students),2)
    }


def top_ten(students):
    tops = sorted(
        enumerate(students),
        key = lambda pair: (pair[1]["G3"], pair[1]["G2"], pair[1]["G1"]),
        reverse=True
    )[:10]

    for index, student in tops:
        print(f"Student #{index} : ({student['G3']},{student['G2']},{student['G1']})")
    

def filter_students(students, filters):
    if not filters or not students:
        return None 
    count=0
    for index, student in enumerate(students):
        matches = True
        for filter in filters:
            if filters[filter] != student[filter]:
                matches = False
                break
        if(matches):
            print(f"Student #{index} matches!")
            count+=1
    if count == 0:
        print("-"*55)
        print("There is no matches!")
        print("-"*55)

def studytime_to_finalGrade(students):
    #where:
    #  group1 -> student`s studytime from [0,2]
    #  group2 -> student`s studytime from (2,5]
    #  group3 -> student`s studytime from (5,10]
    #  group4 -> student`s studytime 10+ hours

    grades = {}
    grades["group1"] = []
    grades["group2"] = []
    grades["group3"] = []
    grades["group4"] = []
    for index,student in enumerate(students):
        if 0 <= student["studytime"] <= 2:
            grades["group1"].append(student["G3"])
        elif 2 < student["studytime"] <= 5:
            grades["group2"].append(student["G3"])
        elif 5 < student["studytime"] <= 10:
            grades["group3"].append(student["G3"])
        else:
            grades["group4"].append(student["G3"])
    return grades


