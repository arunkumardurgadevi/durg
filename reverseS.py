def reverse(Sentence):
  words=Sentence.split(" ")
  newWords=[word[:: -1]for word in words]
  newSentence=" ".join(newWords)
  reurn newSentence
Sentence=input(" ")
print(reverse(Sentence))
