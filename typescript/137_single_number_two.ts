// Time: O(n) / Space: O(1)
function singleNumber(nums: number[]): number {
  let ones = 0;
  let twos = 0;

  for (let i = 0; i < nums.length; i++) {
    ones = (ones ^ nums[i]) & ~twos;
    twos = (twos ^ nums[i]) & ~ones;
  }

  return ones;
}
