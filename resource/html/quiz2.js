console.log(window.navigator.vendor);

// note: Google Inc works with Edge and Chrome
// note: works with firefox
// TODO: go back and make this work in IE (my coworkers are really weird!)
if (window.navigator.vendor != "Apple Computer, Inc." && window.navigator.vendor != "Google Inc." && !(navigator.userAgent.toLowerCase().indexOf('firefox') > -1)){
    alert("Please Leave now! You are welcome to return once you're a chrome user!");
    alert(window.navigator.vendor);
    window.location.href = "https://www.google.com/chrome/browser-features/";
    close();
}

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}  


function questionSoundFile(soundPrompt1,soundQuestion,soundPrompt2) {
    var sndprompt1 = new Audio('/resource/prompt/' + soundPrompt1);
    var sndquestion = new Audio('/resource/vocab/' + soundQuestion);
    var sndprompt2 = new Audio('/resource/prompt/' + soundPrompt2);

    sndprompt1.play();            

    sndprompt1.onended = function() {
        sndquestion.play();            
    };

    sndquestion.onended = function() {
        sndprompt2.play();            
    };
}

function selectAnswer(ID,soundAnswer){
    var sndAnswer = new Audio('/resource/vocab/' + soundAnswer);
    sndAnswer.play();

    if (httpGet("checkAnswer/" + ID) == "True"){
        document.getElementById("answer" + ID).className = "AnswerButtonCORRECT";
    } else if (httpGet("checkAnswer/" + ID) == "False"){ 
        document.getElementById("answer" + ID).className = "AnswerButtonWRONG";
    }}

function selectReview(soundFile){
    var sndFile = new Audio('/resource/vocab/' + soundFile);
    sndFile.playbackRate = 0.5;
    sndFile.play();

    }