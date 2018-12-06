print ("Welcome to the text-to-Play button comment converter!")
originaltext = input("Enter text: ")
length = len(originaltext)
for i in range(1, length):
    print (originaltext[:i])

print (originaltext)

for i in range(1, length):
    print (originaltext[:length-i])
