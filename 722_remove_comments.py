class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        def parse(s, this_line_in_comments, to_be_continue):
            if s == "":
                if not this_line_in_comments:
                    to_be_continue = False
                return s, this_line_in_comments, to_be_continue

            if this_line_in_comments:
                if "*/" in s:
                    return parse(s.split("*/",1)[1], False, False)
                else:
                    return "", this_line_in_comments, to_be_continue
            else:
                if "/" not in s:
                    return s, this_line_in_comments, to_be_continue
                else:
                    left,right = s.split("/",1)
                    if right == "":
                        return s, this_line_in_comments, to_be_continue
                    c = right[0]
                    if c == "/":
                        return left, False, False
                    elif c == "*":
                        cur_str ,this_line_in_comments, to_be_continue = parse(right[1:], True, True)
                        return left+cur_str, this_line_in_comments, to_be_continue
                    else:
                        cur_str ,this_line_in_comments, to_be_continue = parse(right, False, to_be_continue)
                        return left + "/"+ cur_str, this_line_in_comments, to_be_continue

        this_line_in_comments = False
        res = []
        new_line=""
        to_be_continue = False
        for s in source:
            cur_str, next_line_in_comments, to_be_continue  = parse(s, this_line_in_comments, to_be_continue)
            this_line_in_comments = next_line_in_comments
            new_line += cur_str
            if not to_be_continue and new_line!="":
                res.append(new_line)
                new_line = ""
                to_be_continue = False

        return res
