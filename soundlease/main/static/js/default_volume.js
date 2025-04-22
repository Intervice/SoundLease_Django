document.addEventListener('DOMContentLoaded', function() {
  const audioElements = document.querySelectorAll('.beat-song');
  audioElements.forEach(audio => {
    audio.volume = 0.4;
  });
});