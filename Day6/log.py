word = "python"
with open("log.txt", "r") as f:
    content = f.read()
    if word in content:
        print("Contains")
    else:
        print("Not contains")
    