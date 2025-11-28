# app.py
import json
import streamlit as st
import re
from collections import Counter

# Load FAQs
with open("faqs.json", "r", encoding="utf-8") as f:
    FAQs = json.load(f)

def normalize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    return text

def score_query(query, text):
    q_tokens = normalize(query).split()
    t_tokens = normalize(text).split()
    q_counts = Counter(q_tokens)
    t_counts = Counter(t_tokens)
    # score is total overlapping token counts
    score = sum(min(q_counts[w], t_counts[w]) for w in q_counts)
    return score

st.set_page_config(page_title="Support Assistant (FAQ Bot)", layout="centered")
st.title("Support Assistant - FAQ Bot")
st.write("Ask any question and I'll try to answer from the FAQ.")

user_q = st.text_input("Your question:")

if st.button("Get Answer") and user_q.strip():
    scored = []
    for faq in FAQs:
        s = score_query(user_q, faq["question"] + " " + faq["answer"])
        scored.append((s, faq))
    scored.sort(key=lambda x: x[0], reverse=True)
    top_score, top_faq = scored[0]

    if top_score == 0:
        st.warning("I couldn't find a close match in the FAQ. Try rephrasing your question.")
    else:
        st.subheader("Best match from FAQ")
        st.write("**Q:**", top_faq["question"])
        st.write("**A:**", top_faq["answer"])

        if len(scored) > 1 and scored[1][0] > 0:
            st.write("---")
            st.write("Other possible matches:")
            for s, f in scored[1:4]:
                if s > 0:
                    st.write("- ", f["question"])
