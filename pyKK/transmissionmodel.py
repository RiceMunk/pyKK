import numpy as np
import inspect

class BaseModel:
  """
  The base class for containing free-form transmission models used
  by the Kramers-Kronig relation calculations
  """
  def __init__(self,
                modelname='Unknown',
                alpha=None,
                transmittance=None
              ):
    # raise NotImplementedError()
    self.modelname  = modelname
    if alpha is None: # Set function for calculating alpha
      self.alpha = self.base_alpha #default to base_alpha if none given
    else:
      self.alpha = alpha
    if transmittance is None: # Set function for calculating I/I0
      self.transmittance = self.base_transmittance #default to base_transmittance if none given
    else:
      self.transmittance  = transmittance
    #construct lists containing required variable names for calculating alpha and I/I0
    self.args_alpha = tuple(filter(lambda varname:varname!='self',inspect.getargspec(self.alpha).args))#self.alpha.func_code.co_varnames)
    self.args_transmittance = tuple(filter(lambda varname:varname!='self',inspect.getargspec(self.transmittance).args))#self.transmittance.func_code.co_varnames)
    # #check for extra arg vars from potential children:
    # argvars = filter(lambda varname:varname!='args_alpha' and varname!='args_transmittance' and 'args_' in varname,locals().keys())
    # print argvars
    # if len(argvars)>0:
    #   for cArgvar in argvars:
    #     self.args_alpha+=locals()[cArgvar]
    #     self.args_transmittance+=locals()[cArgvar]
  def base_alpha(self,d,transmittance):
    return (-1./d)*np.log(transmittance)

  def base_transmittance(self,d,alpha):
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
  and transmittance which seems common in many transmission models found
  in the literature.
  """
  def __init__(self,modifier,modelname='Unknown Generic'):
    self.modifier=modifier
    self.args_modifier=tuple(filter(lambda varname:varname!='self',inspect.getargspec(self.modifier).args))#self.modifier.func_code.co_varnames)
    BaseModel.__init__(self,modelname=modelname,alpha=self.modified_alpha,transmittance=self.modified_transmittance)

  def modified_alpha(self,**kwargs):
    return self.base_alpha(kwargs['d'],kwargs['transmittance'])+np.log(self.modifier(**kwargs))/kwargs['d']

  def modified_transmittance(self,**kwargs):
    return self.base_transmittance(kwargs['d'],kwargs['alpha'])*self.modifier(**kwargs)

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
    # self.args_alpha.append('m1')
    # self.args_alpha.append('wavel')
    # self.args_transmittance.append('m1')
    # self.args_transmittance.append('wavel')

  def Hudgins_modifier(d,m1,wavel):
    """
    The coefficient that's common to the calcualtion of both
    transmittance and alpha for the Hudgins model
    """
    t01 = transmission_coeff(self.m0,m1)
    t02 = transmission_coeff(self.m0,self.m2)
    t12 = transmission_coeff(m1,self.m2)
    r01 = reflection_coeff(self.m0,m1)
    r12 = reflection_coeff(m1,self.m2)
    return np.abs((t01*t12/t02)/(1.+r01*r12*np.exp(4.j*np.pi*d*m1/wavel)))**2.