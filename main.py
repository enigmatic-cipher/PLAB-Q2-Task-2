"""
Given a string as input. Print capital if we encounter capital letter. Print small otherwise. Assume string contains only alphabets.
Input-> "car"
Output->
c:small 
a:small 
r:small
"""

st = "car"
ln = len(st)
for i in range(0,ln):
  ch = st[i]
  if (ch>="a" and ch<="z"):
    print(f"{ch}:small")
  elif (ch>="A" and ch<"Z"):
    print(f"{ch}:Capital")
