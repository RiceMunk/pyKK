#Tests for transmissionmodel.py
import pyKK

def test_modelcreation_basic():
  #the most basic model
  testmodel = pyKK.transmissionmodel.BaseModel()
  assert testmodel.alpha == testmodel.base_alpha
  assert testmodel.transmittance == testmodel.base_transmittance
  assert testmodel.args_alpha == ('d','transmittance')
  assert testmodel.args_transmittance == ('d','alpha')
  #with a custom function for alpha
  def testalpha(x,y,duck):
    return x+y+duck
  testmodel = pyKK.transmissionmodel.BaseModel(alpha=testalpha)
  assert testmodel.alpha == testalpha
  assert testmodel.transmittance == testmodel.base_transmittance
  assert testmodel.args_alpha == ('x','y','duck')
  assert testmodel.args_transmittance != ('x','y','duck')
  #with a custom function for transmittance
  def testtransmittance(a,b,puppy):
    return a+b+puppy
  testmodel = pyKK.transmissionmodel.BaseModel(transmittance=testtransmittance)
  assert testmodel.alpha == testmodel.base_alpha
  assert testmodel.transmittance == testtransmittance
  assert testmodel.args_alpha != ('a','b','puppy')
  assert testmodel.args_transmittance == ('a','b','puppy')
  #with a custom function for both alpha and transmittance
  testmodel = pyKK.transmissionmodel.BaseModel(alpha=testalpha,transmittance=testtransmittance)
  assert testmodel.alpha == testalpha
  assert testmodel.transmittance == testtransmittance
  assert testmodel.args_alpha == ('x','y','duck')
  assert testmodel.args_transmittance == ('a','b','puppy')

def test_modelcreation_hudgins():
  #the Hudgins model
  testmodel = pyKK.transmissionmodel.HudginsModel(1+1j)
  assert testmodel.modelname == 'Hudgins 1993'
  print testmodel.args_alpha
  assert testmodel.args_alpha == ('d','transmittance','m1','wavel')