class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
      corrected_string = ""
      for c in s:
        if c.islower() == True: corrected_string += c.upper()
        elif c == '-': continue
        else: corrected_string += c

      print(corrected_string)
      length = len(corrected_string)
      if k >= length: return corrected_string
      rem = length%k

      final_string = ""
      if rem != 0:
        final_string += corrected_string[:rem]
        final_string += '-'

      for i in range(rem,length):
        final_string += corrected_string[i]
        if (i-rem+1)%k == 0 and i != length-1: final_string += '-'

      return final_string