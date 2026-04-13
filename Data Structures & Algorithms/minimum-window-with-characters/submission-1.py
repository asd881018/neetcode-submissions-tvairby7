class Solution:
    def minWindow(self, s: str, t: str) -> str:    
    # slinding window and HashMap
        # s = "OUZODYXAZV", t = "XYZ"
        # ZODYX, YXAZ

        
        # hashmap of the window and t
        window, countT = {}, {}

        # countT = {x:1, y:1, z:1}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        need, have = len(countT), 0
        l = 0
        res, resLen = [-1, -1], float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            # find the window meet the condition (have == need)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    # update
                    res = [l, r]
                    resLen = r - l + 1
                
                # remove the redundant char in front
                # pop the front element
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
        
        l, r = res

        if resLen != float("infinity"):
            return s[l : r + 1]
        return ""

        

        # record the position from left to right, and the length (r - l + 1)