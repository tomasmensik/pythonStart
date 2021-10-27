import operator

def charFrequency():
    text = "You can literally call someone a fathead, but it's still mean. According to 'Psychology Today', 60 percent of human brain matter is made of fat."
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    sorted_frequency = dict(sorted(frequency.items(), key=operator.itemgetter(1), reverse=True))
    print(f'\nVěta: {text}\n')
    print("Četnost výskytu písmen: ")
    for key, value in sorted_frequency.items():
        print('(\'%c\', %3d),' %(key, value))

charFrequency()