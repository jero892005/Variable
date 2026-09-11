query = input()

if query == "5 multiplied by 6":
    answer = 5 * 6

elif query == "8 divided by 3":
    answer = 8 / 3
    answer = round(answer, 8)

elif query == "8 divided by 3 without the remainder":
    answer = 8 // 3

elif query == "8 modulo 3 (remainder only)":
    answer = 8 % 3

elif query == "4200000 add 23090":
    answer = 4200000 + 23090

elif query == "4200000 subtract 7633":
    answer = 4200000 - 7633

else:
    answer = "Invalid input"

print("The answer to your query is:", answer)
print("Program written by Jeronimo Valencia")
