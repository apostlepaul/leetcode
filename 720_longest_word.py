class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def len_lex(x, y):
            if len(x) < len(y):
                return -1
            elif len(x) > len(y):
                return 1
            else:
                if x < y:
                    return 1
                elif x > y:
                    return -1
                else:
                    return 0

        words.sort(cmp=len_lex)
        res = ""
        word_valid = set()
        for word in words:
            if len(word) == 1:
                word_valid.add(word)
                res = word
            elif word[:-1] in word_valid:
                word_valid.add(word)
                res = word
        return res



