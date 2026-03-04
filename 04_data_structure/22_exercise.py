from pprint import pprint

sentence = "This is a common interview question"

char_frequency = {}


for letter in sentence:
    if letter in char_frequency:
        char_frequency[letter] += 1
    else:
        char_frequency[letter] = 1
        


sorted_list = sorted(
    char_frequency.items(),
    key=lambda kv:kv[1],
    reverse=True
    )

# pprint(sorted_list,width=10)

print("Most repeated key :",sorted_list[0])
print("List repeated key :",sorted_list[-1])

        
        
