vowels=['a','e','i','o','u']
word='poonam'
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for letter in found:
    print(letter)
