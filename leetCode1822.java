class Solution {
    public int arraySign(int[] nums) {
        int product = 1;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] > 0)
                product *= 1;
            else if(nums[i] < 0)
                product *= -1;
            else product *= 0;
        }
        System.out.println(product);
        
        if(product > 0)
            return 1;
        else if(product == 0)
            return 0;
        else return -1;
    }
}