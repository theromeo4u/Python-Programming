words = ["Make a lot of money", "buy now", "subscribe this"," click this"]

with open("names.txt","r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))
    
    
    
with open("names.txt", "w") as f:
    f.write(content)