


sum(N, N, N).
sum(M, N, S):-
  N>M,
  X is M+1,
  sum(X, N, T),
  S is M+T.
