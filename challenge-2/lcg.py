def slcg(seed: int):
  """
    Set seed for LCG
  """

  setattr(lcg, 's', seed)

def lcg():
  """
    LCG:
    s = (a * s + c) % m
  """

  if not hasattr(lcg, 'a'):
    setattr(lcg, 'a', 1140671485)
  if not hasattr(lcg, 's'):
    setattr(lcg, 's', 1)
  if not hasattr(lcg, 'c'):
    setattr(lcg, 'c', 128201163)
  if not hasattr(lcg, 'm'):
    setattr(lcg, 'm', 2 ** 24)

  setattr(lcg, 's', (getattr(lcg, 'a') * getattr(lcg, 's') + getattr(lcg, 'c')) % getattr(lcg, 'm'))

  return getattr(lcg, 's') / getattr(lcg, 'm')

if __name__ == '__main__':
  print('Default seed: 1')

  for i in range(10):
    print(f'Iter {i + 1} has: {lcg()}')

  print('\nSet seed: 32131252')

  slcg(32131252)

  for i in range(10):
    print(f'Iter {i + 1} has: {lcg()}')
