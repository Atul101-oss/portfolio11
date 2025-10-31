// Custom JavaScript for interactivity (optional)
document.addEventListener('DOMContentLoaded', function() {
    // Example: Alert on card click (customize as needed)
    let cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('click', () => {
            // You can show modals or effects here
            // alert('Card clicked: ' + card.querySelector('.card-title').textContent);
        });
    });
});
