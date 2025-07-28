# app.py

import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

# --- Page Configuration ---
st.set_page_config(
    page_title="Market Basket Insights",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="auto"
)


# --- Load Data and Analysis Functions ---
@st.cache_data
def load_data():
    """Loads and preprocesses the dataset."""
    try:
        df = pd.read_csv('data/Groceries_dataset.csv')
        transactions_df = df.groupby(['Member_number', 'Date'])['itemDescription'].apply(list).reset_index(name='items')
        transactions = transactions_df['items'].tolist()

        te = TransactionEncoder()
        te_ary = te.fit(transactions).transform(transactions)
        return pd.DataFrame(te_ary, columns=te.columns_)
    except FileNotFoundError:
        st.error("Error loading dataset: `data/Groceries_dataset.csv` not found.")
        return None


@st.cache_data
def analyze_market_basket(df, min_support, min_lift):
    """Performs market basket analysis and returns association rules."""
    frequent_itemsets = fpgrowth(df, min_support=min_support, use_colnames=True)

    if frequent_itemsets.empty:
        return pd.DataFrame()

    rules = association_rules(frequent_itemsets, metric='lift', min_threshold=min_lift)

    # Convert frozensets to readable strings
    rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
    rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))

    return rules.sort_values('lift', ascending=False)


# Load data
df_encoded = load_data()

# --- Streamlit UI ---
st.markdown("## 🛒 Market Basket Insights")
st.subheader("Association Rule Mining for Retail Analytics")
st.markdown("""
This tool analyzes shopping patterns to discover which products are frequently bought together. 
It helps retailers optimize product placement, create targeted promotions, and improve customer experience.
""")

st.markdown("---")

if df_encoded is not None:
    # --- Analysis Parameters ---
    st.write("### Analysis Parameters")

    col1, col2 = st.columns(2)

    with col1:
        min_support = st.slider(
            "Minimum Support",
            min_value=0.001,
            max_value=0.02,
            value=0.003,
            step=0.001,
            format="%.3f",
            help="Minimum frequency threshold - items must appear together in at least this percentage of transactions"
        )

    with col2:
        min_lift = st.slider(
            "Minimum Lift",
            min_value=1.0,
            max_value=5.0,
            value=2.0,
            step=0.1,
            help="How much more likely items are to be bought together compared to random chance"
        )

    if st.button('Analyze Shopping Patterns'):
        if df_encoded is not None:
            # Perform analysis
            with st.spinner('Analyzing shopping patterns...'):
                rules = analyze_market_basket(df_encoded, min_support, min_lift)

            # Display results
            st.markdown("---")
            st.write("### Analysis Results")

            if rules.empty:
                st.warning("No strong association rules found with current parameters. Try lowering the thresholds.")
            else:
                # Show number of rules found
                progress_bar = st.progress(0)
                progress_bar.progress(100, text=f"Found {len(rules)} association rules")

                st.success(f"**Discovered {len(rules)} strong association rules**")

                # Display top rules in a clean table
                st.write("#### Top Association Rules")
                display_rules = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10)

                st.dataframe(
                    display_rules.style.format({
                        'support': '{:.2%}',
                        'confidence': '{:.2%}',
                        'lift': '{:.2f}'
                    }),
                    use_container_width=True,
                    hide_index=True
                )

                # Highlight the strongest rule
                if not rules.empty:
                    st.write("#### Key Business Insight")
                    top_rule = rules.iloc[0]

                    # Display key metrics
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Support", f"{top_rule['support']:.2%}")
                    col2.metric("Confidence", f"{top_rule['confidence']:.2%}")
                    col3.metric("Lift", f"{top_rule['lift']:.2f}x")

                    st.info(
                        f"**Strongest Pattern:** Customers who buy **{top_rule['antecedents']}** are "
                        f"**{top_rule['lift']:.1f}x more likely** to also purchase **{top_rule['consequents']}**. "
                        f"This happens in {top_rule['support']:.1%} of all transactions with {top_rule['confidence']:.1%} confidence.",
                        icon="💡"
                    )
        else:
            st.error("Dataset could not be loaded. Please check the file path.")
else:
    st.error("Unable to load the dataset. Please ensure `data/Groceries_dataset.csv` exists.")

st.markdown("---")
st.markdown(
    "Built for retail analytics and business intelligence. Discover hidden patterns in customer shopping behavior.")
st.markdown(
    "Built By Surya Nallaparaju.")