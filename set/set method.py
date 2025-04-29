s1={1,2,3,4,5}
s2={4,5,6,7}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s1,s2)
print(s1.symmetric_difference(s2))
print(s1.difference( s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))