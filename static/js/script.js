document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('logout-link').addEventListener('click', function(event) {
        event.preventDefault();
        if (confirm('¿Estás seguro de que deseas cerrar sesión?')) {
            window.location.href = this.href;
        }
    });
});