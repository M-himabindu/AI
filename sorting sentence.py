def Func(S):
  W = S.split(" ")
  for i in range(len(W)):
     
      # convert all the words into lowercase
      W[i]=W[i].lower() 
  S = sorted(W)
  print(' '.join(S))
 
# Driver code
S = "the Quick brown fox jumPs over the lazY Dog"
 
# function call
Func(S)
