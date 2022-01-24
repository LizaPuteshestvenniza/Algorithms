def detectCapitalUse(word):
  cnt_low = 0
  cnt_hight = 0
  for i in word:
    if i.isupper():
      cnt_hight += 1
    else:
      cnt_low += 1
  if cnt_hight == len(word) or cnt_low == len(word):
    return True
  elif word[0].isupper() and word[1:].islower():
    return True
  else:
    return False
