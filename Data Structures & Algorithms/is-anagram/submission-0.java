class Solution {
    public boolean isAnagram(String s, String t) {
        
        // If diff length, then return false
        if (s.length() != t.length())
            return false;
        
        // 1. Sorting, then compare
        
        // 2. Use 2 HashMap to record 2 diff strings, and compare the Hashmaps are the same or not 
        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();

        // Use a for loop or for each, store value into the HashMap
        for (char c : s.toCharArray()){
            map1.put(c, map1.getOrDefault(c,0) + 1);
        }

        for (char c : t.toCharArray()){
            map2.put(c, map2.getOrDefault(c,0) + 1);
        }

        return map1.equals(map2);

    }
}
