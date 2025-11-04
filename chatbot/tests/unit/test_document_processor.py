import pytest
from unittest.mock import patch, MagicMock
from src.services import document_processor

@patch('src.services.document_processor.OpenAIEmbeddings')
@patch('src.services.document_processor.get_chroma_client')
def test_process_document_txt(mock_get_chroma_client, mock_openai_embeddings):
    # Arrange
    mock_collection = MagicMock()
    mock_client = MagicMock()
    mock_client.get_or_create_collection.return_value = mock_collection
    mock_get_chroma_client.return_value = mock_client

    mock_embeddings_instance = MagicMock()
    mock_openai_embeddings.return_value = mock_embeddings_instance

    file_path = "test.txt"
    with open(file_path, "w") as f:
        f.write("This is a test document.")

    # Act
    document_processor.process_document(file_path, "txt")

    # Assert
    mock_openai_embeddings.assert_called_once()
    mock_get_chroma_client.assert_called_once()
    mock_collection.add.assert_called_once()

    # Cleanup
    import os
    os.remove(file_path)
