// Time: O(n) / Space: O(1)
function maxProfit(prices: number[]): number {
  let minPrice = Infinity;
  let maxProfit = 0;

  for (const price of prices) {
    if (price < minPrice) {
      minPrice = price;
    } else {
      let profit = price - minPrice;
      if (profit > maxProfit) {
        maxProfit = profit;
      }
    }
  }
  return maxProfit;
}
