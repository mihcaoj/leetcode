// Naive solution (Time: O(n^2) / Space: O(n^2))
function twoSumNaive(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
  return [];
}

// Optimal solution (Time: O(n) / Space: O(n))
function twoSumOptimal(nums: number[], target: number): number[] {
  const numMap = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const complement = target - num;

    if (numMap.has(complement)) {
      return [numMap.get(complement)!, i];
    }
    numMap.set(num, i);
  }
  return [];
}
