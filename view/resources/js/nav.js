

// Fungsi untuk memberikan efek scroll yang halus
function smoothScroll(event) {
    event.preventDefault(); // Mencegah perilaku default tautan

    // Mendapatkan elemen tujuan berdasarkan href
    const targetId = event.currentTarget.getAttribute('href');
    const targetElement = document.querySelector(targetId);

    // Jika elemen tujuan ditemukan, lakukan scroll dengan halus
    if (targetElement) {
        targetElement.scrollIntoView({
            behavior: 'smooth' // Mengatur scroll menjadi halus
        });
    }
}

// Ambil semua tautan di navbar
const navLinks = document.querySelectorAll('nav a');

// Tambahkan event listener ke setiap tautan di navbar
navLinks.forEach(link => {
    link.addEventListener('click', smoothScroll);
});

// Ambil semua tautan di dalam menu burger
const burgerMenuLinks = document.querySelectorAll('#menu a');

// Fungsi untuk menutup menu burger ketika tautan ditekan
function closeBurgerMenu() {
    toggleMenu();
}

// Tambahkan event listener ke setiap tautan di dalam menu burger
burgerMenuLinks.forEach(link => {
    link.addEventListener('click', closeBurgerMenu);
});

