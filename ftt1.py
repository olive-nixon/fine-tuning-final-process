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

#Using the provided file_id
file_id = "file-3b0Za6FiLCs0F3KdhKSjXDB6"
model_name = "gpt-3.5-turbo" #Or another base model if you prefer

response = openai.FineTuningJob.create(
    training_file=file_id,
    model=model_name,
    hyperparameters={
        "n_epochs":50
    }
)

job_id = response['id']
# job_id = response
print(f"Fine-tuning job created successfully with ID: {job_id}")