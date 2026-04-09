class Solution {
    public int[] plusOne(int[] digits) {
        for ( int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            } else {
                digits[i] = 0;
            }
        }

        // Deal with the edge case like [9,9,9]
        // Append extra 1 in digits
        digits = new int[digits.length + 1];
        digits[0] = 1;
        return digits;
    }
}
