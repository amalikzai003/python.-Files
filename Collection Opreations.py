scores = [85, 72, 90, 55, 68, 45, 78, 90, 60, 95]
print(scores)

minimum = min(scores)
maximum = max(scores)
average = sum(scores)/ len(scores)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)

passed_scores = [score for score in scores if score >= 60]

print(passed_scores)

score_set = set(scores)

print(score_set)

students = {
    101:  "Ahmad",
    102:  "Ali",
    103:  "Omid",
    104:  "Hamid",
    105:  "Farid"
}

print(students)

students_id = 103

print(students[students_id])

names = ["Ahmad", "Ali", "Omid", "Hamid", "Farid"]
scores = [85, 72, 90, 55, 68]

records = list(zip(names, scores))

print(records)

sorted_records = sorted(records, key=lambda record: record[1])

print(sorted_records)

for index, record in enumerate(records, start=1):
    print(index, record)

student_ids = [101, 102, 103, 104, 105]
names = ["Ahmad", "Ali", "Omid", "Hamid", "Farid"]
scores = [85, 72, 90, 55, 68]

records = list(zip(student_ids, names, scores, ))

print(records)