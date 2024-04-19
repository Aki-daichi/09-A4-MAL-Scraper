// Animasi saat mengarahkan mouse ke kartu anggota
const anggotaCards = document.querySelectorAll('.anggota-card');

anggotaCards.forEach(card => {
    card.addEventListener('mouseover', () => {
        card.style.transform = 'translateY(-5px)';
        card.style.boxShadow = '0 8px 15px rgba(0, 0, 0, 0.2)';
    });

    card.addEventListener('mouseout', () => {
        card.style.transform = 'translateY(0)';
        card.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
    });
});

// Fungsi untuk memberikan efek scroll yang halus saat mengklik tautan di navbar
function smoothScroll(event) {
    event.preventDefault(); // Mencegah perilaku default tautan

    const targetId = event.currentTarget.getAttribute('href');
    const targetElement = document.querySelector(targetId);

    if (targetElement) {
        targetElement.scrollIntoView({
            behavior: 'smooth'
        });
    }
}

// Ambil semua tautan di navbar
const navLinks = document.querySelectorAll('nav a');

// Tambahkan event listener ke setiap tautan di navbar
navLinks.forEach(link => {
    link.addEventListener('click', smoothScroll);
});
