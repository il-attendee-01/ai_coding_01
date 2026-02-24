const CHOICES = Object.freeze({ ROCK: 'rock', PAPER: 'paper', SCISSORS: 'scissors' });
let playerWins = 0, computerWins = 0, ties = 0, round = 0;

const buttons = document.querySelectorAll('button[data-choice]');
const resultEl = document.getElementById('result');
const scoreEl = document.getElementById('score');
const roundEl = document.getElementById('round');
const resetBtn = document.getElementById('reset');

function randomChoice() {
  const vals = Object.values(CHOICES);
  return vals[Math.floor(Math.random() * vals.length)];
}

function determineWinner(player, computer) {
  if (player === computer) return 'tie';
  const wins = new Set([
    JSON.stringify([CHOICES.ROCK, CHOICES.SCISSORS]),
    JSON.stringify([CHOICES.SCISSORS, CHOICES.PAPER]),
    JSON.stringify([CHOICES.PAPER, CHOICES.ROCK])
  ]);
  return wins.has(JSON.stringify([player, computer])) ? 'player' : 'computer';
}

function updateScoreDisplay() {
  scoreEl.textContent = `You: ${playerWins} — Computer: ${computerWins} — Ties: ${ties}`;
}

function updateRoundDisplay() {
  roundEl.textContent = `Round: ${round}`;
}

function endMatch() {
  buttons.forEach(b => b.disabled = true);
  resetBtn.hidden = false;
  if (playerWins === 2) {
    resultEl.textContent = `🎉 You won the match! Final score: ${playerWins} — ${computerWins} (ties: ${ties})`;
  } else {
    resultEl.textContent = `💻 Computer won the match. Final score: ${computerWins} — ${playerWins} (ties: ${ties})`;
  }
}

function playRound(playerChoice) {
  if (playerWins === 2 || computerWins === 2) return;
  round += 1;
  const computerChoice = randomChoice();
  const winner = determineWinner(playerChoice, computerChoice);

  if (winner === 'player') {
    playerWins += 1;
    resultEl.textContent = `You chose ${playerChoice}. Computer chose ${computerChoice}. You win this round!`;
  } else if (winner === 'computer') {
    computerWins += 1;
    resultEl.textContent = `You chose ${playerChoice}. Computer chose ${computerChoice}. Computer wins this round.`;
  } else {
    ties += 1;
    resultEl.textContent = `You chose ${playerChoice}. Computer chose ${computerChoice}. It's a tie.`;
  }

  updateRoundDisplay();
  updateScoreDisplay();

  if (playerWins === 2 || computerWins === 2) {
    endMatch();
  }
}

buttons.forEach(btn => btn.addEventListener('click', (e) => {
  const choice = e.currentTarget.getAttribute('data-choice');
  playRound(choice);
}));

resetBtn.addEventListener('click', () => {
  playerWins = 0; computerWins = 0; ties = 0; round = 0;
  buttons.forEach(b => b.disabled = false);
  resetBtn.hidden = true;
  resultEl.textContent = 'Make your move.';
  updateScoreDisplay();
  updateRoundDisplay();
});

// Initialize displays
updateScoreDisplay();
updateRoundDisplay();
