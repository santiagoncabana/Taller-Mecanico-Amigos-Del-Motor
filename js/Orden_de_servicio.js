/* Obtener referencia al formulario
const formElement = document.getElementById('crearOrdenForm');

// Agregar event listener para capturar el envío del formulario
formElement.addEventListener('submit', async function(e) {
  e.preventDefault();  // Detener el envío tradicional (evita recarga)

  // Recopilar datos del formulario
  const data = {
    descripcion_trabajo: document.getElementById('descripcion_trabajo').value.trim(),
    precio_total: parseFloat(document.getElementById('precio_total').value),
    turno_id: parseInt(document.getElementById('turno_id').value),
    patente: document.getElementById('patente').value.trim(),
    modelo: document.getElementById('modelo').value.trim()
  };

  // Enviar datos al backend usando fetch
  try {
    const response = await fetch('http://127.0.0.1:8000/api/orden_de_servicio/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Error al crear orden');
    }

    const resJson = await response.json();
    alert(`Estado del turno ${resJson.turno_id} actualizado correctamente.`);
  } catch (error) {
    alert(`Error al actualizar estado: ${error.message}`);
  }
});*/

// Configuración
const API_URL = 'http://127.0.0.1:8000/api/orden_de_servicio/';

// Función para crear orden de servicio
async function crearOrden(ordenData) {
    const response = await fetch(`${API_URL}/orden_de_servicio/`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(ordenData)
    });
    
    if (!response.ok) throw new Error('Error al crear orden');
    return await response.json();
}

// Función para cambiar estado del turno
async function cambiarEstado(turnoId, estado) {
    const response = await fetch(`${API_URL}/orden_de_servicio/turnos/${turnoId}/estado`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ estado })
    });
    
    if (!response.ok) throw new Error('Error al cambiar estado');
    return await response.json();
}

// Buscar turno en el backend
async function buscarTurno(turnoId) {
    const response = await fetch(`${API_URL}/turnos/${turnoId}`);
    
    if (!response.ok) throw new Error('Turno no encontrado');
    return await response.json();
}

// Autocompletar datos del turno
async function cargarDatosTurno(turnoId) {
    try {
        const turno = await buscarTurno(turnoId);
        
        document.getElementById('orderTurnId').value = turno.id;
        document.getElementById('orderClientDni').value = turno.DNI;
        document.getElementById('orderClientName').value = turno.cliente_nombre;
        document.getElementById('orderClientPhone').value = turno.telefono;
        document.getElementById('orderDate').value = turno.fecha;
        document.getElementById('orderEmployeeId').value = turno.empleado_id;
        
        showNotification(`Turno ${turnoId} cargado`);
    } catch (error) {
        showNotification(error.message, 'error');
    }
}

// Manejar creación de orden
document.getElementById('orderForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const ordenData = {
        turno_id: parseInt(document.getElementById('orderTurnId').value),
        descripcion_trabajo: document.getElementById('orderWorkDescription').value,
        precio_total: parseFloat(document.getElementById('orderPrice').value),
        patente: document.getElementById('orderLicensePlate').value,
        modelo: document.getElementById('orderModel').value
    };
    
    try {
        await crearOrden(ordenData);
        showNotification('Orden creada exitosamente!');
        document.getElementById('orderForm').reset();
    } catch (error) {
        showNotification(error.message, 'error');
    }
});

// Manejar búsqueda de turno
document.getElementById('searchTurnBtn').addEventListener('click', () => {
    const turnoId = parseInt(document.getElementById('searchTurnForOrder').value);
    if (turnoId) cargarDatosTurno(turnoId);
});

// Cambiar estado del turno
function updateTurnStatus(turnoId, nuevoEstado) {
    cambiarEstado(turnoId, nuevoEstado)
        .then(() => showNotification(`Estado cambiado a: ${nuevoEstado}`))
        .catch(error => showNotification(error.message, 'error'));
}

// Mostrar notificaciones
function showNotification(mensaje, tipo = 'success') {
    const notification = document.getElementById('notification');
    notification.textContent = mensaje;
    notification.className = `notification ${tipo} show`;
    setTimeout(() => notification.classList.remove('show'), 3000);
}