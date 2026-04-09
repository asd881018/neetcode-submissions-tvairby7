class Solution {
    public boolean isAnagram(String s, String t) {
        
        // Compare the length
        if (s.length() != t.length()) {
            return false;
        }

        // // 1. Conver to Arrays
        // char[] sArr = s.toCharArray();
        // char[] tArr = t.toCharArray();

        // // Sorted
        // Arrays.sort(sArr);
        // Arrays.sort(tArr);

        // // Compare

        // return Arrays.equals(sArr, tArr);

        // ------------------------------------------------------------------------------------
        // 2. Use two HashMap to store the occurance
        HashMap <Character, Integer> sMap = new HashMap<>();
        HashMap <Character, Integer> tMap = new HashMap<>();
        
        // Store the occurence
        for (char c : s.toCharArray()) {
            sMap.put(c, sMap.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            tMap.put(c, tMap.getOrDefault(c, 0) + 1);
        }
        
        // Compare
        return sMap.equals(tMap);


        // ------------------------------------------------------------------------------------
        // 3. Use one HashMap, any Char occur in s, + 1; any Char occur in t, -1;

        // Check if the HashMap has all 0  



        // 1.
        // Convert to Arrays

        // Sorting

        // Compare
        // If not same. return false. else, true


        // 2. Use two HashMap

        // Record the alphabet and the occurances

        // Compare


        // 3. Single Array, add occurence in s, subtract occurance in t



        // 1. convert to arrays, sorting, compare
        // char[] sArray = s.toCharArray();
        // char[] tArray = t.toCharArray(); 

        // Arrays.sort(sArray);
        // Arrays.sort(tArray);

        // return Arrays.equals(sArray, tArray);
        
        // 2. HashMap to record the occurnace, then compare
        // Runtime O(2n), but need more memory
        // HashMap <Character, Integer> sMap = new HashMap<>();
        // HashMap <Character, Integer> tMap = new HashMap<>();

        // for (char c : s.toCharArray()) {
        //     sMap.put(c, sMap.getOrDefault(c, 0) + 1);
        // }

        // for (char c : t.toCharArray()) {
        //     tMap.put(c, tMap.getOrDefault(c, 0) + 1);
        // }

        // return sMap.equals(tMap);

        // 3. Array to record (Fixed size of HashMap)
        // int[] dict = new int[26];

        // for (int i = 0; i < s.length(); i++) {
        //     // Add 1 when alphabet occur in s
        //     dict[s.charAt(i) - 'a']++;
        //     // Subtract 1 when alphabet occur in t
        //     dict[t.charAt(i) - 'a']--;
        // }

        // for (int i : dict) {
        //     if (i != 0) {
        //         return false;
        //     }
        // }

        // return true;

    }
}
