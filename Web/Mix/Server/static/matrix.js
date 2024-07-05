const characters = [
    'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', // Russo
    'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰヱヲン', // Japonês
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ', // Inglês
    '0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/`~' // Símbolos
];


document.addEventListener('DOMContentLoaded', function() {
    const message = document.querySelector('.animated-message');
    let index = 0;
    const text = message.textContent;
    message.textContent = '';

    function typeWriter() {
        if (index < text.length) {
            message.textContent += text.charAt(index);
            index++;
            setTimeout(typeWriter, 80); // Ajuste o tempo conforme desejado
        }
    }

    function startMatrixEffect() {
        // Aparecer a mensagem
        message.style.opacity = 1;
        message.style.visibility = 'visible';
        setTimeout(() => {
            // Desaparecer a mensagem
            message.style.opacity = 0;
            message.style.visibility = 'hidden';
            setTimeout(() => {
                // Iniciar o efeito de caracteres descendo
                startFallingCharacters();
            }, 1000); // Desaparecer por 1 segundo
        }, 2000); // Aparecer por 2 segundos
    }

    function startFallingCharacters() {
        const fallingCharacters = document.createElement('div');
        fallingCharacters.style.position = 'absolute';
        fallingCharacters.style.width = '100%';
        fallingCharacters.style.top = '0';
        fallingCharacters.style.left = '0';
        fallingCharacters.style.color = 'purple'; // Cor dos caracteres descendo
        document.body.appendChild(fallingCharacters);

        let y = 0;
        const interval = setInterval(() => {
            if (y > window.innerHeight) {
                clearInterval(interval);
                document.body.removeChild(fallingCharacters);
            } else {
                const character = characters[Math.floor(Math.random() * characters.length)];
                fallingCharacters.textContent += character.charAt(Math.floor(Math.random() * character.length));
                fallingCharacters.style.top = y + 'px';
                y += 1;
            }
        }, 15); // Ajuste a velocidade conforme desejado

        setTimeout(() => {
            clearInterval(interval);
            document.body.removeChild(fallingCharacters);
        }, 10000); // Finalizar os 10 segundos
    }
    startFallingCharacters();
    setTimeout(startMatrixEffect, 1000); // Iniciar o efeito após 1 segundo
    typeWriter();
});