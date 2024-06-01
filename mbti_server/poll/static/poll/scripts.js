/* poll/static/poll/scripts.js */
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', (e) => {
        const questions = form.querySelectorAll('.question');
        let allAnswered = true;

        questions.forEach((question) => {
            const radios = question.querySelectorAll('input[type="radio"]');
            let answered = false;
            radios.forEach((radio) => {
                if (radio.checked) {
                    answered = true;
                }
            });
            if (!answered) {
                allAnswered = false;
                question.classList.add('unanswered');
            } else {
                question.classList.remove('unanswered');
            }
        });

        if (!allAnswered) {
            e.preventDefault();
            alert('아직 모든 설문에 답하지 않았습니다.');
        }
    });

    // 추가 인터랙티브 효과
    const questions = document.querySelectorAll('.question');
    questions.forEach((question) => {
        question.addEventListener('mouseenter', () => {
            question.style.backgroundColor = '#f1f1f1';
        });
        question.addEventListener('mouseleave', () => {
            question.style.backgroundColor = 'white';
        });
    });
});
