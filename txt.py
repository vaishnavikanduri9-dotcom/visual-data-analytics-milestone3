import chromadb
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(
     name="safety_docs" 
)
print("Collection created successfully!") 
print("Collection name:", collection.name) 
print("Documents:", collection.count())