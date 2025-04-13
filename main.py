with open("Input/Names/invited_names.txt") as names:
    content = names.read().splitlines()

print(content)

for names in content:
    with open(f"Output/ReadyToSend/{names}", mode='w') as letter:
        with open('Input/Letters/starting_letter.txt') as template:
            letter_content = template.read()
        letter.write(letter_content.replace('[name]', names))
        # name_inserted = letter_content.replace('[name]', names)
