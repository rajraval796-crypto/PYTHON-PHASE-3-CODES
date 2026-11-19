#------------------------------------------------------code 1 -------------------------------------

# f=open("lec1.txt","r")
# a=f.read()
# print(f" THE MODE OF FILE IS {f.mode}")
# print(f" THE NAME OF FILE IS {f.name}")
# print(f" THE READ PERMISSION  OF FILE IS {f.readable()}")
# print(f" THE WRITE PERMISSION  OF FILE IS {f.writable()}")
# f.close()
# print(a.title())
# print(f" THE FILE IS CLOSED OR NOT {f.closed}")

#------------------------------------------------------code 2 -------------------------------------
f=open("1.txt")
a=f.read()
f.close()

f2=open("2.txt","w+")
f2.write(a[::-1])
f2.seek(0)
b=f2.read()
f2.close()

f3=open("3.txt","w")
f3.write(b.upper())
f3.close()

#------------------------------------------------------code 3 -------------------------------------
# f=open("class.txt")
# d=f.read()
# f.close()

# f2=open("ipl.txt","w")
# e=d.split()
# for i in e:
#     if i[0]=="d":
#         f2.write(i+"\n")
#     else:
#         continue
# f2.close()