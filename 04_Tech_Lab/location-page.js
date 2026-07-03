(() => {
  const slides = Array.from(document.querySelectorAll('[data-review-slide]'));
  const prev = document.querySelector('[data-review-prev]');
  const next = document.querySelector('[data-review-next]');
  const counter = document.querySelector('[data-review-counter]');
  const dropdownToggles = Array.from(document.querySelectorAll('[data-dropdown-toggle]'));

  const closeAllDropdowns = () => {
    dropdownToggles.forEach((toggle) => {
      const key = toggle.getAttribute('data-dropdown-toggle');
      const menu = document.querySelector(`[data-dropdown-menu="${key}"]`);
      if (!menu) return;
      menu.classList.add('invisible', 'opacity-0');
      menu.classList.remove('visible', 'opacity-100');
    });
  };

  dropdownToggles.forEach((toggle) => {
    toggle.addEventListener('click', (event) => {
      event.stopPropagation();
      const key = toggle.getAttribute('data-dropdown-toggle');
      const menu = document.querySelector(`[data-dropdown-menu="${key}"]`);
      if (!menu) return;
      const isHidden = menu.classList.contains('invisible');
      closeAllDropdowns();
      if (isHidden) {
        menu.classList.remove('invisible', 'opacity-0');
        menu.classList.add('visible', 'opacity-100');
      }
    });
  });

  document.addEventListener('click', closeAllDropdowns);

  if (!slides.length || !prev || !next || !counter) return;

  let index = 0;

  const render = () => {
    slides.forEach((slide, i) => {
      slide.classList.toggle('hidden', i !== index);
    });
    counter.textContent = `${index + 1} / ${slides.length}`;
  };

  prev.addEventListener('click', () => {
    index = (index - 1 + slides.length) % slides.length;
    render();
  });

  next.addEventListener('click', () => {
    index = (index + 1) % slides.length;
    render();
  });

  render();
})();
