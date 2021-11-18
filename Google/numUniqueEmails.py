class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        output = []
        for email in emails:
            localname, domain = email.split("@")
            localname_out = ""
            for ch in localname:
                if ch == "+":
                    break
                elif ch == ".":
                    continue
                else:
                    localname_out += ch
            out = localname_out + "@" + domain
            if not out in output:
                output.append(out)

        return len(output)
