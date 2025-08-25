// Time: O(n) / Space: O(n)
function reverseWords(s: string): string {
  let reversedWords = [];
  let i = s.length - 1;

  while (i >= 0) {
    // Skip spaces
    while (i >= 0 && s[i] === " ") {
      i--;
    }

    // Reached start
    if (i < 0) {
      break;
    }

    // End index of current word
    let end = i;

    while (i >= 0 && s[i] !== " ") {
      i--;
    }

    let start = i + 1;

    reversedWords.push(s.slice(start, end + 1));
  }
  return reversedWords.join(" ");
}
