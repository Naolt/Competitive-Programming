import java.util.*;
import java.util.List;
class Solution {
    public List<String> fizzBuzz(int n) {
		
        List<String> nums = new ArrayList<String>();
		for(int i = 1; i <= n; ++i){

			nums.add((i%15==0)?"FizzBuzz":(i%5==0)?"Buzz":(i%3==0)?"Fizz":Integer.toString(i));
		
		}
		return nums;
    }

}