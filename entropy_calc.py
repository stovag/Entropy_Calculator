import mpmath as m
import math

msg = input()

### Find different characters in input ###

c_list = []
for c in msg:
    if c not in c_list:
        c_list.append(c)
c_num = len(msg)


### Find the numer of apearances of each character ###

c_app = []
for i in c_list:
    c_app.append([i, 0])

for i in c_app:
    for j in msg:
        if i[0] == j:
            i[1] = i[1] + 1

### Find the probability of each character ###

c_prob = []
for i in c_app:
    c_prob.append([i[0], float(i[1])/c_num])

### Find the entropy of each character ###
H_c = []

for i in c_prob:
    num = float(i[1])
    H = -(num * m.log(num, b=2))
    #print(m.log(i[1], b=2))
    H_c.append([i[0], H])

### Print the entropy of each character

for i in H_c:
    print("The entropy of", i[0], "is", float(i[1]))

### Print total entropy
H = 0
for h in H_c:
    H = H + float(h[1])
print("Total entropy is", H)

### Calculate and print minimum number of bits needed to encode the string

bit_size = math.ceil(H)
min_bits = bit_size * c_num

print("Optimal encoding is possible with ", min_bits, "bits")
