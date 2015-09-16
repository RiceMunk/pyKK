import numpy as np

def kkint():
  """
  KK integration
  """
  raise NotImplementedError()

def kkiter(model):
  """
  KK iteration
  """
  raise NotImplementedError()
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

