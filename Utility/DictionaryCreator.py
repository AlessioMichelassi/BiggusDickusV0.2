listOfWorld = []

with open('word.txt', 'r') as w:
    for line in w:
        definition = line.replace('QKeySequence.', '').lower()
        newSentence = F"\"{line.replace('QKeySequence.', '').lower().rstrip()}\":\"{line.rstrip()}\",\n"
        listOfWorld.append(newSentence)

with open('wordTranslated.txt', 'a+') as ws:
    for eachWorld in listOfWorld:
        ws.write(eachWorld)

print(listOfWorld)

