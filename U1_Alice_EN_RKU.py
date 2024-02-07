# THE TASK DESCRIPTION:

# Write a script in Python that opens the file alice.txt (Alice’s Adventures in Wonderland by Lewis Carroll) and calculates the frequency of all characters:
# ● Treat uppercase letters as lowercase.
# ● Ignore spaces and newline characters.

# As output, the program must create a file, which should be identical to the sample output ukol1_output_vzor.json
# ● The file ukol1_output.json is in JSON format.
# ● It contains a dictionary where keys are characters and values are their frequencies.
# ● Optional: the dictionary is sorted by keys.
#--------------------------------



#Import all the necessary modules
import json

#Load the text file with read method, lower all the characters, replace newline or space (whitespaces) with '' (= nothing), since we don't want to count them
with open("alice.txt", encoding = 'utf-8') as file:
    alice = (((file.read()).lower()).replace('\n', '')).replace(' ','')

#create a list of all characters called 'all_chars' using for cycle
all_chars=[]
for char in alice:
    all_chars.append(char) 

#for later alphabetical sorting purposes it is convenient to sort all the characters now
all_chars.sort()

#create a dictionary of letter frequencies
frequencies={}
#if the element (character) is already in my dictionary as a key, we add +1 to our counter (value)
#if the element (character) isn't in the dictionary as a key yet, we create it and assign 1 occurence as the value
for element in all_chars:
    if element in frequencies:
        frequencies[element] += 1
    else:
        frequencies[element]= 1

# we dump the dictionary to a json file, for nice formatting as in pprint we use indent=4
with open ("ukol_1_EN.json", mode='w', encoding = 'utf-8') as outfile:
    json.dump(frequencies,outfile, ensure_ascii=False, indent=4)



