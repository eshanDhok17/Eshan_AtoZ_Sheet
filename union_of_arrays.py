class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        res = []
        i, j = 0, 0
        while(i < n and j < m):
            while(i+1 < n and arr1[i] == arr1[i+1]): i += 1
            while(j+1 < m and arr2[j] == arr2[j+1]): j += 1
            if arr1[i] != arr2[j]:
                num = -1
                if arr1[i] < arr2[j]:
                    num = arr1[i]
                    i += 1
                else:
                    num = arr2[j]
                    j += 1
                res.append(num)
            
            elif arr1[i] == arr2[j]:
                res.append(arr1[i])
                i += 1
                j += 1
        
        while(i < n):
            if(res[-1] == arr1[i]):
                i += 1
            else:
                res.append(arr1[i])
                i += 1
                
                
        while(j < m):
            if(res[-1] == arr2[j]):
                j += 1
            else:
                res.append(arr2[j])
                j += 1
        
        return res