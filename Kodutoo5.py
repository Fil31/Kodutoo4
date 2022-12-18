#harjutus 1
postal_index = input("Enter the postal index: ")

if isinstance(postal_index, str) and len(postal_index) == 5:
  postal_index_list = list(postal_index)

  first_digit = postal_index_list[0]

  if first_digit == "1":
    print("The postal index belongs to Tallinn.")
  elif first_digit == "2":
    print("The postal index belongs to Narva or Narva-Jõesuu.")
  elif first_digit == "3":
    print("The postal index belongs to Kohtla-Järve.")
  elif first_digit == "4":
    print("The postal index belongs to Ida-Virumaa, Lääne-Virumaa, or Jõgevamaa.")
  elif first_digit == "5":
    print("The postal index belongs to Tartu linn.")
  elif first_digit == "6":
    print("The postal index belongs to Tartumaa, Põlvamaa, Võrumaa, or Valgamaa.")
  elif first_digit == "7":
    print("The postal index belongs to Viljandimaa, Järvamaa, Harjumaa, or Raplamaa.")
  elif first_digit == "8":
    print("The postal index belongs to Pärnumaa.")
  elif first_digit == "9":
    print("The postal index belongs to Läänemaa, Hiiumaa, or Saaremaa.")
  else:
    print("Invalid postal index.")
else:
  print("Invalid postal index.")

if first_digit in ["1", "2", "3"]:
  print("Stay home!")
else:
  print("Wear masks!")

#harjutus 2
list2 = input ("Enter numbers: ")

original_list = list(list2)

num_items = int(input("Enter the number of items to swap: "))

if num_items >= 2:
  for i in range(num_items // 2):
    original_list[i], original_list[-(i+1)] = original_list[-(i+1)], original_list[i]

print(original_list)

#harjutus 4
name = input("Please enter your name: ")

if name.isalpha():
  print(f"Hello, {name.capitalize()}!")

  num_letters = len(name)
  print(f"Your name has {num_letters} letters.")

  num_vowels = 0
  num_consonants = 0
  for letter in name:
    if letter in "aeiouAEIOU":
      num_vowels += 1
    else:
      num_consonants += 1
  print(f"Your name has {num_vowels} vowels and {num_consonants} consonants.")

  sorted_name = sorted(set(name.lower()))
  print(f"Your name in alphabetical order is: {''.join(sorted_name)}")
else:
  print("Please enter a name with only letters.")
  
#Harjutus 5
def pad_strings(strings):
    longest = max(strings, key=len)
    padded_strings = [s.ljust(len(longest), '_') for s in strings]
    return padded_strings

strings = ["крот", "белка", "выхухоль"]
padded_strings = pad_strings(strings)
print(padded_strings)  

strings = ["a", "aa", "aaa", "aaaa", "aaaaaa"]
padded_strings = pad_strings(strings)
print(padded_strings)  

strings = ["qweasdqweas", "q", "rteww", "ewqqqqq"]
padded_strings = pad_strings(strings)
print(padded_strings) 

#harjutus 6
name = input("Please enter your name: ")

if name.isalpha():
  print(f"Hello, {name.capitalize()}!")

  num_letters = len(name)
  print(f"Your name has {num_letters} letters.")

  num_vowels = 0
  num_consonants = 0
  for letter in name:
    if letter in "aeiouAEIOU":
      num_vowels += 1
    else:
      num_consonants += 1
  print(f"Your name has {num_vowels} vowels and {num_consonants} consonants.")

  sorted_name = sorted(set(name.lower()))
  print(f"Your name in alphabetical order is: {''.join(sorted_name)}")
else:
  print("Please enter a name with only letters.")
