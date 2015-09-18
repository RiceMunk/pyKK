import numpy as np

def kkint():
  """
  KK integration
  """
  raise NotImplementedError()

def kkiter(model,wavel,transmittance,ice_thickness,m_guess=1.3+0.0j,**kwargs):
  """
  KK iteration

  Returns
  -------
    m : The complex refractive index for the spectrum
  """
  raise NotImplementedError()
  # m = np.ones_like(wavel)*np.nan
  # cM = m_guess
  # for cIndex,(cWavel,cTransmittance) in enumerate(zip(wavel,transmittance)):
  #   alpha_args = {}
  #   if wavel in model.
  #   cAlpha = model.alpha(ice_thickness,cTransmittance,**kwargs)

  # return m


  # alpha = model.alpha(alpha_params)
  # k = model.k(k_params)
  # n = kkint(kkint_params)
  # transmission = model.transmission(transmission_params)
  # diff = transmission - transmission_target


def calculate_n(model):
  """
  Calculate n with given model
  """
  raise NotImplementedError()

def calculate_k(model):
  """
  Calculate k with given model
  """
  raise NotImplementedError()

