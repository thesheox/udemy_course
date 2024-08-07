import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict={row.letter:row.code for (index,row) in data.iterrows()}



def generate_phonetic():
    word=input("Enter a word: ").upper()
    try:
        output_list = {letter: alphabet_dict[letter] for letter in word}
    except KeyError:
        print("Sorry you can just enter letters")
        generate_phonetic()
    else:
        print(output_list)
generate_phonetic()
