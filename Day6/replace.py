word = "Subodh"

with open("name.txt","r") as f:
    content = f.read()
    
    contentNew = content.replace(word, "######")
    
with open("name.txt", "w") as f:
    f.write(contentNew)