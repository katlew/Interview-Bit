public class Solution {
    
    ArrayList<ArrayList<Integer>> res;
    public ArrayList<ArrayList<Integer>> combine(int n, int k) {
        res = new ArrayList<>();
        if (k > n)
            return res;
        rec(n, 0, k, new ArrayList<>());
        return res;
    }
    
    public void rec(int n, int last, int k, ArrayList<Integer> temp) {    
        if (k == 0) {
            res.add(new ArrayList(temp));
            return;
        }
        for (int i = last + 1; i <= n; i++) {   
            temp.add(i);
            rec(n, i, k - 1, temp);
            temp.remove(temp.size() - 1);
            
        }
    }
}

/*
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,
1. Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
2. Entries should be sorted within themselves.

Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python.
If you do, we will disqualify your submission retroactively and give you penalty points. 
*/