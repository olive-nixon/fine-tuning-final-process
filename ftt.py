import openai

#define a function to open a file and return its contents as a string
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
#Define a function to save content to a file
def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.write(content)
        
#Set the OpenAI API keys by reading them form files
api_key = open_file('openaiapikey2.txt')

openai.api_key = api_key

#Assuming the file name is 'processed_data.jsonl'
with open("toyft1.jsonl", 'rb') as file:
    response = openai.File.create(
        file = file,
        purpose = 'fine-tune'
    )
    
file_id = response['id']
print(f"File uploaded successfully with ID: {file_id}")