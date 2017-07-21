// questions to be randomly asked on page load
var questionsList = ["What are your/your friend's favorite animals?", "What do I/you hate the most(foodwise)?", "What is my favorite color?"];


//randomly chooses a question to display
function init() {
  var randomIndex = Math.floor(Math.random() * questionsList.length);
  document.getElementById("question").innerHTML = questionsList[randomIndex];
}

window.onload = init;

var answerList = []; //initialize answerList to be empty


//adds user-submitted answer to answerList
function submitAnswer() {
  var answer = document.getElementById("answerInput").value;
  var answer2 = answer.toUpperCase();
  document.getElementById("answerInput").value = "";
  answerList.push(answer2);
  console.log(answerList);
}

function displayResult() {
  document.getElementById("result").innerHTML = message
}

//checks if user-submitted guess is in answerList
function checkGuess() {
  var guess = document.getElementById("guessInput").value;
  var guess2 = guess.toUpperCase();
  // this condition will check the guesser's input and print the phrase corresponding to its accuracy
  if (answerList.indexOf(guess2) == -1){
     displayResult("you suck");
  }
  else{
    displayResult = ("you better have gotten that right -_-");
  }
}
