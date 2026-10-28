def grade_statistics(students):
    grades = [student["G3"] for student in students]
    return {
        "max": max(grades),
        "min": min(grades),
        "avg": round(sum(grades) / len(grades),2),
        "total": len(students),
        "fields": len(students[0])
    }