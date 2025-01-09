print("โปรแกรมนับคำ")
txt = "this is a book"
space = 1
for char in txt:
  if char == ' ':
    space += 1
print(f"จากประโยค {txt} นับได้ {space} คำ")