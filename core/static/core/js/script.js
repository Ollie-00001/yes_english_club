document.addEventListener('DOMContentLoaded', () => {
    const wrapper = document.querySelector('.image-thumbnails-wrapper');
    if (!wrapper) return;

    const preview = document.getElementById("preview-img");
    const thumbnails = wrapper.querySelector('.image-thumbnails');
    const thumbImages = Array.from(wrapper.querySelectorAll(".thumb img"));
    const btnLeft = wrapper.querySelector('.thumb-nav.left');
    const btnRight = wrapper.querySelector('.thumb-nav.right');

    const VISIBLE = 5;
    let activeIndex = 0; // индекс активной миниатюры
    let offset = 0;      // сдвиг карусели

    function updatePreview() {
        preview.src = thumbImages[activeIndex].src;
    }

    function updateCarousel() {
        const step = thumbImages[0].offsetWidth + parseInt(getComputedStyle(thumbnails).gap || 8);
        // смещаем карусель на активную фотку
        offset = activeIndex;
        thumbnails.style.transform = `translateX(${-offset * step}px)`;
    }

        function goNext() {
        activeIndex = (activeIndex + 1) % thumbImages.length; // зацикливаем вправо
        updatePreview();
        updateCarousel();
    }

    function goPrev() {
        activeIndex = (activeIndex - 1 + thumbImages.length) % thumbImages.length; // зацикливаем влево
        updatePreview();
        updateCarousel();
    }

    btnLeft.addEventListener('click', goPrev);
    btnRight.addEventListener('click', goNext);

    thumbImages.forEach((img, i) => {
        img.parentElement.addEventListener('click', e => {
            e.preventDefault();
            activeIndex = i;
            updatePreview();
            updateCarousel();
        });
    });

    // автопрокрутка
    let timer = setInterval(goNext, 3000);
    wrapper.addEventListener('mouseenter', () => clearInterval(timer));
    wrapper.addEventListener('mouseleave', () => timer = setInterval(goNext, 3000));

    // старт
    updatePreview();
    updateCarousel();
});
