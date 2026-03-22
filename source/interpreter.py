class Interpreter:
  def __init__(self):
    self.variables = {}

  def get_kind(self,token,expected_kind):
    if expected_kind == "number":
      return token.isdigit()
    
    elif expected_kind == "string":
      if token.startswith('"') and token.endswith('"'):
        return token[1:-1]
      return token
      
    elif expected_kind == "bool":
      if token.lower() in ("true","false"):
        return True
    
    elif expected_kind == "identifier":
      return token
    return False
    
  def evaluate_expression(self,token,args=None):
    if token.startswith('if') or token.startswith('elif') :
      first_colon = token.find(':')
      else_colon = token.find("else:")
      parts = token.split()
      condition = token[2:first_colon].strip()        # Everything between 'if' and ':'
      if_true_val = token[first_colon+1:else_colon].strip() # Between ':' and 'else:'
      else_val = token[else_colon+5:].strip()         # Everything after 'else:'
      is_true = eval(condition, {}, args) 
      if is_true:
        return eval(if_true_val, {}, args) 
      else:
        return eval(else_val, {}, args)
    
  def evaluate_comparason(self,token,args):
    pass
  
  def evaluate_combining(self,token):
    pass
  
  def evaluate_math(self,token):
    pass
  
