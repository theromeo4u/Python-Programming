f = open("file.txt")
content = f.read()
if "Romeo" in content:
    print(f"The word Romeo is present")
else:
    print(f"The word Romeo is not present")
        
f.close()