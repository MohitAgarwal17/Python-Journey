# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

# A match statement takes an expression and compares its value to successive patterns
# given as one or more case blocks. Specifically, pattern matching operates by:
# 1. using data with type and shape (the subject)
# 2. evaluating the subject in the match statement
# 3. comparing the subject with each pattern in a case statement from top to bottom until a match is confirmed.
# 4. executing the action associated with the pattern of the confirmed match
# If an exact match is not confirmed, the last case, a wildcard _,
# if provided, will be used as the matching case. If an exact match is not confirmed
# and a wildcard case does not exist, the entire match block is a no-op.

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Monday"))