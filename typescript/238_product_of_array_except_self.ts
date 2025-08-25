// Time: O(n) / Space: O(n)
function productExceptSelf(nums: number[]): number[] {
  const output = new Array(nums.length).fill(1);

  // Forward pass: compute prefix products
  let product = 1;
  for (let i = 0; i < nums.length; i++) {
    output[i] = product;
    product *= nums[i];
  }

  // Backward pass: compute suffix products
  product = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    output[i] *= product;
    product *= nums[i];
  }
  return output;
}
