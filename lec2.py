# f=open("friends.txt")
# a=f.read()
# f.close()

# f2=open("fr2.txt","w+")
# f2.write(a[::-1])
# f2.seek(0)
# b=f2.read()
# f2.close()

# f3=open("fr3.txt","w+")
# f3.write(b.upper())
# f3.seek(0)
# cu=f3.readlines()
# print(f"THE SECOND LINE IS {cu[1]}")
# f3.seek(0)
# z=f3.read()
# c=0
# for i in  z:
#     if i in "AEIOU":
#         c+=1
# print(f"THE TOTAL NUMBER OF VOWELS ARE {c}")

#----------------------------------------------------pb-16-------------------------------------
# f=open("fr4.txt")


# f2=open("fr5.txt","w+")

# for i in range(4):
#     x=f.readline()
#     y=x.find("#")
#     line=(x[:y].strip())
#     if line:
#         f2.write(line + "\n")

# f2.seek(0)
# z=f2.read()
# print(z)
# f.close()
# f2.close()
