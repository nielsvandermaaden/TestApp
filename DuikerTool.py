from pydantic import BaseModel

# berekeningen van duikers, bruggen, onderleiders en hevels 
class DuikerTool(BaseModel):

  ## verliezen
  #-------------------------------
  # Weerstandscoëfficiënt mu
  # mu = 1 / √ (mu_i + mu_w + mu_u + n • mu_b)
  def weerstandscoëfficiënt(self):
    print('@')

  # mu_w = (2 • g • L) / (C^2 • R)
  def wrijvingsverlies(self):
    print('@')

  # mu_u = (1 - a • alpha)^2 • k
  def uittreeverlies(self):
    print('@')
    
  ## vuistregels ontwerp stuwen
  #-------------------------------
  
  # toelaatbare opstuwing
  # z_toelaatbaar = ∆H / (2•n)
  def toelaatbare_opstuwing(self):
    print('@')

  # toelaatbare uitstroomsnelheid (opstuwing als functie)
  # z_toelaatbaar_v_max = v_max^2 / (mu^2 • 2g)
  def toelaatbare_uitstroomsnelheid(self):
    print('#')

  ## evenwichtige diepte 
  #-------------------------------
  # L = (2•z) / S
  def evenwichtsdiepte(self):
    print('@')

  ## Duiker berekening
  #-------------------------------
  # z = (1 / (mu^2 • 2•g)) • (Q^2 • A^2)
  def stroomsnelheid(self):
    print('a')

  # Q=mu•A•√(2•g•z)
  def debiet(self):
    print('a')
    

  
  
