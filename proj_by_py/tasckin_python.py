'''
 #պետք է տպի ներմուծված թվի յոթնապատիկը
a = int(input())
a *=7
print(a)

'''
# task numbr 2
'''
a = float(input())
c = a*2
print(c)
#պետք է տպի ներմուծված թվի կրկնապատիկը
'''

#task  num 3

'''
Հաշվիր օգտագործողի տարիքը։ Օգտագործողը պիտի ներմուծի իր ծննդյան
թվականը, իսկ ծրագիրը պետք է տպի նրա տարիքը։




from time import ctime, time, sleep, asctime, localtime
usBrdey = input("write your birthyear") 
usBrdey1 = int(usBrdey)  # ogtagorcum enq int() vorpesi type lini tiv
current_year = localtime().tm_year  # localtime().tm_year  cuic e talis nekaic tarin  
current_year1 = int(current_year) 
useyear = current_year1- usBrdey1  
print(type(useyear))
print(useyear)
'''


# task 4



'''Օգտագործողը ներմուծում է որոշակի քանակի նիշեր(symbol), իսկ ծրագիրը
պետք է տպի դրա եռապատիկը։

symbol = input("write dymbol")
res = symbol * 3
print(res)
'''

# task 5



'''Օգտագործողը ներմուծում է օրերի քանակը, իսկ ծրագիրը պիտի տպի, թե տվյալ
քանակի օրերում քանի վայրկյան կա։
dey = int(input("write count day"))
cecDey = 24 * 60 * 60 * dey
print(cecDey)
'''

# task 6


'''Գրիր ծրագիր, որը կհաշվի 5/x^2 + x*y*z-z/x արժեքը, որտեղ x, y, z ներմուծում է
օգտվողը

x = int(input("input x"))
y = int(input("input y"))
z = int(input("input z"))
res = 5/(x**2) + (x * y * z) - (z / x )
print(res)
  '''


# task 7

'''Գրիր ծրագիր, որը կտպի օգտագործողի ներմուծած թիվը զու՞յգ է, թե՞ կենտ

num = input("write in number:")
num1 = int(num)
if num1 % 2 == 0:
        print("input nummber is even")
else:
    print(f"{num1} add number")
'''

# task 8


'''Գրիր ծրագիր, որը կտպի օգտագործողի ներմուծած թիվը միաժամանակ 2-ի եւ 3-
ի բազմապատի՞կ է, թե՞ ոչ։

i = input("")
inum = int(i)
num1 = 1874
num2 = 2232

if num1 % inum == 0 & num2 % inum == 0:
    print(f"{inum}@  bazmzpatiq e {num1} end {num2} hamar  ")
else:
    print(f"{inum} bazmzpatik che {num1} end {num2} hamar")
'''

# task 9




product_name = input("product name  ") 
produqt = {
    "kola":670,
    "potatoes":250,
    "bread":220,
    "egg":80,
    "milk":180
}
if product_name == "bread":
     print(produqt["bread"])
elif product_name == "kola":
     print(produqt["kola"])
elif product_name == "egg":
    print(produqt["egg"])
elif product_name == "milk":
    print(produqt["milk"])
elif product_name == "potatoes":
    print(produqt["potatoes"])
else:
    print("end")