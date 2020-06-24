def cal_sum(a=0,b=0):
    return (a+b)

__version__ = 1.0
func_type = "basic"
#Call this module in calling module

if __name__ == "__main__":
    print ("Running as main function")
else:
    print ("Running as imported module")
