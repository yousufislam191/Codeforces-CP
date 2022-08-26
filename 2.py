array = []
NumberOfWord = int(input())

for x in range(NumberOfWord):
    text = str(input().lower().replace(" ", ""))
    if 1 <= len(text) <= 100:
        array += list(map(str, text.split()))
    else:
        print('condition not mached')

for singleWord in array:
    if(len(singleWord) > 10):
        count = 0
        for i in singleWord:
            count += 1
        print(singleWord[0] + str(count-2) + singleWord[len(singleWord)-1])
    if(len(singleWord) <= 10):
        print(singleWord)
