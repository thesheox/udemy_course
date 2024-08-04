#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_list=[]
with open("input/names/invited_names.txt") as name_file:
    for name in name_file.readlines():
        name_list.append(name.strip())
text=""
with open("input/letters/starting_letter.txt") as letter_text:
    text=letter_text.read()


for i in range(0,len(name_list)):
    with open(f"Output/ReadyToSend/letter_for_{name_list[i]}","a") as letter:
       letter.write(text.replace("[name]",name_list[i]))

# print(text.replace("[name]",name_list[0]))
# print(name_list)