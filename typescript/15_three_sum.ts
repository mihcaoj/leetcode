// Time: O(n^2) / Space: O(1)
function threeSum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b); // sort ascending
  let result: number[][] = [];
  let n = nums.length;

  for (let i = 0; i < n - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = n - 1;
    while (left < right) {
      let total = nums[i] + nums[left] + nums[right];

      if (total < 0) {
        left++;
      } else if (total > 0) {
        right--;
      } else {
        result.push([nums[i], nums[left], nums[right]]);

        // skip duplicate second numbers
        while (left < right && nums[left] === nums[left + 1]) left++;
        // skip duplicate third numbers
        while (left < right && nums[right] === nums[right - 1]) right--;

        left++;
        right--;
      }
    }
  }

  return result;
}
