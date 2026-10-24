"""break exits a loop, continue skips to its next iteration, and pass does nothing.
match compares a value against patterns and runs the first matching case.
"""

# Topic 42: break, continue, pass, and match

for number in range(1, 6):
    if number == 2:
        continue  # Skip this iteration.
    if number == 5:
        break  # Stop the loop.
    print("Loop value:", number)

if False:
    pass  # A placeholder statement that does nothing.

command = "start"
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
