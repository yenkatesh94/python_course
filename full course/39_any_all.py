"""any() checks whether at least one item is true; all() checks whether every item is true.
Generator expressions let these functions test conditions without building another list.
"""

# Topic 39: any() and all()

scores = [78, 92, 64, 88]

# any() is True if at least one item passes the condition.
has_high_score = any(score >= 90 for score in scores)
print("Is there a score of 90 or higher?", has_high_score)

# all() is True only if every item passes the condition.
all_scores_pass = all(score >= 50 for score in scores)
print("Did every student pass?", all_scores_pass)
