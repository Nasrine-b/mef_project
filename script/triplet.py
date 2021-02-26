from scipy.sparse import coo_matrix
class Triplet:

  def __init__(self):
    self.data = ([], ([], []))

  def __str__(self):
    return str(self.data)

  def append(self, I, J, val):
      self.data[0].append(val)
      self.data[1][0].append(I)
      self.data[1][1].append(J)

  def getElemAtIndex(self,i,j):
      return coo_matrix(self.data).toarray()[i][j]
