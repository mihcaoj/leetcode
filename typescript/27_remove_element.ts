// Splice solution (Time: O(n^2) / Space: O(1))
function removeElement(nums: number[], val: number): number {
  let i = 0;

  while (i < nums.length) {
    if (nums[i] === val) {
      nums.splice(i, 1);
    } else {
      i++;
    }
  }
  return nums.length;
}

// Two-pointer solution (Time: O(n) / Space: O(1))
function removeElementTwo(nums: number[], val: number): number {
  let k = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      nums[k] = nums[i];
      k++;
    }
  }

  return k;
}
