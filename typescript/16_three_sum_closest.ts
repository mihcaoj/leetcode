// Naive solution (Time: O(n^3) / Space: O(1))
function threeSumClosest(nums: number[], target: number): number {
  let n = nums.length;
  let closestSum = nums[0] + nums[1] + nums[2];

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        let sum = nums[i] + nums[j] + nums[k];
        if (sum === target) return sum;
        if (Math.abs(sum - target) < Math.abs(closestSum - target)) {
          closestSum = sum;
        }
      }
    }
  }

  return closestSum;
}

// Optimal soltuon (Time: O(n^2) / Space: O(1))
function threeSumClosestOptimal(nums: number[], target: number): number {
  nums.sort((a, b) => a - b); // sort ascending
  let closestSum = nums[0] + nums[1] + nums[2];
  let n = nums.length;

  for (let i = 0; i < n - 2; i++) {
    let left = i + 1;
    let right = n - 1;
    while (left < right) {
      let sum = nums[i] + nums[left] + nums[right];
      if (sum === target) return sum;

      if (Math.abs(sum - target) < Math.abs(closestSum - target)) {
        closestSum = sum;
      }

      if (sum < target) {
        left++;
      } else if (sum > target) {
        right--;
      }
    }
  }

  return closestSum;
}
