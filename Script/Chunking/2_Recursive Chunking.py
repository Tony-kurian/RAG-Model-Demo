from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Sample long-form text
# The 'with' statement automatically closes the file for you

with open(r'C:\Users\248740\Desktop\RAG\RAG-Model-Demo\Data\ai_basics.txt', 'r', encoding='utf-8') as file:
    raw_text = file.read()

# 2. Initialize the splitter
# We use a small chunk_size here to demonstrate the splitting
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,                      # Set the maximum size of each chunk (in characters)
    chunk_overlap=20,                    # Set the number of characters to overlap between chunks to maintain context
    length_function=len,                 # Use the built-in len function to measure text length
    separators=["\n\n", "\n", " ", ""]   # Define the hierarchy of separators for splitting  or is_separator_regex=False
    #is_separator_regex=False
)

# 3. Create the chunks
chunks = text_splitter.split_text(raw_text)


# 4. Preview the results
for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(chunk.strip())