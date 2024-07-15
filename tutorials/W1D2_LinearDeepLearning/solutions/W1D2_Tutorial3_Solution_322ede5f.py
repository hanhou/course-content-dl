def ex_net_rsm(h):
  """
  Calculates the Representational Similarity Matrix

  Arg:
    h: torch.Tensor
      Activity of a hidden layer

  Returns:
    rsm: torch.Tensor
      Representational Similarity Matrix
  """
  rsm = h @ h.T
  return rsm


## Uncomment and run
test_net_rsm_ex(SEED)