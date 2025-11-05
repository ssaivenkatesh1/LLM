document.addEventListener('DOMContentLoaded', () => {
    const pdfFile = document.getElementById('pdfFile');
    const summarizeBtn = document.getElementById('summarizeBtn');
    const loadingDiv = document.getElementById('loading');
    const summaryResultDiv = document.getElementById('summaryResult');
    const summaryTextP = document.getElementById('summaryText');
    const wordCountsP = document.getElementById('wordCounts');
    const errorMessageDiv = document.getElementById('errorMessage');

    summarizeBtn.addEventListener('click', async () => {
        const file = pdfFile.files[0];
        if (!file) {
            errorMessageDiv.textContent = 'Please select a PDF file.';
            errorMessageDiv.classList.remove('hidden');
            return;
        }

        loadingDiv.classList.remove('hidden');
        errorMessageDiv.classList.add('hidden');
        summaryResultDiv.classList.add('hidden');

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('/api/summarize', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();

            if (response.ok) {
                summaryTextP.textContent = data.summary_text;
                wordCountsP.textContent = `Original words: ${data.original_word_count}, Summary words: ${data.summary_word_count}`;
                summaryResultDiv.classList.remove('hidden');
            } else {
                errorMessageDiv.textContent = data.detail || 'An unknown error occurred.';
                errorMessageDiv.classList.remove('hidden');
            }
        } catch (error) {
            errorMessageDiv.textContent = 'Failed to connect to the summarization service.';
            errorMessageDiv.classList.remove('hidden');
            console.error('Fetch error:', error);
        } finally {
            loadingDiv.classList.add('hidden');
        }
    });
});
