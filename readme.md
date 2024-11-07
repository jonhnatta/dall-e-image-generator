## Introduction

This project uses the GPT model to generate images and display them using Streamlit. Through a simple interface, users can interact with the model and view the generated images in real-time.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jonhnatta/dall-e-image-generator.git
   cd dall-e-image-generator
   ```

2. Create a virtual environment (optional, but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

3. Install the necessary libraries:

   ```bash
   pip install streamlit python-dotenv openai requests
   ```

4. Configure your OpenAI API key:

   Create a `.env` file in the root of the project and add your API key:

   ```
   OPENAI_API_KEY=yourapikeyhere
   ```

## Running the Project

To start the Streamlit application, run the following command:

```bash
streamlit run main.py
```