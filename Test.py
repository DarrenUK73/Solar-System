class Obj(object):
   def __init__(self):
      self.a = 2
      self.b = []
      self.c = []
   
   def append_att(self, att):
      self.__dict__[att].append(self.a)

o = Obj()
o.append_att('b')
o.append_att('b')
o.append_att('c') 
print(o.b)
print(o.c)