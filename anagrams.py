thought_process = False

def find_all_combos(scrambled):
  limit = len(scrambled)

  def regroup(x):
    while x[-1] == x[-2]:
      x.remove(x[-1])
      x[-1] = str(int(x[-1]) + 1)
      if len(x) == 1: 
        break
    return x

  combos = []
  running = True

  while running:
    combo = ["1"]
    while True:
      if combo in combos:
        combo.append("1")
        regroup(combo)
        if combo[0] == str(limit+1):
          running = False
          break
      else:
        combos.append(combo)
        break
  if thought_process: 
    print(combos)
  return combos

def isAnagram(scrambled, striped):
  final, striped = sorted(scrambled.lower()), sorted(striped.lower())
  return final == striped



unscramble = input("\nEnter letters to unscramble: ")
combos = find_all_combos(unscramble)

anagrams = []

for combo in combos:
  for letter in combo:
    combo[combo.index(letter)] = unscramble[int(letter)-1]
  combos[combos.index(combo)] = "".join(combo)


combos.sort(key=len, reverse=True)
if thought_process: 
  print(combos)


for combo in combos:
  with open("allwords.txt", "r") as file:
    for line in file:
      word = line.strip()
      if isAnagram(combos[combos.index(combo)], word) and word not in anagrams:
          anagrams.append(word)
          print(word)


anagrams.sort(key=len, reverse=True)
if thought_process: 
  print(anagrams)