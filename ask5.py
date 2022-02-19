import string


def stringchange(line):
    for charecter in string.punctuation:
        line = line.replace(charecter, " ")
    return line


word_count = {}
towletters_count = {}
threeletters_count = {}

def sortword(dictionary):
    sorted_values = []
    for key in dictionary:
        sorted_values.append((dictionary[key], key))
    sorted_values = sorted(sorted_values)
    sorted_values = sorted_values[::-1]
    return sorted_values




with open("two_cities_ascii.txt", 'r') as fi:
    for line in fi:
        line = stringchange(line)
        words = line.split()

        for word in words:
            word = word.lower()
            twochars = word[0:2]
            if (len(word)>2):
                threechars = word[0:3]

            if  towchars in towletters_count:
                towletters_count[twochars] += 1
            else:
                threeletters_count[towchars] = 0

            if threechars in threeletters_count:
                threeletters_count[threechars] += 1
            else:
                threeletters_count[threechars] = 0


            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 0


top_word = sortword(word_count)[:10]
top_two = sortword(towletters_count)[:3]
top_three = sortword(threeletters_count)[:3]

 print("The top ten most used words are:")
 for tuple_freq in top_words:
     count, word = tuple_freq
     print("{0:15}{1:8d}".format(word, count))

print("The top three most used first two letters are:")
for tuple_freq in top_tow:
    count, twochars = tuple_freq
    print("{0:15}{1:8d}".format(twochars, count))

    print("The top three most used first three letters are:")
    for tuple_freq in top_three:
        count, threechars = tuple_freq
        print("{0:15}{1:8d}".format(threechars, count))
