import numpy as np
from collections import defaultdict

class MarkovModel:

    def __init__(self, text, k): 

        self.k = k               
        self.tran = defaultdict(float)
        self.alph = list(set(list(text)))
        self.kgrams = defaultdict(int)
        n = len(text)
        for i in range(n-k):
            self.tran[text[i:i+k],text[i+k]] += 1.
            self.kgrams[text[i:i+k]] += 1

    def order(self):                  
        return self.k

    def freq(self, kgram):         
        assert len(kgram) == self.k    
        return self.kgrams[kgram]

    def freq2(self, kgram, c):   	
        assert len(kgram) == self.k    
        return self.tran[kgram,c]  

    def rand(self, kgram):            
        assert len(kgram) == self.k    
        Z = sum([self.tran[kgram, alph] for alph in self.alph])
        ele = np.random.choice(self.alph, 1, p=np.array([self.tran[kgram, alph] for alph in self.alph])/Z)
        p = list(np.array([self.tran[kgram, alph] for alph in self.alph])/Z)
        i = self.alph.index(ele[0])
        return ele[0], p[i]
        
    def gen(self, kgram, T):          
        assert len(kgram) == self.k    
        str = kgram
        proba = 1
        for _ in range(T):             
             c, p =  self.rand(kgram)
             proba *= p
             kgram = kgram[1:] + c     
             str += c			 
        return str, proba
