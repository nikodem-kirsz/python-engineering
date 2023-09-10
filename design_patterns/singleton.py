"""
Singleton Pattern:
Logger: Ensure there is only one instance of a logger in your application to centralize and 
manage log messages effectively.

Database Connection Pool: Maintain a single pool of database connections to efficiently handle 
database access across your application.
"""

class Singleton:
    # __new__ which serves object creation is called first then __init__ to initialize object
    # with given properties anytime you create object using Singleton()
    _instance = None

    def __new__(cls, connection = "mysql:128:1:0:2:8040:called_from_new"):
        if cls._instance is None:
            # 1 option, python3 automaticaly 
            # infers class and class context based on the actual context
            # which is Singleton
            cls._instance = super().__new__(cls)
            # 2 option, to pass both class Singleton and cls as class context
            # so the python knows to use object's super class and context 
            # for creation as Singleton so it creates object of this class
            # and saves it as a class property
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.connection = connection
        return cls._instance
    def __init__(self, connection = "mysql:init:called_from_init"):
        self.connection = connection
    def mitigate(): ...
    def object_id(): ...    

class SubSingleton(Singleton):
    ...

s1 = Singleton("mysql:666")
s2 = SubSingleton()
# s2.connection = "ssasa"
print(s1 is s2)
print(s1.connection)
print(s2.connection)