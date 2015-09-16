#Tests for transmissionmodel.py
import pyKK

def test_modelcreation_basic():
  #the most basic model
  testmodel = pyKK.transmissionmodel.BaseModel()
  assert testmodel.func_alpha == testmodel.base_alpha
  assert testmodel.func_irat == testmodel.base_irat
  assert testmodel.arglist_alpha == ('d','irat')
  assert testmodel.arglist_irat == ('d','alpha')
  #with a custom function for alpha
  def testalpha(x,y,duck):
    return x+y+duck
  testmodel = pyKK.transmissionmodel.BaseModel(func_alpha=testalpha)
  assert testmodel.func_alpha == testalpha
  assert testmodel.func_irat == testmodel.base_irat
  assert testmodel.arglist_alpha == ('x','y','duck')
  assert testmodel.arglist_irat != ('x','y','duck')
  #with a custom function for irat
  def testirat(a,b,puppy):
    return a+b+puppy
  testmodel = pyKK.transmissionmodel.BaseModel(func_irat=testirat)
  assert testmodel.func_alpha == testmodel.base_alpha
  assert testmodel.func_irat == testirat
  assert testmodel.arglist_alpha != ('a','b','puppy')
  assert testmodel.arglist_irat == ('a','b','puppy')
  #with a custom function for both alpha and irat
  testmodel = pyKK.transmissionmodel.BaseModel(func_alpha=testalpha,func_irat=testirat)
  assert testmodel.func_alpha == testalpha
  assert testmodel.func_irat == testirat
  assert testmodel.arglist_alpha == ('x','y','duck')
  assert testmodel.arglist_irat == ('a','b','puppy')