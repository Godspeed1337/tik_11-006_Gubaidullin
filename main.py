from shennon import Shennon

with open('123.txt', 'r') as f:
    string = ''.join(f.readlines())

print(string)
s = Shennon()
s.calc(string)
print(s.d)
print(s.p_sum)
print(s.code)
s.save_probs()
s.save_encoded(string)
