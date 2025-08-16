class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        index_first_6 = str_num.find('6')
        if index_first_6!=-1 :
            return int(str_num[:index_first_6]+'9'+str_num[index_first_6+1:])
        return num

"""
in python str are immutable, so we cannot change a character in a string directly.
   so we create a new string with the desired change.
find() method returns the lowest index of the substring if found in the string, otherwise it returns -1.
rfind () method returns the highest index of the substring if found in the string, otherwise it returns -1.
"""