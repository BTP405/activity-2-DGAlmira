def stats_decorator(func):
    """Displays the statistics of the numbers that appear in a list of characters"""
    def wrapper(*args, **kwargs):
        charList = func(*args, **kwargs);
        # removing non-numbers from charList
        numList = [int(char) for char in charList if char.isnumeric()];
        
        print(f"Numbers Read: {numList}");
        print(f"Number Count: {len(numList)}");
        print(f"Average: {sum(numList) / len(numList)}");
        print(f"Max: {max(numList)}");

        print("---------------");
        return numList;
    return wrapper;

@stats_decorator        
def processLine(line):
    """Returns a list of each character in a string"""
    charList = [char for char in line];
    return charList;

def printStats(t):
    """Reads and processes each line in a text file"""
    file = open(t, 'r');
    for line in file:
        processLine(line);
    file.close();

printStats('nums.txt');