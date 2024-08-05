import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict={row.letter:row.code for (index,row) in data.iterrows()}
word=input("Enter a word: ").upper()
output_list={letter:alphabet_dict[letter] for letter in word}
print(output_list)