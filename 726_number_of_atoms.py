class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def push_to_dict(d, last_element, last_num):
            if last_element == "":
                return
            if last_num == "":
                num = 1
            else:
                num=int(last_num)
            d[last_element] = num

        def count_no_p(s):
            d = dict()
            last_element = ""
            last_num = ""
            for c in s:
                if c.isupper():
                    #d = push_to_dict(d, last_element, last_num)
                    if last_element != "":
                        if last_num == "":
                            num = 1
                        else:
                            num=int(last_num)
                        d[last_element] = num
                    
                    last_element = c
                    last_num = ""
                elif c.islower():
                    last_element += c
                elif c.isdigit():
                    last_num+=c
                
            #d = push_to_dict(d, last_element, last_num)
            if last_element != "":
                if last_num == "":
                    num = 1
                else:
                    num=int(last_num)
                d[last_element] = num
            return d

        def process_formula(s):
            left_res=dict()
            right_res = dict()
            if len(s) == 0:
                return left_res
            if s[0] == "(":
                left_p_num = 1
                for end,c in enumerate(s):                    
                    if c == "(":
                        left_p_num +=1
                    if c == ")":
                        left_p_num -=1
                    if left_p_num == 0:
                        break     
                end = end-1
                pattern = s[1:end]
                end2 = end+1
                mul = ""
                while end2 < len(s) and s[end2].isdigit():
                    mul += s[end2]
                    end2+=1
                if mul == "":
                    multiple = 1
                else:
                    multiple = int(mul)
                left_res = process_formula(pattern)
                for k in left_res:
                    left_res[k] *= multiple
                if end2 < len(s):
                    right_res = process_formula(s[end2:])
            else:
                p_ind = s.find("(")
                if p_ind != -1:
                    right_res = process_formula(s[p_ind:])
                else:
                    p_ind = len(s)
                left_res = count_no_p(s[:p_ind])
            
            if right_res:
                for k, v in right_res.items():
                    left_res[k] = left_res.setdefault(k, 0) + v
            return left_res
        element_num = process_formula(formula)
        keys = sorted(element_num.keys())
        res = ""
        for k in keys:
            res += k
            if element_num[k] > 1:
                res += str(element_num[k])
        return res
