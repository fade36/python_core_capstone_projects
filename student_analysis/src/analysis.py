def grade_statistics(students):
    if not students:
        return None
    grades = [student["G3"] for student in students]
    return {
        "total": len(students),
        "fields": len(students[0]),
        "max": max(grades),
        "min": min(grades),
        "avg": round(sum(grades) / len(grades),2)
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
        enumerate(students,start=1),
        key = lambda pair: (pair[1]["G3"], pair[1]["G2"], pair[1]["G1"]),
        reverse=True
    )[:10]

    result = []

    for rank,(student_number, student) in enumerate(tops,start = 1):
        result.append({
            "rank": rank,
            "student_number": student_number,
            "G1": student["G1"],
            "G2": student["G2"],
            "G3": student["G3"]
        })

    return result

def filterr(students,filters):
    if not filters or not students:
        return None 
    students = list(enumerate(students))
    for filter in filters:
        filtered_students = []
        for i in range(len(filters[filter])):
            for index,student in students:
                if filters[filter][i] == student[filter]:
                    filtered_students.append((index,student))
        students = filtered_students
    return students 

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
    for student in students:
        if student["studytime"] == 1:
            grades["group1"].append(student["G3"])
        elif student["studytime"] == 2:
            grades["group2"].append(student["G3"])
        elif student["studytime"] == 3:
            grades["group3"].append(student["G3"])
        else:
            grades["group4"].append(student["G3"])

    result = {}

    for grade in grades:
        if not grades[grade]:
            result[grade] = {
                "Students": 0,
                "Average final grade": None,
                "Minimum grade": None,
                "Maximum grade": None
            }
            continue

        count = len(grades[grade])
        summ = sum(grades[grade])
        minimum = min(grades[grade])
        maximum = max(grades[grade])

        result[grade] = {
            "Students": count,
            "Average final grade": round(summ / count, 2),
            "Minimum grade": minimum,
            "Maximum grade": maximum
        }

    return result

def continuous_field(students,field):
    nums = []
    for student in students:
        if student[field] not in nums:
            nums.append(student[field])
    result = {}
    for num in nums:
        result[num] = {}
        count = 0
        sum = 0
        for student in students:
            if student[field] == num:
                count+=1
                sum+=student["G3"]
        result[num] = {
            "Average": round(sum/count,2),
            "Student count": count
        }

    result = dict(sorted(result.items(), key = lambda group: group[1]["Student count"], reverse=True))

    return result

def discrete_field(students, field):
    
    result = {}
    count_yes = 0
    sum_yes = 0
    count_no = 0
    sum_no = 0
    for student in students:
        if student[field] == "yes":
            count_yes+=1
            sum_yes+=student["G3"]
        else:
            count_no+=1
            sum_no+=student["G3"]

    result["yes"] = {
        "Average": round(sum_yes/count_yes,2)  if count_yes > 0 else None,
        "Student count": count_yes
    }
    result["no"] = {
            "Average": round(sum_no/count_no,2)  if count_yes > 0 else None,
            "Student count": count_no
        }

    return result 