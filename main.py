with open('books/frankenstein.txt','r') as f:
    file_contents = f.read()

#counts number of words
def count_words(doc):
    words = doc.split()
    return len(words)

#counts frequency of letters
def letter_frequency(doc):
    words = doc.lower() # convert letters to lowercase(other characters included)
    freq = {} # creating dictionary for easy maping
    for c in set(words):
        freq[c] = words.count(c)
    return freq
        
char_count_list = list(map(list, letter_frequency(file_contents).items()))
alpha_list = []
for chars in char_count_list:
    if chars[0].isalpha():
        alpha_list.append(chars) # created list only with alphabets

alpha_list.sort(key=lambda x:x[0])# sorting alphabet list
print("--- Begin report of books/frankenstein.txt ---")
print(f"{count_words(file_contents)} words found in the document")


for i in range(len(alpha_list)):
    print(f"The '{alpha_list[i][0]}' character was found {alpha_list[i][1]} times")
