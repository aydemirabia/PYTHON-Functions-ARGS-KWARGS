def displayuser(*args):
    print(type(args))
    print(args);
    
displayuser()

def displayuser(**kwargs):
    print(type(kwargs));
    print(kwargs);

displayuser(username ="rabia aydemir");
displayuser(username = "aydemir", email="aydemirabia@gmail.com");
displayuser(username = "aydemir", email="aydemirabia@gmail.com", country="Turkiye");

def myfunc(a, b, c, *args, **kwargs):
    print(a);
    print(b);
    print(c);
    print(args);
    print(kwargs);

myfunc(45, 50, 60, 70, 80, 90, 100, key1="value1", key2="value2");

# args --> type değeri : TUPLE
# kwargs --> type değeri : DICTIONARY 
