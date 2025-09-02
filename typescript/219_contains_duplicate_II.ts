// Time: O(n) / Space: O(n)
function containsNearbyDuplicate(nums: number[], k: number): boolean {
  const seen = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (seen.has(num) && i - seen.get(num) <= k) {
      return true;
    }
    seen.set(num, i);
  }
  return false;
}
