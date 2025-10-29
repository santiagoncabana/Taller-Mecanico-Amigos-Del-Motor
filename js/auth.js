// // auth.js - Manejo del formulario de login y registro
// document.addEventListener('DOMContentLoaded', function () {
//     console.log('auth.js cargado correctamente');

//     const loginForm = document.getElementById('loginForm');
//     const registerForm = document.getElementById('registerForm');

//     // Manejo del LOGIN
//     if (loginForm) {
//         loginForm.addEventListener('submit', function (event) {
//             event.preventDefault();
//             console.log('Formulario de login enviado');

//             // Obtener valores
//             const email = document.getElementById('email').value;
//             const password = document.getElementById('password').value;

//             // Validaciones básicas
//             if (!email || !password) {
//                 alert('Por favor, completa todos los campos');
//                 return;
//             }

//             if (!isValidEmail(email)) {
//                 alert('Por favor, ingresa un email válido');
//                 return;
//             }

//             // Simulación de login exitoso
//             console.log('Login exitoso, redirigiendo...');
//             alert('¡Login exitoso! Redirigiendo al dashboard...');

//             // REDIRECCIÓN DIRECTA - sin setTimeout
//             window.location.href = 'index.html';
//         });
//     }

//     // Manejo del REGISTRO
//     if (registerForm) {
//         registerForm.addEventListener('submit', function (event) {
//             event.preventDefault();
//             console.log('Formulario de registro enviado');

//             // Obtener valores
//             const fullName = document.getElementById('fullName').value;
//             const email = document.getElementById('email').value;
//             const password = document.getElementById('password').value;
//             const confirmPassword = document.getElementById('confirmPassword').value;
//             const terms = document.getElementById('terms').checked;

//             // Validaciones
//             if (!fullName || !email || !password || !confirmPassword) {
//                 alert('Por favor, completa todos los campos');
//                 return;
//             }

//             if (!isValidEmail(email)) {
//                 alert('Por favor, ingresa un email válido');
//                 return;
//             }

//             if (password.length < 6) {
//                 alert('La contraseña debe tener al menos 6 caracteres');
//                 return;
//             }

//             if (password !== confirmPassword) {
//                 alert('Las contraseñas no coinciden');
//                 return;
//             }

//             if (!terms) {
//                 alert('Debes aceptar los términos y condiciones');
//                 return;
//             }

//             // Simulación de registro exitoso
//             console.log('Registro exitoso, redirigiendo...');
//             alert('¡Registro exitoso! Redirigiendo al login...');

//             // Redirección directa
//             window.location.href = 'login.html';
//         });
//     }

//     // Función para validar email
//     function isValidEmail(email) {
//         const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//         return emailRegex.test(email);
//     }

//     // Manejo de botones sociales
//     const socialButtons = document.querySelectorAll('.social-btn');
//     socialButtons.forEach(button => {
//         button.addEventListener('click', function () {
//             const socialType = this.classList.contains('google-btn') ? 'Google' : 'Facebook';
//             alert(`Iniciar sesión con ${socialType} - Funcionalidad en desarrollo`);
//         });
//     });
// });




// 1. Lógica para el Formulario de REGISTRO
const registerForm = document.getElementById('registerForm');

if (registerForm) {
    // Solo si estamos en la página de registro
    registerForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Recoger datos (ej. fullName, email, password)
        const nombre = document.getElementById('fullName').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        
        const data = { nombre, email, contrasena: password };

        await enviarDatos(data);
    });
}

async function enviarDatos(data) {
    try {
        const response = await fetch('http://127.0.0.1:8000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            // Si la respuesta no es 2xx, muestra el error
            const errorData = await response.json();
            console.error('Error al registrar:', errorData);
            alert('Error: ' + errorData.detail); 
            return;
        }

        console.log('Registro exitoso!');
        // Redirigir o mostrar éxito
        window.location.href = '/MecApp/frontend/formulario.html';

    } catch (error) {
        // MUESTRA ERRORES DE RED/CONEXIÓN/CORS
        console.error('Error de conexión o fetch:', error); 
        alert('Error de conexión con el servidor.');
    }
}



// 2. Lógica para el Formulario de LOGIN



const backendURL = 'http://127.0.0.1:8000/login'; 

const form = document.getElementById('loginForm');

if (form) {
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        const loginData = {
            email: email,
            contrasena: password 
        };

        await enviarLogin(loginData);
    });
} else {
    console.error("El formulario de login ('loginForm') no fue encontrado.");
}


async function enviarLogin(data) {
    try {
        const response = await fetch(backendURL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            alert('¡Bienvenido! Iniciaste sesión correctamente.');
            window.location.href = '/MecApp/frontend/formulario.html';
        } else {
            console.error('Error al iniciar sesión:', result);
            alert(`Error: ${result.detail || 'Credenciales incorrectas o problema del servidor.'}`);
        }

    } catch (error) {
        console.error('Error de conexión:', error);
        alert('No se pudo conectar con el servidor. Verifica que el backend esté activo.');
    }
}