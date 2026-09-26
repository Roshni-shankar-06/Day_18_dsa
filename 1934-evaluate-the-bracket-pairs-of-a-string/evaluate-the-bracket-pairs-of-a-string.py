class Solution:

  def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
    # Build the lookup map
    mapping = {key: value for key, value in knowledge}

    ans = []
    i = 0
    n = len(s)

    while i < n:
      if s[i] == '(':
        # Find the closing bracket
        j = i + 1
        while j < n and s[j] != ')':
          j += 1
        # Extract the key
        key = s[i + 1 : j]
        # Append corresponding value or '?'
        ans.append(mapping.get(key, '?'))
        i = j + 1
      else:
        ans.append(s[i])
        i += 1

    return ''.join(ans)
