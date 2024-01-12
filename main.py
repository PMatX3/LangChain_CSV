import csv
import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_community.llms import OpenAI
from dotenv import load_dotenv  


def parse_csv(csv_file):
    processed_data = []
    reader = csv.reader(csv_file.decode('utf-8-sig').splitlines())
    for row in reader:
        processed_data.append(row)
    return processed_data

def main():
    load_dotenv()
    st.set_page_config(page_title="Best Candidate AI 😀::")
    st.header("Best Candidate AI")

    user_csv = st.file_uploader("Upload a CSV file", type=["csv"])

    if user_csv is not None:
        user_question = st.text_input("Ask your question about here:")

        processed_csv_data = parse_csv(user_csv)
        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, processed_csv_data, verbose=True)

        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            st.write(response)



if __name__ == '__main__':
    main()