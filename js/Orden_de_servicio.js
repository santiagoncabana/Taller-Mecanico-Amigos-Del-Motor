async function crearOrdenDeServicio(data) {
  try {
    const response = await fetch('/api/orden_de_servicio', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Error al crear la orden');
    }
    const resultado = await response.json();
    console.log('Orden creada:', resultado);
    alert(`Orden creada con ID: ${resultado.orden_id}`);
  } catch (error) {
    console.error('Error:', error.message);
    alert('Error al crear orden: ' + error.message);
  }
}

//Función para cambiar estado del turno
async function cambiarEstadoTurno(turnoId, nuevoEstado) {
  try {
    const response = await fetch(`/turnos/${turnoId}/estado`,{
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ estado: nuevoEstado })
    });
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Error al actualizar estado');
    }
    const resultado = await response.json();
    console.log('Estado actualizado:', resultado);
    alert(`Estado actualizado para turno ID: ${resultado.turno_id}`);
  } catch (error) {
    console.error('Error:', error.message);
    alert('Error al actualizar estado: ' + error.message);
  }
}