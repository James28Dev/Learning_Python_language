print("โปรแกรมหาค่าผลรวมของเลขที่หาร 3 ลงตัว ตั้งแต่ 1 - 30")
total = 0
for num in range(1, 31):
  if num % 3 == 0:
    total += num
print("ผลรวมของเลขที่หาร 3 ลงตัว ตั้งแต่ 1 - 30 คือ", total)