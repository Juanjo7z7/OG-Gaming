// Obtener el elemento de cierre
var closeButton = document.querySelector('.toast_alert .close');

// Obtener el elemento de notificación
var toastAlert = document.querySelector('.toast_alert');

// Agregar un evento de clic al botón de cierre
closeButton.addEventListener('click', function() {
  // Ocultar la notificación al hacer clic en el botón de cierre
  toastAlert.style.display = 'none';
});