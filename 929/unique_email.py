class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
      unique_emails = {}
      for email in emails:
        at_pos = email.find('@')
        local_name = email[:at_pos]
        domain_name = email[at_pos:]
        stripped_local_name = ""
        for c in local_name:
          if c == '.': continue
          elif c == '+': break
          else: stripped_local_name += c

        stripped_email = stripped_local_name + domain_name
        if stripped_email not in unique_emails: 
          unique_emails[stripped_email] = True

      return len(list(unique_emails.keys()))