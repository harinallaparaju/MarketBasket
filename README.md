## 🛒 Market Basket Analysis Dashboard

This project presents an interactive web dashboard for performing Market Basket Analysis on a grocery store's transaction data. The goal is to uncover purchasing patterns and generate data-driven business strategies for marketing, cross-selling, and store layout.

### Key Features

*   **Interactive Dashboard:** Built with Streamlit for a user-friendly experience.
*   **Dynamic Parameter Tuning:** Users can adjust `min_support` and `min_lift` thresholds to explore different rule strengths.
*   **Algorithm Benchmarking:** The dashboard provides a real-time performance comparison between the Apriori and FP-Growth algorithms.
*   **Actionable Insights:** Results are translated into clear, actionable business recommendations.

### Key Findings & Insights

1.  **Algorithm Performance:** A key finding was that on this sparse dataset, the classic **Apriori algorithm consistently outperformed FP-Growth**. This is a valuable real-world insight, demonstrating that the theoretical superiority of FP-Growth is not universal and depends on dataset characteristics like density.

2.  **Product Association:** The analysis uncovered several strong, non-obvious product associations. The top-ranked rule was:
    
    **Rule:** `{yogurt, whole milk} -> {sausage}`
    
    - **Lift: 2.18** — Customers who buy yogurt and whole milk together are **2.18 times more likely** to also buy sausage than the average customer.
    - This suggests a strong "breakfast" or "quick meal" purchasing pattern.

### Business Recommendations

Based on the findings, the following strategies are recommended:

1.  **Create a "Breakfast Bundle" Promotion:** Offer a discount when `yogurt`, `whole milk`, and `sausage` are purchased together.
2.  **Strategic Product Placement:** Place sausages in a secondary, refrigerated display near the dairy aisle to encourage impulse buys from customers already purchasing milk and yogurt.
3.  **Targeted Online Marketing:** If a customer adds both milk and yogurt to their online cart, trigger a recommendation for sausages.

### How to Run Locally

1.  **Prerequisites:** Ensure you have Python 3.7+ installed.
2.  **Clone the repository and set up the project folder structure:**
    ```
    market_basket_app/
    ├── app.py
    ├── data/
    │   └── Groceries_dataset.csv
    └── notebooks/
        └── market_basket.ipynb
    ```
3.  **Install dependencies:**
    ```bash
    pip install streamlit pandas mlxtend matplotlib seaborn
    ```
4.  **Run the Streamlit app from the `market_basket_app` directory:**
    ```bash
    streamlit run app.py
    ```
5.  Open your web browser to the URL provided (e.g., `http://localhost:8501`).

### Libraries Used

*   **Analysis:** `pandas`, `mlxtend`
*   **Dashboard & UI:** `streamlit`
*   **Visualization:** `matplotlib`, `seaborn`