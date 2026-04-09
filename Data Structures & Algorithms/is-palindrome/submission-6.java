class Solution {
    public boolean isPalindrome(String s) {
        // // 1. Using Cleaned String and Reversed String
        // // Make s has only lowercase without space
        // String cleanedString = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        // // Have a string t with reverse order of s
        // StringBuilder reversedString = new StringBuilder(cleanedString).reverse();
        // // Compare s and t
        // return cleanedString.equals(reversedString.toString());

        // // 2. Two-Pointer Approach
        // int l = 0;
        // int r = s.length() - 1;
        // while(l < r){
        //     while(l < r && !Character.isLetterOrDigit(s.charAt(l))){
        //         l++;
        //     }
        //     while(l < r && !Character.isLetterOrDigit(s.charAt(r))){
        //         r--;
        //     }
        //     if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))){
        //         return false;
        //     }
        //     l++;
        //     r--;
        // }
        // return true;


        // int l = 0;
        // int r = s.length() - 1;

        // while (l < r) {
        //     // Make sure s[i] or s[r] is a lowercase char
        //     while (l < r && !Character.isLetterOrDigit(s.charAt(l))) {
        //         l++;
        //     }

        //     while (l < r && !Character.isLetterOrDigit(s.charAt(r))) {
        //         r--;
        //     }

        //     if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
        //         return false;
        //     }
        //     l++;
        //     r--;
        // }

        // return true;

        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            while (l < r && !Character.isLetterOrDigit (s.charAt(l))) {
                l++;
            }
            while (l < r &&!Character.isLetterOrDigit(s.charAt(r))) {
                r--;
            }
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
