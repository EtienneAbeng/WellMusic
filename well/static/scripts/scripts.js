function playAudio(songId) {
  var audio = document.getElementById('audio-' + songId);
  audio.play();
}

function pauseAudio(songId) {
  var audio = document.getElementById('audio-' + songId);
  audio.pause();
}

function fastForwardAudio(songId) {
  var audio = document.getElementById('audio-' + songId);
  audio.currentTime += 10; // Fast forward by 10 seconds
}

function rewindAudio(songId) {
  var audio = document.getElementById('audio-' + songId);
  audio.currentTime -= 10; // Rewind by 10 seconds
}

function stopAudio(songId) {
  var audio = document.getElementById('audio-' + songId);
  audio.pause();
  audio.currentTime = 0;
}

const audioPlayer = document.querySelector('#audio-player');
const playBtn = document.querySelector('.play-btn');
const controls = document.querySelector('#controls');

playBtn.addEventListener('click', () => {
  if (audioPlayer.paused) {
    audioPlayer.play();
    playBtn.classList.remove('fa-play');
    playBtn.classList.add('fa-pause');
  } else {
    audioPlayer.pause();
    playBtn.classList.remove('fa-pause');
    playBtn.classList.add('fa-play');
  }
});

controls.addEventListener('click', (event) => {
  if (event.target.tagName === 'I') {
    event.target.parentNode.classList.toggle('active');
  }
});
