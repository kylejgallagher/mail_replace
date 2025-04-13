#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as names:
    content = names.read().splitlines()

# with open("Input/Names/invited_names.txt") as names:
#     content = names.read().strip('\\n')

print(content)

# with open("Input/Letters/starting_letter.txt", mode='a') as letter:
#     letter_content = letter.read()
#     print(letter_content)
#     for names in content:
#         letter.write(letter.replace('[name]', names))
for names in content:
    with open(f"Output/ReadyToSend/{names}", mode='w') as letter:
        with open('Input/Letters/starting_letter.txt') as template:
            letter_content = template.read()
        letter.write(letter_content.replace('[name]', names))
        # name_inserted = letter_content.replace('[name]', names)