const tabs = document.querySelectorAll('.tab');
const forms = document.querySelectorAll('.form');

// Function to handle tab clicks
tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        // Remove active class from all tabs
        tabs.forEach(t => t.classList.remove('active'));
        // Add active class to the clicked tab
        tab.classList.add('active');

        // Hide all forms
        forms.forEach(form => form.classList.remove('active'));
        // Show the corresponding form based on data-tab attribute
        const activeFormId = tab.getAttribute('data-tab');
        document.getElementById(activeFormId).classList.add('active');
    });
});

// Function to explicitly show a form (useful for links within forms)
function showForm(formId) {
    // Update active tab
    tabs.forEach(tab => {
        if (tab.getAttribute('data-tab') === formId) {
            tab.classList.add('active');
        } else {
            tab.classList.remove('active');
        }
    });

    // Show the specified form
    forms.forEach(form => {
        if (form.id === formId) {
            form.classList.add('active');
        } else {
            form.classList.remove('active');
        }
    });
}

// Set the initial active tab and form on page load (Login)
document.addEventListener('DOMContentLoaded', () => {
    // Find the login tab and form and mark them as active
    document.querySelector('.tab[data-tab="login"]').classList.add('active');
    document.getElementById('login').classList.add('active');
});

document.addEventListener('DOMContentLoaded', autoCloseMessages);

document.addEventListener('DOMContentLoaded', function () {
    const likeButtons = document.querySelectorAll('.like-button');

    likeButtons.forEach(button => {
        let isLiked = false;
        let likeCount = button.querySelector('.like-count');
        let currentCount = parseInt(likeCount.textContent) || 0; // گرفتن شمارنده فعلی یا صفر

        button.addEventListener('click', function () {
            // دکمه لایک را پیدا می‌کنیم
            const likeButton = this;
            const likeIcon = likeButton.querySelector('.like-icon');
            const likeCountSpan = likeButton.querySelector('.like-count');

            if (!isLiked) {
                // لایک کردن
                isLiked = true;
                likeButton.classList.add('liked');
                likeCountSpan.classList.add('animate'); // اضافه کردن انیمیشن
                currentCount++;
            } else {
                // آنلایک کردن
                isLiked = false;
                likeButton.classList.remove('liked');
                likeCountSpan.classList.remove('animate'); // حذف انیمیشن
                currentCount--;
            }
            likeCountSpan.textContent = currentCount;

            // حذف کلاس انیمیشن بعد از اتمام آن
            likeCountSpan.addEventListener('animationend', function () {
                likeCountSpan.classList.remove('animate');
            }, { once: true }); // اجرای یک بار
        });
    });
});
