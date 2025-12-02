from typing import Union

def add(x:Union[int,float], y:Union[int,float]) -> Union[int,float]:
    return x + y

if __name__=="__main__":
    print(add(1,2))
    print(add(1.0,2.0))
    print(add(1,3.0))