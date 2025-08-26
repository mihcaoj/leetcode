function lengthOfLongestSubstring(s: string): number {
  let longest = 0;
  let left = 0;
  const seen = new Map<string, number>();

  for (let right = 0; right < s.length; right++) {
    const char = s[right];

    if (seen.has(char) && seen.get(char)! >= left) {
      left = seen.get(char)! + 1; // move left pointer past duplicate
    }

    seen.set(char, right); // update last seen index
    longest = Math.max(longest, right - left + 1);
  }
  return longest;
}
