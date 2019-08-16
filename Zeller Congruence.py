from math import floor

def zeller(d,m,y):
    q = d
    Dict = {0:"Saturday",1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",
            5:"Thursday",6:"Friday"}
    K = y % 100; J = floor(y/100)
    h = (q+floor((13*(m+1))/5)+K+floor(K/4)+floor(J/4)-2*J)%7
    for key,val in Dict.items():
        if key == h:
            print(val)