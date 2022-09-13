import pytest

class FloatClass:
def test_IsHundred(self):
try:
assert self==100.0
except AssertionError:
print('not 100')
pass

def test_Range(self):
try:
assert -100.0<=self<=100.0
except AssertionError:
print(self, 'out of range')
pass

lst=[-101,-100,-99,0,99,100.0,101.0]
for i in range(len(lst)):
FloatClass.test_Range(lst[i])
FloatClass.test_IsHundred(lst[2])




class StrClass:
def test_i_Indicate(self):
assert 'i' in self
def test_LenMoreFive(self):
assert len(self)>5

StrClass.test_i_Indicate('gghii ')
StrClass.test_LenMoreFive('gghii ')


class DictClass:
def test_IsNotEmpty(self):
assert self!={}
def test_HasKeyOne(self):
flag=False
for key in self:
if(key==1):
flag=True
assert flag


d={1:'Parisis',2:'Georgy'}
DictClass.test_IsNotEmpty(d)
DictClass.test_HasKeyOne(d)