# week1day8_fixed.py

cash = int(input())
prices = list(map(int, input().split()))

# BNP 전략
bnp_cash = cash
bnp_stock = 0
for price in prices:
    if price <= bnp_cash:
        count = bnp_cash // price
        bnp_stock += count
        bnp_cash -= count * price

# TIMING 전략
timing_cash = cash
timing_stock = 0

for i in range(3, len(prices)):
    prev1, prev2, prev3 = prices[i - 1], prices[i - 2], prices[i - 3]
    today = prices[i]

    if prev3 < prev2 < prev1:  # 3일 연속 상승 → 다음날 하락 예측 → 매도
        timing_cash += timing_stock * today
        timing_stock = 0
    elif prev3 > prev2 > prev1:  # 3일 연속 하락 → 다음날 상승 예측 → 매수
        count = timing_cash // today
        timing_stock += count
        timing_cash -= count * today

# 자산 계산
final_price = prices[-1]
bnp_total = bnp_cash + bnp_stock * final_price
timing_total = timing_cash + timing_stock * final_price

if bnp_total > timing_total:
    print("BNP")
elif bnp_total < timing_total:
    print("TIMING")
else:
    print("SAMESAME")
