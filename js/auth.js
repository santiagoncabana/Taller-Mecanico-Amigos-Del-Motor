// auth.js - Manejo del formulario de login y registro
document.addEventListener('DOMContentLoaded', function () {
    console.log('auth.js cargado correctamente');

    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');

    // Manejo del LOGIN
    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault();
            console.log('Formulario de login enviado');

            // Obtener valores
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            // Validaciones básicas
            if (!email || !password) {
                alert('Por favor, completa todos los campos');
                return;
            }

            if (!isValidEmail(email)) {
                alert('Por favor, ingresa un email válido');
                return;
            }

            // Simulación de login exitoso
            console.log('Login exitoso, redirigiendo...');
            alert('¡Login exitoso! Redirigiendo al dashboard...');

            // REDIRECCIÓN DIRECTA - sin setTimeout
            window.location.href = 'index.html';
        });
    }

    // Manejo del REGISTRO
    if (registerForm) {
        registerForm.addEventListener('submit', function (event) {
            event.preventDefault();
            console.log('Formulario de registro enviado');

            // Obtener valores
            const fullName = document.getElementById('fullName').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirmPassword').value;
            const terms = document.getElementById('terms').checked;

            // Validaciones
            if (!fullName || !email || !password || !confirmPassword) {
                alert('Por favor, completa todos los campos');
                return;
            }

            if (!isValidEmail(email)) {
                alert('Por favor, ingresa un email válido');
                return;
            }

            if (password.length < 6) {
                alert('La contraseña debe tener al menos 6 caracteres');
                return;
            }

            if (password !== confirmPassword) {
                alert('Las contraseñas no coinciden');
                return;
            }

            if (!terms) {
                alert('Debes aceptar los términos y condiciones');
                return;
            }

            // Simulación de registro exitoso
            console.log('Registro exitoso, redirigiendo...');
            alert('¡Registro exitoso! Redirigiendo al login...');

            // Redirección directa
            window.location.href = 'login.html';
        });
    }

    // Función para validar email
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Manejo de botones sociales
    const socialButtons = document.querySelectorAll('.social-btn');
    socialButtons.forEach(button => {
        button.addEventListener('click', function () {
            const socialType = this.classList.contains('google-btn') ? 'Google' : 'Facebook';
            alert(`Iniciar sesión con ${socialType} - Funcionalidad en desarrollo`);
        });
    });
});