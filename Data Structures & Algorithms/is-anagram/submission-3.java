class Solution {
    public boolean isAnagram(String s, String t) {
        
        // If diff length, then return false
        if (s.length() != t.length())
            return false;
        
        // // 1. Sorted, then compare
        // // Runtime O(n log n)
        // char[] sChars = s.toCharArray();
        // char[] tChars = t.toCharArray();

        // Arrays.sort(sChars);
        // Arrays.sort(tChars);

        // return Arrays.equals(sChars, tChars);

        // 2. Use 2 HashMap to record 2 diff strings, and compare the Hashmaps are the same or not
        // Runtime O(2n), but need more memory
        // HashMap<Character, Integer> map1 = new HashMap<>();
        // HashMap<Character, Integer> map2 = new HashMap<>();

        // // Use a for loop or for each, store value into the HashMap
        // for (char c : s.toCharArray()){
        //     map1.put(c, map1.getOrDefault(c,0) + 1);
        // }

        // for (char c : t.toCharArray()){
        //     map2.put(c, map2.getOrDefault(c,0) + 1);
        // }

        // return map1.equals(map2);

        // 3. Using Array (Fixed-size Hash Table)
        int[] store = new int[26];

        for (int i = 0; i < s.length(); i++){
            // Use ASCII table to get the location
            store[s.charAt(i) - 'a']++;
            store[t.charAt(i) - 'a']--;
        }

        // check if the table is all 0 or not
        for (int c : store){
            if (c != 0)
                return false;
        }
        return true;

    }
}
