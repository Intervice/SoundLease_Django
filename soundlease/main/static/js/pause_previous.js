document.addEventListener('play', function(event) {
  const audioElements = document.querySelectorAll('audio');
  audioElements.forEach(audio => {
    // Перевіряємо, чи це не той аудіо елемент, на якому щойно натиснули "play"
    if (audio !== event.target) {
      audio.pause();
      // Додатково можна скинути час відтворення на початок
      audio.currentTime = 0;
    }
  });
}, true);