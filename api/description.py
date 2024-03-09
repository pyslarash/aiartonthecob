from openai import OpenAI
from dotenv import load_dotenv
import os
import re

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
# Replace spaces with underscores and convert to lowercase
def format_keyword(keyword):
    formatted_keyword = keyword.replace(" ", "_").lower()
    return formatted_keyword
        
# Writing Etsy description
def etsy_title(keyword):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a highly-skilled Etsy marketer who is focused on keyword-centric Etsy titles."},
        {"role": "user", "content": f"Write an Etsy title using for a keyword '{keyword}' somewhere in the beginning. You are selling a pack of downloadable digital prints. The title should be at least 100 characters, but no longer than 140 characters. Utilize the jeywords in title separated by | sign."}
    ]
    )

    return(completion.choices[0].message.content)

# Writing product description   
def etsy_description(keyword):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a highly-skilled Etsy marketer who is focused on keyword-centric Etsy descriptions."},
        {"role": "user", "content": f"Write a lengthy description for a keyword '{keyword}' for a pacl of downloadable digital prints created by AI. It should be a minimum of 400 words. Do not overuse the keyword, but use it enough times. The print will have 300dpi suitable for prints with up to 20 inches; the images are square. Use human-like writing style and avoid detection by ChatGPT detectors."}
    ]
    )
    return completion.choices[0].message.content

# Writing tags  
def etsy_tags(keyword):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a highly-skilled Etsy marketer who is focused on kEtsy keywords."},
        {"role": "user", "content": f"Write 13 Etsy keywords separated by commas; we are focusing on the keyword '{keyword}'. You are selling a pack of downloadable digital prints. Do not overuse the keyword in the tags. Each tag should be no longer than 20 characters!"}
    ]
    )

    return(completion.choices[0].message.content)

# Combining everything
def description_creation(keyword):
    title = etsy_title(keyword)
    description = etsy_description(keyword)
    tags = etsy_tags(keyword)
    return title, description, tags