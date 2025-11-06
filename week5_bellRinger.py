# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = 'abracadabra'
# a. Retrieve the 5th character.
fifth_char = print(magic[4])
# b. Retrieve the second to last character.
second_to_last_char = print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
first_c_index = print(magic.index('r'))
#fidn the last occurrence of the letter 'a'
last_a_index = print(magic.rindex('a'))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
hij = print(alphabet[7:10])
hij2 = print(alphabet.index('hij'))
# b. Extract every second letter starting from 'a' to 'm'.
#get the letter m 
m_index = print(alphabet.index('m'))
every_second = print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
reversed_alphabet = print(alphabet[ : :-1])
i_have_a_dream = "When we allow freedom to ring—when we let it ring from every city and every hamlet, from every state and every city, we will be able to speed up that day when all of Gods children, black men and white men, Jews and Gentiles, Protestants and Catholics will be able to join hands and sing in the words of the old Negro spiritual, “Free at last, Free at last, Great God a-mighty, We are free at last.”"
reversed_speech = print(i_have_a_dream[ : :-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

famous_quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy" 
john = print(famous_quote.find("John F. Kennedy"))

extracted_name = print(famous_quote[83:])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
string_info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
subjective = print(string_info.index('subjective'))
# b. Extract every third letter.
every_third_word = print(string_info[0::3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.

words = string_info.split() # Split the string into words 
print(words) # output: ['python' , 'is' , 'fun.' , 'Fun', 'is' , 'good

reversed_words = ' '.join(reversed(words)) 

print(reversed_words) 

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text =  "MAY THE FORCE BE WITH YOU."
text_lower = print(text.lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
joined_motto = ' '.join(motto)
print(joined_motto)
# b. Now, split the string at every occurrence of the letter 'a'.
word1 = joined_motto.split('a')
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.