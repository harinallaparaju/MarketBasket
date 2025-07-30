## 🛒 Market Basket Analysis Dashboard

Hello. I'm an MTech Computer Science student at NIT Warangal, and this is my **Interactive Market Basket Analysis Dashboard**—a project I built to dive deep into grocery store transaction data and uncover hidden purchasing patterns.  

**Live Demo:** https://marketbaskett.streamlit.app

### Project Overview

This dashboard uses Market Basket Analysis to reveal customer purchasing behaviors, helping businesses optimize marketing, product placement, and cross-selling strategies. I built it with **Streamlit** to make it interactive and accessible, and it includes performance comparisons between two classic algorithms: **Apriori** and **FP-Growth**.

### Key Insights

Here’s what I uncovered while working on this project:

1. **Algorithm Performance:** Surprisingly, the **Apriori algorithm outperformed FP-Growth** on this sparse grocery dataset. This was an eye-opener, as it challenges the common belief that FP-Growth is always faster. It taught me how dataset characteristics (like sparsity) can flip theoretical expectations!
   
2. **Top Association Rule:** One of the strongest patterns I found was:
   - **Rule:** `{yogurt, whole milk} → {sausage}`
   - **Lift: 2.18** — Customers buying yogurt and whole milk are **2.18 times more likely** to grab sausages, hinting at a "breakfast bundle" trend.

### Business Recommendations

Based on the analysis, I proposed these strategies to turn insights into action:

1. **"Breakfast Bundle" Promo:** Offer a discount when customers buy `yogurt`, `whole milk`, and `sausage` together to boost sales.
2. **Smart Store Layout:** Place a small sausage display near the dairy aisle to spark impulse purchases.
3. **Personalized Marketing:** For online shoppers, suggest sausages when `yogurt` and `whole milk` are added to their cart.

### Tech Stack

- **Data Analysis:** `pandas`, `mlxtend`
- **Dashboard:** `streamlit` for a polished, interactive UI
- **Visualization:** `matplotlib`, `seaborn` for clear, insightful charts
