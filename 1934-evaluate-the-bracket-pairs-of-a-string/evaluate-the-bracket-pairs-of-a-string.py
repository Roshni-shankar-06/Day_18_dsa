class Solution:

  def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
    # Build the lookup map
    mapping = {key: value for key, value in knowledge}

    ans = []
    i = 0
    n = len(s)

    while i < n:
    
    
