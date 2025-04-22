document.addEventListener('DOMContentLoaded', function() {
  const beatImages = document.querySelectorAll('.beat-image');
  const audios = document.querySelectorAll('audio');

  beatImages.forEach(image => {
    image.addEventListener('click', () => {
      const audioId = image.dataset.audioId;
      const currentAudio = document.getElementById(audioId);

      if (!currentAudio) {
        return;
      }

      audios.forEach(audio => {
        if (audio.id !== audioId) {
          audio.pause();
          audio.currentTime = 0;
        }
      });

      if (currentAudio.paused) {
        currentAudio.play();
      } else {
        currentAudio.pause();
      }
    });
  });
});