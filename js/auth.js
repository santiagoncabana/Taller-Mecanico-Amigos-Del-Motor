
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
        const userType = document.getElementById('userType').value
        
        let endpointURL;
        let redirectURL;

        if (userType == 'cliente') {
            endpointURL = 'http://127.0.0.1:8000/login';
            redirectURL = '/MecApp/frontend/formulario.html';
        } else if (userType == 'encargado') {
            endpointURL = 'http://127.0.0.1:8000/encargado/login';
            redirectURL = '/MecApp/frontend/dashboard-encargado.html';
        }

        const loginData = {
            email: email,
            contrasena: password 
        };

        await enviarLogin(loginData, endpointURL, redirectURL);
    });
} else {
    console.error("El formulario de login ('loginForm') no fue encontrado.");
}

async function enviarLogin(data, url, redirect) {
    try {
        const response = await fetch(url, {
            // ... (código de fetch/POST)
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)

        });

        if (response.ok) {
            const result = await response.json();
            console.log('Login exitoso:', result);
            window.location.href = redirect; // <-- REDIRECCIÓN
        } else {
            // FALLO: Mostrar error de credenciales
            const errorData = await response.json();
            alert(`Error de Login: ${errorData.detail || 'Credenciales incorrectas.'}`);
        }
    } catch (error) {
        alert('Error de conexión con el servidor.');
    }
}