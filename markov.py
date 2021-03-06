
def nbr_occur(kgram, text):
  n = len(text)
  m = len(kgram)
  occ = 0
  for i in range(n-m+1): 
    if ( text[i:i+m] == kgram):
      occ += 1
  return occ


def get_proba_markov(kgram, text):
  n = len(get_characters(kgram,text))
  occ = nbr_occur(kgram,text)
  mydict = {}
  for i in range(n):
    mydict[get_characters(kgram,text)[i]] = nbr_occur(kgram+get_characters(kgram,text)[i], text)/occ

  return mydict
