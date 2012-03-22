palindromes = []
i = j = 100
while i < 1000:
  while j < 1000:
    if str(j * i) == str(j * i)[::-1]:
      palindromes.append(j * i)
    j += 1
  i += 1
  j = 100
print max(palindromes)
