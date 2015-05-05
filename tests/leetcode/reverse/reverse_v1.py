class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        
        str_x = str(x)
        #result = []
        result = str_x[::-1]
        
        if x >= 0:
            if int(result) > math.pow(2, 31):
                return 0
            result = int(result)
            return result
        else:
            
            temp = result[-1]
            result = list(result)
            result.insert(0, temp)
            del result[-1]
            result = ''.join(result)
            result = int(result)
            if abs(result) > math.pow(2, 31):
                return 0
            return result
        
