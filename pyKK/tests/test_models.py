#Tests for transmissionmodel.py
import pyKK

def test_modelcreation_basic():
  #the most basic model
  testmodel = pyKK.transmissionmodel.BaseModel()
  assert testmodel.alpha == testmodel.base_alpha
  assert testmodel.irat == testmodel.base_irat
  assert testmodel.args_alpha == ('d','irat')
  assert testmodel.args_irat == ('d','alpha')
  #with a custom function for alpha
  def testalpha(x,y,duck):
    return x+y+duck
  testmodel = pyKK.transmissionmodel.BaseModel(alpha=testalpha)
  assert testmodel.alpha == testalpha
  assert testmodel.irat == testmodel.base_irat
  assert testmodel.args_alpha == ('x','y','duck')
  assert testmodel.args_irat != ('x','y','duck')
  #with a custom function for irat
  def testirat(a,b,puppy):
    return a+b+puppy
  testmodel = pyKK.transmissionmodel.BaseModel(irat=testirat)
  assert testmodel.alpha == testmodel.base_alpha
  assert testmodel.irat == testirat
  assert testmodel.args_alpha != ('a','b','puppy')
  assert testmodel.args_irat == ('a','b','puppy')
  #with a custom function for both alpha and irat
  testmodel = pyKK.transmissionmodel.BaseModel(alpha=testalpha,irat=testirat)
  assert testmodel.alpha == testalpha
  assert testmodel.irat == testirat
  assert testmodel.args_alpha == ('x','y','duck')
  assert testmodel.args_irat == ('a','b','puppy')

def test_modelcreation_hudgins():
  #the Hudgins model
  testmodel = pyKK.transmissionmodel.HudginsModel(1+1j)
  assert testmodel.modelname == 'Hudgins 1993'