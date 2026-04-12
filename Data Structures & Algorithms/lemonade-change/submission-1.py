class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        have = [0, 0, 0]

        for i in bills:
            if i == 5:
                have[0] += 1

            if i == 10:
                if have[0] >= 1:
                    have[0] -= 1
                    have[1] += 1
                else:
                    return False
                
            if i == 20:
                if have[0] >= 3:
                    have[0] -= 3
                    have[2] += 1
                elif have[0] >= 1 and have[1] >= 1:
                    have[0] -= 1
                    have[1] -= 1
                    have[2] += 1
                else:
                    return False

        return True
                