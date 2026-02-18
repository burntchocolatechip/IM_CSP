#name = input("what is your name: ").strip().title()

#print("Hello", name + "!")

sentence = "the quick brown fox jumps over the lazy dog."
word = input("tell me a word from the sentence")
start = sentence.find(word)
length = len(word)
print(sentence[start:start+length])