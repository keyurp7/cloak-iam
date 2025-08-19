(function () {
  const rootElement = document.documentElement;
  const themeToggleButton = document.getElementById('theme-toggle');
  const navToggleButton = document.querySelector('.nav-toggle');
  const nav = document.getElementById('site-nav');
  const yearElement = document.getElementById('year');

  function getStoredTheme() {
    try { return localStorage.getItem('theme'); } catch { return null; }
  }

  function storeTheme(theme) {
    try { localStorage.setItem('theme', theme); } catch {}
  }

  function applyTheme(theme) {
    const isLight = theme === 'light';
    rootElement.classList.toggle('light', isLight);
    if (themeToggleButton) {
      themeToggleButton.setAttribute('aria-pressed', String(isLight));
      themeToggleButton.textContent = isLight ? '🌞' : '🌗';
      themeToggleButton.title = isLight ? 'Switch to dark mode' : 'Switch to light mode';
    }
  }

  function initTheme() {
    const stored = getStoredTheme();
    if (stored === 'light' || stored === 'dark') {
      applyTheme(stored);
      return;
    }
    const prefersLight = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches;
    applyTheme(prefersLight ? 'light' : 'dark');
  }

  function toggleTheme() {
    const newTheme = rootElement.classList.contains('light') ? 'dark' : 'light';
    applyTheme(newTheme);
    storeTheme(newTheme);
  }

  function toggleNav() {
    const isOpen = nav.classList.toggle('open');
    navToggleButton.setAttribute('aria-expanded', String(isOpen));
  }

  function closeNavOnLinkClick() {
    nav.addEventListener('click', (e) => {
      const target = e.target;
      if (target.tagName === 'A') {
        nav.classList.remove('open');
        navToggleButton.setAttribute('aria-expanded', 'false');
      }
    });
  }

  function initYear() {
    if (yearElement) yearElement.textContent = String(new Date().getFullYear());
  }

  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initYear();
    if (themeToggleButton) themeToggleButton.addEventListener('click', toggleTheme);
    if (navToggleButton && nav) {
      navToggleButton.addEventListener('click', toggleNav);
      closeNavOnLinkClick();
    }
  });
})();

