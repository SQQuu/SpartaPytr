print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a: for number in x[:5]:
#     print(number)



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b: for number in x:
#     if number % 2 == 0:
#         print(number)



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c: for number in x[:5]:
#     if number % 2 == 0:
#         print(number)


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a: first_letter = [name.split()[0][0] for name in names]
# print(name)= wrong  correct = print(first_letters)




print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:index_space = [in_spce.index(' ',0) for in_spce in names]
# print(index_space)




print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c: first_last = [name.split()[0][0] + name.split()[1][0] for name in names]
# print(first_last)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a: for no_dupes in list_of_lists:
#     if len(no_dupes) == len(set(no_dupes)):
#         print(no_dupes)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a: number = 0
# while number < 100:
#     if number >= 100:
#         print("Congratulations, this is a number greater than or equal to 100.")
#     else:
#         print(f"Unsatisfactory value {number} given.")


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b: Not fully confident, this is not my answer
# def is_prime(n):
# if n <= 1:
# return False  # Numbers less than or equal to 1 are not prime
# for i in range(2, int(n**0.5) + 1):
# if n % i == 0:  # If the number is divisible by i, it's not prime
# return False
# return True
#if is_prime(number):
#    print("The number is prime.")
#else:
#    print("The number is not prime.")