// Time: O(n) / Space: O(1)
function maxArea(height: number[]): number {
  let i = 0;
  let j = height.length - 1;
  let maxArea = 0;

  while (i < j) {
    let width = j - i;
    let minHeight = Math.min(height[i], height[j]);
    let area = width * minHeight;
    maxArea = Math.max(maxArea, area);

    if (height[i] < height[j]) {
      i++;
    } else {
      j--;
    }
  }
  return maxArea;
}
