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