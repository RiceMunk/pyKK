import numpy as np

class BaseModel:
  """
  The base class for containing free-form transmission models used
  by the Kramers-Kronig relation calculations
  """
  def __init__(self,
                modelname='Unknown',
                alpha=None,
                irat =None
              ):
    # raise NotImplementedError()
    self.modelname  = modelname
    if alpha is None: # Set function for calculating alpha
      self.alpha = self.base_alpha #default to base_alpha if none given
    else:
      self.alpha = alpha
    if irat is None: # Set function for calculating I/I0
      self.irat = self.base_irat #default to base_irat if none given
    else:
      self.irat  = irat
    #construct lists containing required variable names for calculating alpha and I/I0
    self.args_alpha = filter(lambda varname:varname!='self',self.alpha.func_code.co_varnames)
    self.args_irat = filter(lambda varname:varname!='self',self.irat.func_code.co_varnames)

  def base_alpha(self,d,irat):
    return (-1./d)*np.log(irat)

  def base_irat(self,d,alpha):
    return np.exp(-alpha*d)

  def transmission_coeff(self,m1,m2):
    """
    Transmission coefficient between mediums 1 and 2 with respective
    complex refractive indices.
    Used in many transmission models, so best to have it included
    in the base model instead of reimplementing in every other model.
    """
    return 2.*m1/(m1+m2)

  def reflection_coeff(self,m1,m2):
    """
    Reflection coefficient between mediums 1 and 2 with respective
    complex refractive indices.
    Used in many transmission models, so best to have it included
    in the base model instead of reimplementing in every other model.
    """
    return (m1-m2)/(m1+m2)

class GenericModel(BaseModel):
  """
  A generic transmission model following a pattern of alpha
  and I/I0 which seems common in many transmission models found
  in the literature.
  """
  def __init__(self,modifier,modelname='Unknown Generic'):
    self.modifier=modifier
    BaseModel.__init__(self,modelname=modelname,alpha=self.modified_alpha,irat=self.modified_irat)

  def modified_alpha(self,**kwargs):
    return self.base_alpha(kwargs['d'],kwargs['irat'])+np.log(self.modifier(**kwargs))/kwargs['d']

  def modified_irat(self,**kwargs):
    return self.base_irat(kwargs['d'],kwargs['alpha'])*self.modifier(**kwargs)

class HudginsModel(GenericModel):
  """
  The transmission model presented in Hudgins et al 1993
  This model is for a plane-parallel thin film of ice (medium 1)
  between a vacuum (medium 0) and substrate (medium 2)
  """
  def __init__(self,m2,modelname='Hudgins 1993'):
    self.m0 = 1.+0.j #complex refractive index for vacuum
    self.m2 = m2     #complex refractive index for substrate
    GenericModel.__init__(self,self.Hudgins_modifier,modelname=modelname)

  def Hudgins_modifier(d,m1,wavel):
    """
    The coefficient that's common to the calcualtion of both
    I/I0 and alpha for the Hudgins model
    """
    t01 = transmission_coeff(self.m0,m1)
    t02 = transmission_coeff(self.m0,self.m2)
    t12 = transmission_coeff(m1,self.m2)
    r01 = reflection_coeff(self.m0,m1)
    r12 = reflection_coeff(m1,self.m2)
    return np.abs((t01*t12/t02)/(1.+r01*r12*np.exp(4.j*np.pi*d*m1/wavel)))**2.