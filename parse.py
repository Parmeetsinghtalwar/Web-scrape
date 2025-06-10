from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

def parse_with_ollama(dom_chunks, parse_description):
    """
    Parse DOM content using Groq's Llama 3 model
    """
    # Initialize Groq with your API key
    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0,
        api_key="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"
    )
    
    # Create prompt template
    template = (
        "You are tasked with extracting specific information from the following text content: {dom_content}. "
        "Please follow these instructions: {parse_description}\n\n"
        "Extract the information accurately and format it clearly. If the requested information is not found, "
        "please state that clearly."
    )
    
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm
    
    parsed_results = []
    
    # Process each chunk
    for i, chunk in enumerate(dom_chunks):
        try:
            print(f"Processing chunk {i+1}/{len(dom_chunks)}...")
            
            # Invoke the chain with the chunk and description
            response = chain.invoke({
                "dom_content": chunk, 
                "parse_description": parse_description
            })
            
            parsed_results.append(response.content)
            
        except Exception as e:
            error_msg = f"Error processing chunk {i+1}: {str(e)}"
            print(error_msg)
            parsed_results.append(error_msg)
    
    # Combine all results
    final_result = "\n\n--- CHUNK SEPARATOR ---\n\n".join(parsed_results)
    return final_result
