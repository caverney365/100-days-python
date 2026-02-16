student_scores = [180, 124, 165, 173, 189, 169, 146]

total_score = sum(student_scores)

highest = student_scores[0]
for score in student_scores:
    if score > highest:
        highest = score

print(highest)