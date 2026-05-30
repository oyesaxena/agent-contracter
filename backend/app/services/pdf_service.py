from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader
)


def load_pdf(file_path: str):

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    full_text = "\n".join(
        doc.page_content
        for doc in documents
    )

    file_stats = Path(file_path).stat()

    first_page_metadata = (
        documents[0].metadata
        if documents
        else {}
    )

    metadata = {

        # file metadata
        "file_name": Path(file_path).name,

        "file_size_bytes": file_stats.st_size,

        # pdf metadata
        "page_count": len(documents),

        "source": first_page_metadata.get(
            "source"
        ),

        "author": first_page_metadata.get(
            "author"
        ),

        "creator": first_page_metadata.get(
            "creator"
        ),

        "producer": first_page_metadata.get(
            "producer"
        ),

        "creation_date": first_page_metadata.get(
            "creationdate"
        ),

        "modification_date": first_page_metadata.get(
            "moddate"
        )
    }

    return {
        "text": full_text,
        "metadata": metadata,
        "documents": documents
    }