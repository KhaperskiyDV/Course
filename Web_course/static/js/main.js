const swiper = new Swiper(".mySwiper", {
  effect: 'fade',
  fadeEffect: {
    crossFade: true
  },  
  navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    autoplay: {
        delay: 5000,
        disableOnInteraction: true,
      },
  });