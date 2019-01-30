window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition
// var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList
// var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent

// var departments = ['computer', 'civil', 'chemical']
const recognition = new SpeechRecognition();
recognition.interimResults = true;

var text = document.getElementById('input_message');

recognition.addEventListener('result', e => {
    const transcript = Array.from(e.results)
        .map(results => results[0])
        .map(results => results.transcript)
        .join('')
    text.value = transcript;       
});
function speak(){
    recognition.start();
}
