ls = [4,5,6,7,8,9,10]
sixN = lambda n : n + 10*n+n + 100*n+10*n+n
print("A kapott számok: ",list(map(sixN,ls)))
