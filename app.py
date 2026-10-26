
import asyncio
import streamlit as st

from research_agent import search_web, summarize_research

st.set_page_config(
    page_title="AI Web Research Agent",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 AI Web Research Agent")
st.write(
    "Research a topic using Bright Data web search "
    "and generate a summary using OpenAI."
)

query = st.text_input(
    "What would you like to research?",
    placeholder="e.g. What is Model Context Protocol?",
)

if st.button("Search and Generate Report", type="primary"):
    if not query.strip():
        st.warning("Please enter a research question.")
    else:
        try:
            with st.spinner("Searching the web with Bright Data..."):
                results = asyncio.run(search_web(query.strip()))

            if not results or results.startswith(
                "No organic search results"
            ):
                st.warning("No search results were found. Try another query.")
            else:
                with st.spinner("Generating your research report with OpenAI..."):
                    report = summarize_research(query.strip(), results)

                st.subheader("Research Report")
                st.markdown(report)

                with st.expander("View search results"):
                    st.text(results)

        except Exception as error:
            st.error(f"Something went wrong: {type(error).__name__}: {error}")
