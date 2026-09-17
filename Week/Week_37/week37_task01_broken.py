

def calculate_grade_stats(studentlist,passthreshold=50):
    total_Score = 0
    passed_students = []

    for s in studentlist:
        score = float(s['score'])

        if score >= passthreshold:
            passed_students.append(s['name'])

        total_Score += score

    if len(studentlist) > 0:
        avg = total_Score / len(studentlist)
    else: 
        avg = 0.0
        
    return { 
    'average':avg,
    'passed':passed_students, 
    'total_count':len(studentlist)
}
   

def print_summary(stats_dict, coursename="Python 101"):
    print("=== Summary for " + coursename + "===")
    print("Average Score: " + str(stats_dict['average']))
    print("Passed Students: " + ", ".join(stats_dict['passed']))

data = [
    {'name':'Charlie','score':'85.5'},
    {'name':'River','score':'42.0'},
    {'name':'Jordan','score':'68.0'}
]

res = calculate_grade_stats(data)
print_summary(res)
