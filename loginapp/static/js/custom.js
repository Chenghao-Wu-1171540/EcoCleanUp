// custom.js - Global custom JavaScript for EcoCleanUp Hub

document.addEventListener('DOMContentLoaded', function () {
    // Enable tooltips everywhere
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));


    const unregisterButtons = document.querySelectorAll('[data-bs-target="#confirmUnregisterModal"]');
    const modalEventName = document.getElementById('modalEventName');
    const confirmBtn = document.getElementById('confirmUnregisterBtn');

    document.addEventListener('click', function (e) {
        const button = e.target.closest('[data-bs-target="#confirmUnregisterModal"]');
        if (!button) return;

        const eventName = button.getAttribute('data-event-name');
        const eventId = button.getAttribute('data-event-id');

        if (modalEventName) {
            modalEventName.textContent = `"${eventName}"?`;
        }

        if (confirmBtn) {
            confirmBtn.onclick = null;
            confirmBtn.onclick = function () {
                const form = document.createElement('form');
                form.method = 'POST';
                form.action = `/unregister/${eventId}`;
                // form.innerHTML = '<input type="hidden" name="csrf_token" value="' + document.querySelector('input[name=csrf_token]').value + '">';
                document.body.appendChild(form);
                form.submit();
            };
        }
    });
});


window.addEventListener('scroll', function () {
    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        backToTop.style.display = window.scrollY > 300 ? 'block' : 'none';
    }
});