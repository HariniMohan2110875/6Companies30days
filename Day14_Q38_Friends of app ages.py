class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        n = len(ages)
        c = 0
        counts = [0]*121
        for age in ages:
            counts[age] +=1

        for agea,ca in enumerate(counts):
            for ageb,cb in enumerate(counts):
                if ageb <= 0.5 *agea + 7: continue
                if ageb > agea: continue
                if ageb>100 and agea<100: continue
                c+=ca*cb
                if agea == ageb: c-=ca

        return c
        
        return c