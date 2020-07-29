# Exercise No.  11.2
# File Name:    hw11project2
# Programmer:   Anna Li
# Date:         June 24nd, 2020

# Overall Plan:
# 1. Ask user for file name
# 2. Read file, eliminate any special characters
# 3. Strip all words and save to a list
# 4. Iterate through the word list and reserved word list to see if any match
# 5. IF they match, add to a dictionary and update the value every time the same word is matched

def main():
    print("This program counts the reserved words in a python file.")
    file = input("Please input the name of your .py file: ")
    filename = open(file, "r").read() #opens the file and saves contents to filename
    filename = filename.lower() # filename is set to lowercase
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~': # for any character in this string of special characters
        filename = filename.replace(ch, ' ')   # replace special characters with an empty space
    words = filename.split()  #save all the words into a words list, eliminate any extra space

    #these are the reserve words
    reserve = ["False", "class", "finally", "is", "return", "None", 'continue', "for", "lambda", "try",
               "True", "def", "from", "nonlocal", "while", "and", "del", "global" ,"not" ,"with",
               "as" ,"elif", "if", "or" ,"yield", "assert", "else", "import", "pass", "break", "except", "in", "raise"]

    count = {} #empty dictionary
    for w in words: # for each word save in the list words
        for r in reserve: # for each word in the list of reserve words
            if w == r: # if they are the same
                count[w] = count.get(w,0) + 1 # add an entry into the dictionary if it doesn't alerady exist as a key, add one
                                            #to the value everytime the same word is present


    print("Reserved words in your file:", count)



main()