with open("f1.txt") as f:
    content1 = f.read()


with open("f2.txt") as f:
    content2 = f.read()


if content1 == content2:
    print("Yes both the file are identical")
    
else:
    print("No both the file are not identical")
    