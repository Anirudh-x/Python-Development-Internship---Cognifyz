# File Manipulation

word_count = {} # Dictionary created to store counted words
with open("python.txt", "r") as file: # Opening text file in read mode
    for line in file:
        words = line.split() # Spliting words of line
        for word in words:
            if word not in word_count: # If the word not in the word_count dictionary then it will get added
                word_count[word] = 1
            else: # If the word already present in the word_count dictionary then it count will get increase
                word_count[word] += 1
                
for word in sorted(word_count): # For loop to sort the words in word_count
    print(word, word_count[word])

