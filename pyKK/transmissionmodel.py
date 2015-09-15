import numpy as np

class BaseModel:
  def __init__(self,
                modelname='Basic transmission model'
              ):
    raise NotImplementedError()
    self.modelname = modelname

  def transmission_coeff(self,m1,m2):
    """
    Transmission coefficient between mediums 1 and 2 with respective
    complex refractive indices
    """
    return 2.*m1/(m1+m2)

  def reflection_coeff(self,m1,m2):
    """
    Reflection coefficient between mediums 1 and 2 with respective
    complex refractive indices
    """
    return (m1-m2)/(m1+m2)

  def generate_alpha(self):
    raise NotImplementedError()
    self.alpha = lambda x: raise NotImplementedError()

  def generate_transmission(self):
    raise NotImplementedError()
    self.transmission = lambda x: raise NotImplementedError()

class HudginsModel(BaseModel):
  def __init__(self,Trat,d,m0,m2):
    raise NotImplementedError()
    modelname = 'Hudgins'
    t02 = self.transmission_coeff(m0,m2)    
    alpha = lambda Trat,d,m1,m2,m3: (1./d)*(-1.*np.log(Trat)+np.log(np.abs()))
    BaseModel.__init__(modelname,alpha,transmission)