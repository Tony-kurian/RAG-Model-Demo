from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)

# Raw text dataset
raw_text_1 = (
    "LangChain is a framework for developing applications powered by language models. "
    "It enables applications that are context-aware and reason-based."
)
raw_text_2 = "Text splitting is a crucial preprocessing step for building efficient RAG pipelines."


print("=" * 60)
print("METHOD 1: .split_text()")
print("=" * 60)
# INPUT: A single string
# OUTPUT: A list of strings (no metadata)
string_chunks = splitter.split_text(raw_text_1)

print(f"Returned Type: {type(string_chunks)}")
for i, chunk in enumerate(string_chunks, 1):
    print(f"  -> Chunk {i}: '{chunk}'")


print("\n" + "=" * 60)
print("METHOD 2: .create_documents()")
print("=" * 60)
# INPUT: A list of raw strings + optional metadata
# OUTPUT: A list of LangChain Document objects
texts_to_convert = [raw_text_1, raw_text_2]
custom_metadata = [{"source": "docs_site"}, {"source": "blog_post"}]

created_docs = splitter.create_documents(texts=texts_to_convert, metadatas=custom_metadata)

print(f"Returned Type: {type(created_docs)}")
for i, doc in enumerate(created_docs, 1):
    print(f"  -> Doc {i} Metadata: {doc.metadata}")
    print(f"     Doc {i} Content : '{doc.page_content}'")


print("\n" + "=" * 60)
print("METHOD 3: .split_documents()")
print("=" * 60)
# INPUT: A list of pre-existing Document objects (e.g., from a PDF or Web loader)
# OUTPUT: A list of smaller Document objects (metadata is copied over automatically)
loaded_documents = [
    Document(page_content=raw_text_1, metadata={"file_name": "manual.pdf", "page": 12})
]

split_docs = splitter.split_documents(loaded_documents)

print(f"Returned Type: {type(split_docs)}")
for i, doc in enumerate(split_docs, 1):
    print(f"  -> Chunk {i} Metadata: {doc.metadata}")
    print(f"     Chunk {i} Content : '{doc.page_content}'")


print("\n" + "=" * 60)
print("METHOD 4: .transform_documents()")
print("=" * 60)
# INPUT/OUTPUT: Identical to split_documents, but uses LangChain's pipeline standard
transformed_docs = splitter.transform_documents(loaded_documents)

print(f"Returned Type: {type(transformed_docs)}")
print(f"Total chunks created via transformation pipeline: {len(transformed_docs)}")
print(f"First transformed chunk content: '{transformed_docs[0].page_content}'")
print("=" * 60)