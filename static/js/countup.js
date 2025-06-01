document.addEventListener("DOMContentLoaded", function () {
    const countEl = document.getElementById("completedCount");

    if (countEl) {
        const target = parseInt(countEl.getAttribute("data-count")); // এটা fixed
        let count = 0;
        const duration = 2000; // milliseconds
        const stepTime = Math.abs(Math.floor(duration / target));

        const timer = setInterval(() => {
            count++;
            countEl.innerText = count;
            if (count >= target) {
                clearInterval(timer);
            }
        }, stepTime);
    }
});
