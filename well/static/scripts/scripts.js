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
  audio.currentTime += 10; 
}

function rewindAudio(songId) {
  var audio = document.getElementById('audio-' + songId);
  audio.currentTime -= 10; 
}

function stopAudio(songId) {
  var audio = document.getElementById('audio-' + songId);
  audio.pause();
  audio.currentTime = 0;
}

// Ajoutez cet écouteur d'événement pour jouer la chanson sélectionnée dans la page songs.html
document.addEventListener('DOMContentLoaded', function() {
  var songItems = document.querySelectorAll('.song-item');
  for (var i = 0; i < songItems.length; i++) {
    var songItem = songItems[i];
    songItem.addEventListener('click', function() {
      var audio = this.querySelector('audio');
      if (audio.paused) {
        audio.play();
      } else {
        audio.pause();
      }
    });
  }
});

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
