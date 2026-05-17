document.addEventListener('DOMContentLoaded', () => {

    // Smooth scrolling for navigation links
    document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Handle clicks on album links to pass album ID (basic example)
    document.querySelectorAll('.album-item .btn-secondary').forEach(link => {
        link.addEventListener('click', (e) => {
            // In a real app, you'd fetch album details based on the ID
            // For now, we just let the link navigate
            console.log(`Navigating to album detail for ID: ${link.getAttribute('href').split('=')[1]}`);
        });
    });

    // Placeholder for play track button functionality
    const playTrackButtons = document.querySelectorAll('.play-track-btn');
    playTrackButtons.forEach(button => {
        button.addEventListener('click', () => {
            alert('Playing track! (Implementation needed)');
            // Add logic here to play the specific track
        });
    });

    // Placeholder for 'Play All' button
    const playAllBtn = document.querySelector('.play-all-btn');
    if (playAllBtn) {
        playAllBtn.addEventListener('click', (e) => {
            e.preventDefault();
            alert('Playing all tracks from this album! (Implementation needed)');
            // Add logic here to play all tracks sequentially
        });
    }

    // Add subtle hover effect for album items if needed (already in CSS)
    const albumItems = document.querySelectorAll('.album-item');
    albumItems.forEach(item => {
        item.addEventListener('mouseover', () => {
            // Add class or style if needed, CSS handles basic effects
        });
        item.addEventListener('mouseout', () => {
            // Remove class or style
        });
    });

});


function autoCloseMessages() {
    // تمام پیام‌هایی که کلاس 'messages li' دارند را پیدا کن
    var messages = document.querySelectorAll('.messages li');

    messages.forEach(function (message) {
        // پیام‌هایی که کلاس error یا warning دارند را نگه می‌داریم (برای اینکه کاربر ببیند)
        // بقیه پیام‌ها (مثل success, info, debug) بعد از 5 ثانیه ناپدید می‌شوند.
        if (!message.classList.contains('error') && !message.classList.contains('warning')) {

            // setTimeout یک تابع را بعد از مدت زمان مشخصی اجرا می‌کند
            setTimeout(function () {
                // چک می‌کنیم که آیا پیام هنوز در صفحه وجود دارد یا نه
                // (ممکن است کاربر قبلاً آن را دستی بسته باشد)
                if (message.parentNode) {
                    message.style.display = 'none'; // پیام را مخفی می‌کنیم
                }
            }, 5000); // 5000 میلی‌ثانیه = 5 ثانیه
        }
    });
}

// این خط باعث می‌شود تابع autoCloseMessages هر بار که صفحه بارگذاری می‌شود، اجرا گردد
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

const sidebar = document.getElementById("sidebar");
const btn = document.getElementById("menu-btn");

btn.onclick = () => {
  if (sidebar.style.maxHeight && sidebar.style.maxHeight !== "0px") {
    sidebar.style.maxHeight = "0px";        // بسته شدن
  } else {
    sidebar.style.maxHeight = "300px";      // باز شدن (ارتفاع منوی تو)
  }
};

