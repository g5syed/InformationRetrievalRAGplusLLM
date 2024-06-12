# Precise Information Retrieval Using RAG and LLM

This repository houses the code and documentation for the "Precise Information Retrieval Using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs)" project, as detailed in the project report by Danish Faiz for COMP8420 Advanced Natural Language Processing, Assignment 3.

## Project Overview

The project aims to address the limitations of traditional information retrieval systems by integrating Retrieval-Augmented Generation (RAG) with GPT-4. This combination offers a dynamic, scalable, and efficient method to process and retrieve information, providing accurate and context-aware responses to complex queries.

### Objectives

- **Enhance Precision:** Improve the precision of information retrieval by integrating RAG with GPT-4.
- **Increase Efficiency:** Reduce the time and computational resources required for retrieving information.
- **Scalability:** Develop a scalable solution that can handle increasing amounts of data without performance degradation.

## Repository Structure
```
/
|- app.py                # Main application script
|- dropdown.py           # Module for dropdown menu functionality
|- Project8420.ipynb     # Jupyter notebook with implementation details
|- sampledata.pdf        # Sample Data file (actual data report of a company)
|- README.md             # This file
```

## System Architecture

The system architecture is designed to facilitate high-volume data transactions and is scalable to accommodate future expansions. It includes data preprocessing modules, a retrieval engine, the GPT-4 integration interface, and post-processing units for refining responses.
![alt text]([https://github.com/g5syed/InformationRetrievalRAGplusLLM/blob/main/Retrieval-Augmented%20Generation%20Process.webp])

### Key Components

- **Data Preprocessing:** Cleansing, tagging, and indexing data using NLP techniques.
- **Retrieval Engine:** Customized engine that interacts efficiently with GPT-4 for fetching pertinent information.
- **GPT-4 Integration:** API calls to GPT-4 for processing retrieved information and generating responses.
- **Response Generation and Refinement:** Ensuring the relevance and accuracy of the generated responses.

## Setup and Installation

```bash
# Clone the repository
git clone https://github.com/g5syed/InformationRetrievalRAGplusLLM
cd InformationRetrievalRAGplusLLM

# Install dependencies (Assuming Python environment)
pip install -r requirements.txt

# Run the application
python app.py
```

## Data Collection and Processing

Data for this project is primarily sourced from detailed reports available in PDF format. A Python script has been developed for efficiently extracting text from these documents, converting it into a machine-readable format suitable for processing by the RAG system.

## Usage

Refer to the `Project8420.ipynb` notebook for detailed usage examples and implementation specifics.

## Future Work

Future enhancements will focus on:
- Advanced data processing techniques.
- Expansion into new industries.
- Improvement of the user interface.
- Integration with additional AI technologies.

## References

1. [Retrieval-Augmented Generation: Keeping LLMs Relevant and Current](https://stackoverflow.blog/2023/10/18/retrieval-augmented-generation-keeping-llms-relevant-and-current)
2. [Understanding RAG: Retrieval-Augmented Generation Explained](https://www.6clicks.com/resources/blog/understanding-rag-retrieval-augmented-generation-explained)

## License

This project is a personal assessment for Macquarie University use only
