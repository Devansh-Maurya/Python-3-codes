phrase="Don't panic!"
plist=list(phrase)
print(phrase)
print(plist)

for i in range(len(plist)):
    plist.pop()

plist.extend("on tap")

new_phrase=''.join(plist)
print(plist)
print(new_phrase)
