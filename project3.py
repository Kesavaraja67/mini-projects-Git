import random
import time

OPERATOR = ["+", "-", "*"]
MIN_OPERATOR = 3
MAX_OPERATOR = 15
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    right = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    operator = random.choice(OPERATOR)

    expr = str(left) + " " + operator + " " + str(right)
    # if the python expressions are in strings it can be used to solve that expression
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press Enter to Start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("PROBLEM #" + str(i + 1) + " : " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("---------------------")
print("Congrats, You finished in", total_time, " Seconds!")
