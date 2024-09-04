marks = {
    "Sudhir": 100,
    "Divya": 98,
    "Gunjan":90,
    10:"rahul"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Sudhir": 99, "Renuka" : 100})
# print(marks)

# print(marks.get("Sudhir 2")) #Prints None
# print(marks["Sudhir 2"]) # Returnd an error

print(marks.pop("Sudhir")) 
print(marks) 
print(marks.pop("saish", 88))
print(marks) 
print(marks.popitem())  
print(marks) 


# output
# 100
# {'Divya': 98, 'Gunjan': 90, 10: 'rahul'}
# 88
# {'Divya': 98, 'Gunjan': 90, 10: 'rahul'}
# (10, 'rahul')
# {'Divya': 98, 'Gunjan': 90}