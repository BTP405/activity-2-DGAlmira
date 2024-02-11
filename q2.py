import matplotlib.pyplot as plt

def graphSnowfall(t):
    """Displays a bar chart representing snowfall accumulated for a certain day."""
    file = open(t,'r');
    content = file.readlines();
    count = 0;
    for line in content:
        if (line[-1] == '\n'):
            content[count] = line[:-1];
        content[count] = int(content[count]);
        count += 1;
    
    # creating the dataset
    data = {'0-10cms':0, '11-20cms':0, '21-30cms':0, '31-40cms':0, '41-50cms':0};
    
    for e in content:
        if (e >= 0 and e <= 10):
            data['0-10cms'] += 1;
        elif (e >= 11 and e <= 20):
            data['11-20cms'] += 1;
        elif (e >= 21 and e <= 30):
            data['21-30cms'] += 1;
        elif (e >= 31 and e <= 40):
            data['31-40cms'] += 1;
        else:
            data['41-50cms'] += 1;
    
    ranges = list(data.keys());
    values = list(data.values());

    minimum = min(values);
    maximum = max(values);
    increments = range(minimum, maximum + 1);
    plt.yticks(increments);
    plt.bar(ranges, values, color ='#7FC1C6', width = 0.4);
    plt.xlabel("Ranges")
    plt.ylabel("Number of Occurrences")
    plt.title("Snowfall Accumulation")
    plt.savefig('snowfall.png')

    file.close();

graphSnowfall('snowNums.txt');