// dashboard.js - Simulaciones para frontend
document.addEventListener('DOMContentLoaded', function () {
    console.log('Dashboard MecApp cargado - Modo Frontend');

    // Simular datos de citas pendientes
    simulateAppointments();

    // Navegación simulada
    setupNavigation();
});

function simulateAppointments() {
    const appointments = [
        { id: 1, client: 'Juan Pérez', vehicle: 'Toyota Corolla', time: '09:00 AM', service: 'Cambio de aceite' },
        { id: 2, client: 'María García', vehicle: 'Honda Civic', time: '10:30 AM', service: 'Revisión general' },
        { id: 3, client: 'Carlos López', vehicle: 'Ford Focus', time: '02:00 PM', service: 'Frenos' }
    ];

    const appointmentsList = document.querySelector('.appointments-list');
    if (appointmentsList) {
        appointments.forEach(appointment => {
            const appointmentElement = document.createElement('div');
            appointmentElement.className = 'appointment-item';
            appointmentElement.innerHTML = `
                <div class="appointment-info">
                    <strong>${appointment.client}</strong> - ${appointment.vehicle}
                    <div class="appointment-details">
                        ${appointment.time} • ${appointment.service}
                    </div>
                </div>
                <button class="btn-primary" onclick="simulateStartService(${appointment.id})">
                    Iniciar Servicio
                </button>
            `;
            appointmentsList.appendChild(appointmentElement);
        });
    }
}

function simulateStartService(appointmentId) {
    alert(`Iniciando servicio para cita #${appointmentId} - (Simulación frontend)`);
    // En el backend real, aquí se actualizaría el estado en la base de datos
}
function setupNavigation() {
    // Simular navegación entre páginas
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const pageName = this.textContent;
            alert(`Navegando a: ${pageName} - (Página en desarrollo.)`);
        });
    });
}