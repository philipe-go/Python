#first lesson about printing the Hello World
print("\n1st Lesson")

print("Hello World")

#second lesson about drawing a shape
print("\n2nd Lesson")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#third lesson about variables and data types 
print("\n3rd Lesson")

character_name = "George"
character_age = 70
print("There once was a man named",character_name)
print("He was",character_age,"years old")
print("He really liked the name",character_name)
print("but did not like being",character_age)

character_age = character_age - 20
print("So he changed his age to",character_age)

#fourth lesson about strings and framework string functions
print("\n4th Lesson")

print("There once was a man named",character_name, "\nHe was",character_age,"years old")

phrase = "Philipe Gouveia"
print(phrase.upper())
print("Is lower case?",phrase.lower().isupper())
print("Has",len(phrase),"characters")

index = 5
print("its",index,"th character is",phrase[index])
character = "G"
print("The letter",character,"has the index of",phrase.index(character))
print(phrase.replace("Philipe","Pedro").upper())

#fifth lesson about using numbers data type
my_firstnum = 5
my_secondnum = 7.55
print("\n")
print(my_firstnum-my_secondnum)
print (my_firstnum % my_secondnum)

print(str(my_firstnum),"my favorite number")

print(abs(my_firstnum-my_secondnum))

my_secondnum = 2
print(pow(my_firstnum,my_secondnum))

from math import * #library import
print(sqrt(121))

#sixth lesson about getting input from user
print("\n");
user_name = input("Enter your name: ");
print(user_name,"is a beautiful name.");

#seventh lesson about building a calculator
print("\n")
num1 = input("enter a number:")
num2 = input("enter another number:")
result = float(num1)+float(num2)
print("The sum of the numbers is:",result)

#eighth lesson about building a madlibs game
print("\n")
color = input("enter a color: ")
plural_noum = input("enter a plural noum: ")
celebrity = input("enter a celebrity: ")
print("\nroses are", color)
print(plural_noum,"are blue")
print("I love",celebrity)

#nineth lesson


