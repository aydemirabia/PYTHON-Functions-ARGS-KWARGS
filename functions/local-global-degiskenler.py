#  "global scope"

x = 'global x';

def function():
    # local scope
    # eğer x = 'local x'; olarak atama yapmasaydık global scope'daki x değeri çıktı olarak dönerdi.
    x = 'local x';
    print(x);
    
function();
print(x);

########################################################

# "global scope"

name = "Yigit";
def changename(new_name):
    # local
    name =new_name;
    print(name);
  
changename("Hazal");
print(name);

########################################################

name = "Rana";

def tanisma():
    name = "Emir";
    
    def merhaba():
        print('Hello '+ name);
        
    merhaba();

tanisma();