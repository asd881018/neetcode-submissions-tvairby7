class Solution {
    public boolean isPalindrome(String s) {
        // Make s has only lowercase without space
        String cleanedString = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        // Have a string t with reverse order of s
        StringBuilder reversedString = new StringBuilder(cleanedString).reverse();
        // Compare s and t
        return cleanedString.equals(reversedString.toString());
    }
}
