from py4j.java_gateway import JavaGateway, GatewayParameters

class YourPythonClass():
    def __init__(self):
        gg = JavaGateway(gateway_parameters=GatewayParameters(port=25536))

        # one example of calling  
        p = gg.jvm.java.util.Random()
        print("Printing random number from the virtual machine: ", p.nextInt(10))
        
        # getting your class 
        self.g = gg.entry_point.getYourJavaClass()  

    # and call functions of YourJavaClass    
    def fun1_py(self):
        return self.g.fun2Java(), self.g.fun3Java()/2.0, self.g.fun4Java()
   
    def fun2_py(self, arg1, arg2):
        return self.g.fun1Java(arg1, arg2)



c = YourPythonClass()
print(c.fun1_py())
print(c.fun2_py(2, 3))
