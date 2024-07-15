document.getElementById('drop-area').addEventListener('click', () => {
    document.getElementById('file-input').click();
});

document.getElementById('file-input').addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        previewImage(file);
    }
});

document.addEventListener('paste', (event) => {
    const items = (event.clipboardData || event.originalEvent.clipboardData).items;
    for (const item of items) {
        if (item.kind === 'file') {
            const file = item.getAsFile();
            previewImage(file);
            break;
        }
    }
});

function previewImage(file) {
    const img = document.getElementById('preview');
    const reader = new FileReader();
    reader.onload = (event) => {
        img.src = event.target.result;
        img.style.display = 'block';
    };
    reader.readAsDataURL(file);
}
