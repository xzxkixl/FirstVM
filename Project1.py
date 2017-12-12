# Task: Open a file from the web
# Iterate over the file
# Create a list of words from the file
# Iterate over new list.

from urllib.request import urlopen
def fetch_words():
    f = "http://icarus.cs.weber.edu/~hvalle/hafb/wasteland.txt"
    with urlopen(f) as story:
        story_words = []  # empty list
    for line in story:
        line_rec = line.decode('utf-8').split()
        # print(line_rec)
        for word in line_rec:
            story_words.append(word)
    # Print list of words
    print("The file has: ", len(story_words), " words")
