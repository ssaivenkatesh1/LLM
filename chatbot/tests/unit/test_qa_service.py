import pytest
from unittest.mock import patch, MagicMock
from src.services import qa_service

@patch('src.services.qa_service.RetrievalQA')
@patch('src.services.qa_service.OpenAI')
@patch('src.services.qa_service.Chroma')
@patch('src.services.qa_service.OpenAIEmbeddings')
@patch('src.services.qa_service.get_chroma_client')
def test_answer_question(mock_get_chroma_client, mock_openai_embeddings, mock_chroma, mock_openai, mock_retrieval_qa):
    # Arrange
    mock_qa_chain = MagicMock()
    mock_qa_chain.run.return_value = "This is the answer."
    mock_retrieval_qa.from_chain_type.return_value = mock_qa_chain

    # Act
    response = qa_service.answer_question("What is the answer?")

    # Assert
    mock_retrieval_qa.from_chain_type.assert_called_once()
    mock_qa_chain.run.assert_called_with("What is the answer?")
    assert response == "This is the answer."
