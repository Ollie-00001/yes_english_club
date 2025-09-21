document.addEventListener('DOMContentLoaded', () => {
    const wrapper = document.querySelector('.image-thumbnails-wrapper');
    if (!wrapper) return;

    const preview = document.getElementById("preview-img");
    const thumbnails = wrapper.querySelector('.image-thumbnails');
    const thumbImages = Array.from(wrapper.querySelectorAll(".thumb img"));
    const btnLeft = wrapper.querySelector('.thumb-nav.left');
    const btnRight = wrapper.querySelector('.thumb-nav.right');

    if (thumbImages.length === 0) {
      return;
    }

    const VISIBLE = 5;
    let activeIndex = 0;
    let offset = 0;

    function updatePreview() {
        preview.src = thumbImages[activeIndex].src;
    }

    function updateCarousel() {
        const step = thumbImages[0].offsetWidth + parseInt(getComputedStyle(thumbnails).gap || 8);
        offset = activeIndex;
        thumbnails.style.transform = `translateX(${-offset * step}px)`;
    }

        function goNext() {
        activeIndex = (activeIndex + 1) % thumbImages.length;
        updatePreview();
        updateCarousel();
    }

    function goPrev() {
        activeIndex = (activeIndex - 1 + thumbImages.length) % thumbImages.length;
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

    let timer = setInterval(goNext, 3000);
    wrapper.addEventListener('mouseenter', () => clearInterval(timer));
    wrapper.addEventListener('mouseleave', () => timer = setInterval(goNext, 3000));

    updatePreview();
    updateCarousel();
});

// Reviews pagination
document.addEventListener('DOMContentLoaded', function() {
  const grid = document.getElementById('reviewsGrid');
  const loadBtn = document.getElementById('loadMoreBtn');
  if (!grid || !loadBtn) return;

  const reviews = Array.from(grid.querySelectorAll('.review-card'));
  const initial = parseInt(grid.dataset.initial) || 4;
  let visibleCount = initial;

  reviews.forEach((el, idx) => {
    if (idx < visibleCount) el.classList.remove('hidden');
    else el.classList.add('hidden');
  });

  function updateButton() {
    loadBtn.style.display = (visibleCount >= reviews.length) ? 'none' : '';
  }
  updateButton();

  loadBtn.addEventListener('click', function() {
    const next = Math.min(reviews.length, visibleCount + initial);
    for (let i = visibleCount; i < next; i++) {
      reviews[i].classList.remove('hidden');
      reviews[i].classList.add('fade-in');
      setTimeout(() => reviews[i].classList.remove('fade-in'), 350);
    }
    visibleCount = next;
    updateButton();
  });
});

// Review text toggle btn
document.addEventListener('DOMContentLoaded', () => {
    const reviewCards = document.querySelectorAll('.review-card');

    reviewCards.forEach(card => {
        const text = card.querySelector('.review-text');
        const btn = card.querySelector('.btn-toggle-text');

        const maxHeight = text.clientHeight;

        if (text.scrollHeight > maxHeight) {
            btn.style.display = 'inline-block';

            btn.addEventListener('click', () => {
                text.classList.toggle('clamp');
                btn.textContent = text.classList.contains('clamp') ? 'Развернуть' : 'Скрыть';
            });
        } else {
            btn.style.display = 'none';
        }
    });
});

// Scroll to top button
const scrollTopBtn = document.getElementById('scrollTopBtn');

function findScrollableElement() {
    const candidates = [
        document.documentElement,
        document.body,
        document.querySelector('.main'),
        document.querySelector('.container'),
        document.querySelector('[data-scroll]'),
        ...document.querySelectorAll('*')
    ];

    for (let element of candidates) {
        if (element && (element.scrollTop > 0 || element.scrollHeight > element.clientHeight)) {
            console.log('Found scrollable element:', element);
            return element;
        }
    }
    
    return window;
}

let scrollElement = findScrollableElement();

function getScrollPosition() {
    if (scrollElement === window) {
        return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
    } else {
        return scrollElement.scrollTop;
    }
}

function toggleScrollTopBtn() {
    const scrollPos = getScrollPosition();
    console.log('Scroll position:', scrollPos, 'Element:', scrollElement);
    
    if (scrollPos > 300) {
        scrollTopBtn.classList.add('show');
    } else {
        scrollTopBtn.classList.remove('show');
    }
}

function scrollToTop(e) {
    e.preventDefault();
    
    if (scrollElement === window) {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    } else {
        scrollElement.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
}

function addScrollListener() {
    const elementsToListen = [window, document, document.documentElement, document.body];
    
    const scrollableElements = Array.from(document.querySelectorAll('*')).filter(el => {
        const style = window.getComputedStyle(el);
        return style.overflow === 'auto' || style.overflow === 'scroll' || 
                style.overflowY === 'auto' || style.overflowY === 'scroll';
    });
    
    elementsToListen.push(...scrollableElements);
    
    elementsToListen.forEach(element => {
        if (element) {
            element.addEventListener('scroll', toggleScrollTopBtn);
            console.log('Added scroll listener to:', element);
        }
    });
}

addScrollListener();
scrollTopBtn.addEventListener('click', scrollToTop);

setTimeout(() => {
    scrollElement = findScrollableElement();
    toggleScrollTopBtn();
}, 100);