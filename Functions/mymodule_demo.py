import mymodule

x = 1
y = 77

addition = mymodule.cal_sum(x+y)
print ("addition",addition)
print ("mymodule.__version__",mymodule.__version__)
print ("mymodule.func_type",mymodule.func_type)

"""
OUPUT:
PS C:\Users\Sandesh Gawde\github\sandesh-gawde\python_for_everybody\Functions> python3 .\mymodule_demo.py                             Running as imported module
addition 78
mymodule.__version__ 1.0
mymodule.func_type basic

>>> import mymodule
Running as imported module
>>> dir (mymodule)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'cal_sum', 'func_type']
>>> help (mymodule.cal_sum)
Help on function cal_sum in module mymodule:

cal_sum(a=0, b=0)
"""
