class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n=len(heights)
        st=[float('inf')]*(4*n)
        def buildTree(i,l,r):
            if l==r:
                st[i]=l
                return l
            mid=(l+r)//2
            left_idx=buildTree(2*i+1,l,mid)
            right_idx=buildTree(2*i+2,mid+1,r)
            if heights[left_idx]>heights[right_idx]:
                st[i]=left_idx
            else:
                st[i]=right_idx
            return st[i]
        buildTree(0,0,n-1)
        def query(i,  l,r,  ql,qr,  h): #i->curr idx, l,r-->boundries of heights, ql,qr-->boundries of query, h--> just next greater height than h
            # print(f'idx->{i},  l,r->{l,r},  ql,qr->{ql,qr},    h->{h}')
            if ql>r or qr<l or heights[st[i]]<=h:   
                return -1
            if l==r:
                return l
            m=(l+r)//2
            left_idx=query(2*i+1,  l,m,  ql,qr,  h)
            if left_idx!=-1:
                return left_idx
            else:
                right_idx=query(2*i+2,  m+1,r,  ql,qr,  h)
                return right_idx
        ans=[]
        for a,b in queries:
            if a==b:
                ans.append(a)
                continue
            if a>b:
                a,b=b,a  # ensure a<b
            if heights[a]<heights[b]:
                ans.append(b)
                continue
            ql=b+1
            qr=n-1
            h=heights[a]
            idx=query(0,  0,n-1,  ql,qr,  h) #idx, l,r, ql,qr, h
            ans.append(idx)
        return ans


        
        
        ##BRUTE FORCE -- WORKING BUT GIVING TLE##
        # ans=[]
        # for i,j in queries:
        #     if i==j:
        #         ans.append(i)
        #         continue
        #     elif i>j:
        #         if heights[i]>heights[j]:
        #             ans.append(i)
        #             continue
        #         k=i+1
        #         max_height=heights[j]
        #     else:
        #         if heights[j]>heights[i]:
        #             ans.append(j)
        #             continue
        #         k=j+1
        #         max_height=heights[i]
        #     found=False
        #     while k<len(heights):
        #         if heights[k]>max_height:
        #             ans.append(k)
        #             found=True
        #             break
        #         k+=1
        #     if not found:
        #         ans.append(-1)
        # return ans