#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
    for name in name_list:
        name = name.strip("\n")
        with open("Input/Letters/starting_letter.txt", 'r') as letter:
            old_letter = letter.read()
            new_letter = old_letter.replace("[name]", name)
            with open(f"Output/ReadyToSend/to_{name}.txt", 'w') as to_send:
                to_send.write(new_letter)
        