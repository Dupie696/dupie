console.log(window.navigator.vendor);

// note: Google Inc works with Edge and Chrome
// note: works with firefox
// TODO: go back and make this work in IE (my coworkers are really weird!)
if (window.navigator.vendor != "Google Inc." && !(navigator.userAgent.toLowerCase().indexOf('firefox') > -1)){
    alert("Please Leave now! You are welcome to return once you're a chrome user!");
    window.location.href = "https://www.google.com/chrome/browser-features/";
    close();
}

window.onload = function refreshForm()
{
    document.getElementById("QuestionBox").innerHTML = httpGet("getQuestion");
}


// var intervalId = window.setInterval(function(){
//    var strrr = httpGet("getTime");
//    document.getElementById("QuestionBox").innerHTML =strrr;
 
//  }, 1000);

  

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}  


function questionSoundFile(soundPrompt1,soundQuestion,soundPrompt2) {
    var sndprompt1 = new Audio('resource/prompt/' + soundPrompt1);
    var sndquestion = new Audio('resource/vocab/' +  soundQuestion);
    var sndprompt2 = new Audio('resource/prompt/' + soundPrompt2);

    sndprompt1.play();            

    sndprompt1.onended = function() {
        sndquestion.play();            
    };

    sndquestion.onended = function() {
        sndprompt2.play();            
    };
}

function selectAnswer(ID,soundAnswer){
    var sndAnswer = new Audio('resource/vocab/' + soundAnswer);
    sndAnswer.play();
    
    //console.log(document.getElementById("controlPanel").style.display);
    if (document.getElementById("controlPanel").style.display !== "none") {return};

    //console.log(httpGet("checkAnswer/"+ ID));
    if (httpGet("checkAnswer/" + ID) == "True"){
        document.getElementById("answer" + ID).className = "AnswerButtonCORRECT";
        if (httpGet("newQuestion") == "True"){
            document.getElementById("controlPanel").style = "";
        }
        //httpGet("newQuestion");
    } else {
        document.getElementById("answer" + ID).className = "AnswerButtonWRONG";
    }


}


function nextQuestion(){
    location.reload();
}
