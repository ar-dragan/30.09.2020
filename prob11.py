"""Mariuca tine evidenta iepurilor din crescatorie.Ea isi noteaza cati iepuri sunt la inceputul lunii,
cati au murit si cati s-au nascut in cursul fiecarii luni.Puteti sa realizati un program care, primind aceste date,
sa se afiseze la sfarsitul fiecarii luni cati iepuri sumt in crescatorie"""
n_initial=int(input("numarul de  iepurasi la inceputul lunii:"))
m=int(input ("numarul de iepuri morti:"))
n=int(input("numarul de iepuri nascuti:"))
print("la sfarsitul lunii au ramas",n_initial+n-m,"iepurasi")