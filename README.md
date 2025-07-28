## 🛒 Market Basket Analysis Dashboard

Hello. I'm an MTech Computer Science student at NIT Warangal, and this is my **Interactive Market Basket Analysis Dashboard**—a project I built to dive deep into grocery store transaction data and uncover hidden purchasing patterns.  

### Project Overview

This dashboard uses Market Basket Analysis to reveal customer purchasing behaviors, helping businesses optimize marketing, product placement, and cross-selling strategies. I built it with **Streamlit** to make it interactive and accessible, and it includes performance comparisons between two classic algorithms: **Apriori** and **FP-Growth**.

### Key Features

- **Interactive Experience:** A sleek, Streamlit-based dashboard that lets users explore purchasing patterns effortlessly.
- **Customizable Analysis:** Adjust `min_support` and `min_lift` sliders to fine-tune association rules and discover insights.
- **Algorithm Showdown:** Real-time benchmarking of Apriori vs. FP-Growth, with insights into which performs better and why.
- **Business Impact:** Clear, actionable recommendations derived from the data to boost sales and customer engagement.

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

### How to Run the Project

Want to try it out? Here's how to get it running locally:

1. **Prerequisites:** Make sure you have **Python 3.7+** installed.
2. **Clone the Repository:** Grab the code from my GitHub repo and set up the project structure:
   ```
   market_basket_app/
   ├── app.py
   ├── data/
   │   └── Groceries_dataset.csv
   └── notebooks/
       └── market_basket.ipynb
   ```
3. **Install Dependencies:**
   ```bash
   pip install streamlit pandas mlxtend matplotlib seaborn
   ```
4. **Launch the Dashboard:**
   ```bash
   cd market_basket_app
   streamlit run app.py
   ```
5. Open your browser to the provided URL (usually `http://localhost:8501`) and explore!

### Tech Stack

- **Data Analysis:** `pandas`, `mlxtend`
- **Dashboard:** `streamlit` for a polished, interactive UI
- **Visualization:** `matplotlib`, `seaborn` for clear, insightful charts
