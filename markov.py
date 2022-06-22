
def nbr_occur(kgram, text):
  n = len(text)
  m = len(kgram)
  occ = 0
  for i in range(n-m+1): 
    if ( text[i:i+m] == kgram):
      occ += 1
  return occ


def get_characters(kgram, text):
  n = len(text)
  m = len(kgram)
  list_characters = []
  for i in range(n-m): 
    if ( text[i:i+m] == kgram and text[i+m] not in list_characters):
        list_characters.append(text[i+m])
  return list_characters


def get_proba_markov(kgram, text):
  n = len(get_characters(kgram,text))
  occ = nbr_occur(kgram,text)
  mydict = {}
  for i in range(n):
    mydict[get_characters(kgram,text)[i]] = nbr_occur(kgram+get_characters(kgram,text)[i], text)/occ

  return mydict
