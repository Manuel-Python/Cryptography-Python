#4 + 7 mode 12
val = (14 + 15) % 12
print(val)

#4*5 mod 12
val = (4*5) % 12
print(val)

# g = 2
# for i in range(7):
#     print(i, g ** i % 5)

g = 3

min_gen = 1000

for i in range(7):

    val_gen = (g**i) % 7

    if min_gen > val_gen:

        min_gen = val_gen

    print(i,val_gen)

print(min_gen)