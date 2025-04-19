document.addEventListener('DOMContentLoaded', () => {
    const textarea = document.getElementById('input_text');
    const charCount = document.getElementById('char-count');
    const resetButton = document.getElementById('reset-button');
    const timeDisplay = document.getElementById('time-display');

    // Update character count in real-time
    textarea.addEventListener('input', () => {
        charCount.textContent = `Character count: ${textarea.value.length}`;
    });

    // Clear the form
    resetButton.addEventListener('click', (e) => {
        e.preventDefault();
        if (confirm('Are you sure you want to clear the text?')) {
            textarea.value = '';
            charCount.textContent = 'Character count: 0';
        }
    });

    // Function to update the time
    function updateTime() {
        const now = new Date();
        const options = { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true };
        timeDisplay.textContent = now.toLocaleTimeString(undefined, options);
    }

    // Update time every second
    setInterval(updateTime, 1000);
    updateTime(); // initial call to display the time immediately
});
