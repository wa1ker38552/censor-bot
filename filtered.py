def filt(text):
  bad = [False]
  banned = open('blacklisted.txt','r').read().split('\n')
  splitby = open('splitby.txt','r').read().split('\n')
  for i in range(len(banned)):
    if banned[i] in text:
      bad[0] = True
      bad.append(banned[i])
  for y in range(len(splitby)):
    for x in range(len(banned)):
      if banned[x] in ''.join(text.split(splitby[y])):
        bad[0] = True
        bad.append(banned[x])
  return bad 
