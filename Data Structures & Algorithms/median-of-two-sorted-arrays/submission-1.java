class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A = nums1;
        int[] B = nums2;

        if (nums1.length > nums2.length){
            int[] temp = A;
            A = B;
            B = temp;
        }
        int total = A.length + B.length;
        int half = (total) / 2;

        int l = 0;
        int r = A.length - 1;

        while(true){
            int i = Math.floorDiv(l + r, 2);
            if (l > r) i = -1; // Handle empty A or out of bounds
            int j = half - i - 2;

            double Aleft = (i >= 0) ? A[i] : Double.NEGATIVE_INFINITY;
            double Aright = (i + 1 < A.length) ? A[i+1] : Double.POSITIVE_INFINITY;
            double Bleft = (j >= 0) ? B[j] : Double.NEGATIVE_INFINITY;
            double Bright = (j + 1 < B.length) ? B[j+1] : Double.POSITIVE_INFINITY;

            if (Aleft <= Bright && Bleft <= Aright){
                if (total % 2 != 0){
                    return Math.min(Aright, Bright);
                }
                else{
                    return (Math.max(Aleft, Bleft) + Math.min(Aright, Bright)) / 2.0;
                }
            }
            else if(Aleft > Bright){
                r = i - 1;
            }
            else{
                l = i + 1;
            }
        }
    }
}