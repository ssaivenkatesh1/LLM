const uploadForm = document.getElementById('upload-form');
const audioFile = document.getElementById('audio-file');
const structuredNote = document.getElementById('structured-note');
const taskList = document.getElementById('task-list');

uploadForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('file', audioFile.files[0]);

    const response = await fetch('/upload-audio/', {
        method: 'POST',
        body: formData,
    });

    const results = await response.json();

    structuredNote.innerHTML = results.structured_note.replace(/\n/g, '<br>');
    taskList.innerHTML = ''; // Clear existing content
    const tasksArray = results.tasks.split('\n').map(task => task.trim()).filter(task => task.length > 0);
    taskList.innerHTML = tasksArray.join('<br>');
});
