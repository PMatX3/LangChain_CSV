import openai

# Set up your OpenAI API key
openai.api_key = "your-openai-api-key"

def analyze_text(input_text):
    """
    Function to analyze a given text using OpenAI's API
    and extract key details such as skills, experiences, and summary.
    """
    prompt = f"""
    Extract the following details from the given text:
    - Key Skills
    - Work Experiences
    - Summary

    Text: {input_text}
    """
    try:
        # Make an API call to OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )
        # Extract the response text
        extracted_details = response.choices[0].text.strip()
        return extracted_details

    except Exception as e:
        return f"Error: {e}"

# Sample input text
resume_text = """
John Doe is a software engineer with 5 years of experience in full-stack development.
He has worked on building scalable web applications and has expertise in Python, JavaScript, and React.
John 
