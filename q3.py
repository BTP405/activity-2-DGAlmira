def wordCount(t):
    """
    Returns a dictionary with unique words as the keys and the 
    values being a list of the line numbers they appear
    """
    # special characters to not include
    punctuation = "!?.,"
    words = {};
    file = open(t, 'r');
    lineCount = 0;
    for line in file.readlines():
        lineCount += 1;
        # line.split makes a list of each unique word in the line
        for word in line.split():
            # .strip('.') to remove
            if word.lower().strip(punctuation) not in words.keys():
                words[word.lower().strip(punctuation)] = [lineCount];
            else:
                words[word.lower().strip(punctuation)].append(lineCount);
    
    file.close();
    return words;

wordDict = wordCount('words.txt');
print(wordDict);