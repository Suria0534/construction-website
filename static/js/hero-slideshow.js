document.addEventListener("DOMContentLoaded", function () {
    // Slideshow images switching
    const slides = document.querySelectorAll('.hero-slide');
    let current = 0;

    function showNextSlide() {
        slides[current].classList.remove('active');
        current = (current + 1) % slides.length;
        slides[current].classList.add('active');
    }

    setInterval(showNextSlide, 10000); // every 10 seconds slide changes

    // Word-by-word animated typing of sentence
    const textElement = document.getElementById('animated-text');
    const sentences = [
         "Welcome to A Momin Engineering & Construction",
        "Building Your Dreams With Strength",
        "Trust and Quality, Our Promise"
    ];

    let sentenceIndex = 0;
    let wordIndex = 0;
    let displayedWords = [];

    function typeWordByWord() {
        const words = sentences[sentenceIndex].split(' ');
        if (wordIndex < words.length) {
            displayedWords.push(words[wordIndex]);
            textElement.textContent = displayedWords.join(' ');
            wordIndex++;
            setTimeout(typeWordByWord, 800); // delay between words
        } else {
            setTimeout(() => {
                displayedWords = [];
                wordIndex = 0;
                sentenceIndex = (sentenceIndex + 1) % sentences.length;
                textElement.textContent = '';
                typeWordByWord();
            }, 3000); // pause before next sentence
        }
    }

    typeWordByWord();
});
