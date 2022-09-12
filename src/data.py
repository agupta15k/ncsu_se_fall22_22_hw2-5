import os, csv
from  src.Num import Num
from  src.sym import Sym
from  src.cols import Cols
from  src.row import Row

'''
Class `Data` is a holder of `rows` and their summaries (in `cols`)
'''

class Data:
    '''
    Constuctor which initializes the attributes

    Attributes:
    @cols: column class single object....no list here unlike rows....see next line :)
    @rows: storing Rows class objects

    Arguments:
    @src: input file name
    '''
    def __init__(self, the, src) -> None:
        self.cols = None 
        self.rows = []
        self.the = the
        
        '''
        Check if the recived file name (variable src) is a string. 
        If yes, then run csv function on it and also send add function name 
        If no, we get that someone tried being cheeky here. They gave us a list of rows
        of the file directly and didn't trust us :(
        We simply use the add function directly here instead of asking csv function
        to read each row and then use it.
        '''
        
        if type(src) == str:
            self.readFromCSV(src, self.add)
        else:
            for i in range(len(src)):
                self.add(src[i])


    
    def readFromCSV(self, fname: str, funcnm) -> None:
        """
        Read content from CSV file and run a custom function on each row
        @fname: file path with file name
        @func: custom user function
        """
        sep = self.the['Seperator']
        currentWorkingPath = os.path.dirname(__file__)
        relativePath = os.path.join(currentWorkingPath, fname)
        with open(relativePath, 'r') as file:
            reader = csv.reader(file, delimiter=sep)
            n = 0
            for row in reader:
                n = n + 1
                t ={n : row}
                funcnm(t)

    
    def add(self, xs):
        if self.cols is None:
            self.cols = Cols(list(xs.values())[0])
        else:
            temp_row = Row(xs)
            self.rows.append(temp_row)
            todo = self.cols.x + self.cols.y
            # todo is a list of Sym and Num objects
            for obj_col in todo:
                obj_col.add(list(temp_row.cells.values())[0][obj_col.at])

    # def abc(self,a,b):
    #     return a+b

    def stats(self, places = None, showcols = None, func = None) -> dict:
        if places is None:
            places = 2
        if showcols is None:
            showcols = self.cols.y
        if func is None:
            func = self.div
        t = {}
        print(showcols)
        '''In Progress...'''
        # for i in range(len(showcols)):
        #     #print(type(showcols[i]))
        #     class_name = type(showcols[i]).__name__
        #     func_name = class_name + "." + func
        #     print(func_name)
        #     #v = eval('func_name(showcols[i])')
        #     v = eval('math.pi(5,6)')
        #     print(v)
        #     if type(v) == int:
        #         v = self.rnd(v, places)
        #     t[showcols[i].name] = v
        return t
    

                

''' Can remove after testing, just to see the values outputted from the variables'''
# def showStats():
#     src = '../data/input.csv'
#     the = {"Seperator":","}
#     data = Data(the, src)
    
#     cols = data.cols
    
    
#     for i in cols.all:
#         print(i.name)
    
#     print("-"*100)
#     for i in cols.x:
#         print(i.name)
#         print(i._has)
#         print(i.at)
#     # print(cols.x)
#     # print(cols.y)
#     print("-"*100)
#     for i in cols.y:
#         print(i.name)
#     print("-"*100)
#     print(cols.names)
#     print(cols.klass)

#     print(data.stats(func = 'mid'))

            

# showStats()