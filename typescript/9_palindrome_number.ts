// Time: O(n) / Space: O(n)
function isPalindrome(x: number): boolean {
  let stringNum = x.toString();

  for (let i = 0; i < stringNum.length / 2; i++) {
    if (stringNum[i] !== stringNum[stringNum.length - 1 - i]) {
      return false;
    }
  }
  return true;
}
