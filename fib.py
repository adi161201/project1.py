n=int(input("Enter a number"));
i,a=0,1;
for i in range(n):
    print(a);
    a_temp=a[::];
    a=+i;
    i=a_temp;
    print(i);
    
    
