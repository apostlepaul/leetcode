class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def merge(org_list, new_items):
            res = []
            to_merge = [new_items]
            for items in org_list:
                if items & new_items:
                    to_merge.append(items)
                else:
                    res.append(items)
            merged_set = set()
            for items in to_merge:
                merged_set |= set(items)
            
            res.append(merged_set)
            return res
            
        name_emails = dict()
        for account in accounts:
            name = account[0]
            emails = set(account[1:])
            if name not in name_emails:
                name_emails[name] = [emails]
            else:
                name_emails[name] = merge(name_emails[name], emails)
        
        res = []
        for name, emails in name_emails.items():
            for e in emails:
                res.append([name] + sorted(list(e)))
        return res
