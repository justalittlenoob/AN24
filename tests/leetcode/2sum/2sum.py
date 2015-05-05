def twoSum(nums, target):
        i = 0
        j = len(nums) - 1
        k =0
        dic = []
        tup =()
        for k in range(1,len(nums)+1):
            tup = (k,nums[k-1])
            dic.append(tup)
        dic.sort(lambda x,y:cmp(x[1],y[1])) 
        print 'dic:', dic
        while i < j:
            
            #if i < j:
            sum = dic[i][1] + dic[j][1]
            if sum == target :
                return dic[i][0], dic[j][0]
            elif sum < target:
                i=i+1
            else:
                j=j-1
            break

if __name__ == '__main__':
    twoSum([-1,-2,-3,-4,-5], -8)
