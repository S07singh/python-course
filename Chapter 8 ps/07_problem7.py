def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Sudhir", "Rahul", "Shubham", "Gunjan", "an"]

print(rem(l, "an"))