(() => {
  const button = document.querySelector('.theme-toggle');
  const label = document.querySelector('.theme-label');
  const color = document.querySelector('meta[name="theme-color"]');
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  let preference = null;
  try { preference = localStorage.getItem('aura-theme'); } catch { /* Storage is optional. */ }
  function apply(dark) {
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    button.setAttribute('aria-pressed', String(dark));
    button.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
    label.textContent = dark ? 'Light mode' : 'Dark mode';
    color.content = dark ? '#1a1d24' : '#faf5ee';
  }
  apply(preference === 'dark' || (preference !== 'light' && system.matches));
  button.hidden = false;
  button.addEventListener('click', () => {
    preference = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    apply(preference === 'dark');
    try { localStorage.setItem('aura-theme', preference); } catch { /* Toggle still works. */ }
  });
  system.addEventListener('change', event => { if (!preference) apply(event.matches); });
})();
