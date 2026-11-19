# f=open("mbox-short.txt",encoding="utf-8")
# x=f.readlines()
# z=[]

# for i in x :
#     if "From " in i:
#         z.append(i.split()[1])

# d={}
# for i in z:
#     d[i]=d.get(i,0)+1

# a=max(d.values())
# print(a)
# for i,j in d.items():
#     if j==a:
#         print(i,j)

#--------------------------------------- code to print hours , min and sec from .txt file ------------

f=open("mbox-short.txt",encoding="utf-8")
x=f.readlines()
z=[]

for i in x :
    if "From " in i:
        z.append(i.split()[-2])
for i in z:
    a=i.split(":")
    print(f"{a[0]} HOURS")
    print(f"{a[1]} MINUTES")
    print(f"{a[2]} SECONDS")
    print("-"*10)

