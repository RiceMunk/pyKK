import numpy as np

class BaseModel:
  def __init__(self,
                modelname='Unknown',
                func_alpha=None,
                func_irat =None
              ):
    # raise NotImplementedError()
    self.modelname  = modelname
    if func_alpha is None: # Set function for calculating alpha
      self.func_alpha = self.base_alpha #default to base_alpha if none given
    else:
      self.func_alpha = func_alpha
    if func_irat is None: # Set function for calculating I/I0
      self.func_irat = self.base_irat #default to base_irat if none given
    else:
      self.func_irat  = func_irat
    #construct lists containing required variable names for calculating alpha and I/I0
    self.arglist_alpha = filter(lambda varname:varname!='self',self.func_alpha.func_code.co_varnames)
    self.arglist_irat = filter(lambda varname:varname!='self',self.func_irat.func_code.co_varnames)

  def base_alpha(self,d,irat):
    return (-1./d)*np.log(irat)

  def base_irat(self,d,alpha):
    return np.exp(-1.*alpha*d)

  # def transmission_coeff(self,m1,m2):
  #   """
  #   Transmission coefficient between mediums 1 and 2 with respective
  #   complex refractive indices
  #   """
  #   return 2.*m1/(m1+m2)

  # def reflection_coeff(self,m1,m2):
  #   """
  #   Reflection coefficient between mediums 1 and 2 with respective
  #   complex refractive indices
  #   """
  #   return (m1-m2)/(m1+m2)

  # def generate_alpha(self):
  #   raise NotImplementedError()
  #   self.alpha = lambda x: raise NotImplementedError()

  # def generate_transmission(self):
  #   raise NotImplementedError()
  #   self.transmission = lambda x: raise NotImplementedError()

# class HudginsModel(BaseModel):
#   def __init__(self,Trat,d,m0,m2):
#     raise NotImplementedError()
#     modelname = 'Hudgins'
#     t02 = self.transmission_coeff(m0,m2)    
#     alpha = lambda Trat,d,m1,m2,m3: (1./d)*(-1.*np.log(Trat)+np.log(np.abs()))
#     BaseModel.__init__(modelname,alpha,transmission)