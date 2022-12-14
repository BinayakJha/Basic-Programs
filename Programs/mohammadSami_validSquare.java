//https://leetcode.com/problems/valid-perfect-square/
public class mohammadSami_validSquare {
    public static void main(String[] args) {
        int num = 808201;
        boolean ans = isPerfectSquare(num);
        System.out.println(ans);
    }

    private static boolean isPerfectSquare(int num) {
        long start = 1L;
        long end;
        long lNum = (long) num;
        if (lNum < 16 && lNum >= 4){
             end = lNum/2;
        }else if (lNum >= 16) {
             end = lNum/4;
        }else {
             end = lNum;
        }
        if( start*start == lNum || end*end == lNum){
            return true;
        }
        while (start < end){
            Long mid = start + (end - start)/2;
            if( start*start == lNum || end*end == lNum){
                return true;
            }
            if(mid*mid == lNum){
                return true;
            }else if(mid*mid > lNum){
                end = mid - 1;
            }else if(mid*mid < lNum){
                start = mid + 1;
            }
        }
        return false;
    }
}
