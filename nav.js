/**
 * ViajeraMente — Shared Navigation Module
 * nav.js
 *
 * Auto-injects consistent navigation across all pages:
 *   - Top navigation bar (desktop + mobile)
 *   - Mobile menu overlay
 *   - Bottom tab bar (mobile, authenticated pages)
 *   - Footer (public pages)
 *
 * Usage:
 *   <script src="nav.js" data-page="guias" data-bottom-nav="true" data-footer="true"></script>
 *
 * Config attributes:
 *   data-page       — Active page id (home|guias|plan|mapa|ranking|profile|fechas|interrail|rtw)
 *   data-bottom-nav — Show mobile bottom tab bar ("true"|"false")
 *   data-footer     — Show footer ("true"|"false")
 */

(function () {
  'use strict';

  // ── Read config from <script> tag ─────────────────────────────────
  const scriptTag = document.currentScript;
  const cfg = {
    page:      scriptTag?.getAttribute('data-page') || '',
    bottomNav: scriptTag?.getAttribute('data-bottom-nav') === 'true',
    footer:    scriptTag?.getAttribute('data-footer') === 'true',
  };

  // ── Auth state ────────────────────────────────────────────────────
  const token    = localStorage.getItem('token');
  const userName = localStorage.getItem('user_name') || '';
  const isAuth   = !!token;
  const initials = userName ? userName.charAt(0).toUpperCase() : '?';
  const logoHref = isAuth ? 'main.html' : 'index.html';

  // ── Login redirect helper ─────────────────────────────────────────
  const loginUrl  = 'login.html?next=' + encodeURIComponent(window.location.href);
  const signupUrl = 'signup.html';

  // ── Active page checker ───────────────────────────────────────────
  function isActive(pageId) {
    return cfg.page === pageId;
  }
  function activeClass(pageId) {
    return isActive(pageId) ? ' active' : '';
  }

  // ── Inject styles ─────────────────────────────────────────────────
  const style = document.createElement('style');
  style.textContent = `
    /* ================================================================
       nav.js — Injected Styles
       Uses CSS variables from styles.css where available.
       ================================================================ */

    /* ── Top Navigation Bar ── */
    .vm-topnav {
      position: fixed;
      top: 0; left: 0; right: 0;
      z-index: 200;
      height: 56px;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border, #E2E8F0);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 max(24px, calc((100% - 1200px) / 2 + 24px));
      animation: slideDown .35s ease both;
    }

    /* Logo */
    .vm-topnav-logo {
      font-family: 'Playfair Display', 'Georgia', serif;
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: -0.01em;
      color: var(--text, #0F172A);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
      flex-shrink: 0;
    }
    .vm-topnav-logo em {
      font-style: italic;
      color: var(--text-2, #64748B);
    }

    /* Center nav links (desktop) */
    .vm-topnav-links {
      display: flex;
      align-items: center;
      gap: 2px;
    }
    .vm-topnav-link {
      font-size: .8rem;
      font-weight: 500;
      color: var(--text-2, #64748B);
      text-decoration: none;
      padding: 6px 14px;
      border-radius: 8px;
      transition: color .15s, background .15s;
    }
    .vm-topnav-link:hover {
      color: var(--text, #0F172A);
      background: var(--bg-soft, #F8FAFC);
    }
    .vm-topnav-link.active {
      color: var(--accent, #0EA5E9);
      font-weight: 600;
    }
    @media (max-width: 768px) {
      .vm-topnav-links { display: none; }
    }

    /* Right section */
    .vm-topnav-right {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }
    .vm-topnav-login {
      font-size: .82rem;
      font-weight: 500;
      color: var(--text-2, #64748B);
      text-decoration: none;
      padding: 6px 12px;
      border-radius: 8px;
      transition: color .15s, background .15s;
    }
    .vm-topnav-login:hover {
      color: var(--text, #0F172A);
      background: var(--bg-soft, #F8FAFC);
    }
    .vm-topnav-signup {
      font-size: .82rem;
      font-weight: 600;
      color: #fff;
      background: var(--accent, #0EA5E9);
      text-decoration: none;
      padding: 7px 18px;
      border-radius: 10px;
      transition: background .15s;
      white-space: nowrap;
    }
    .vm-topnav-signup:hover {
      background: var(--accent-dark, #0284C7);
    }

    /* Avatar */
    .vm-topnav-avatar {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: var(--accent-light, #E0F2FE);
      border: 2px solid var(--border, #E2E8F0);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: .72rem;
      font-weight: 700;
      color: var(--accent, #0EA5E9);
      text-decoration: none;
      overflow: hidden;
      transition: border-color .2s;
      flex-shrink: 0;
    }
    .vm-topnav-avatar:hover {
      border-color: var(--accent, #0EA5E9);
    }

    /* Hamburger (mobile only) */
    .vm-topnav-burger {
      display: none;
      background: none;
      border: none;
      cursor: pointer;
      padding: 6px;
      border-radius: 6px;
      color: var(--text, #0F172A);
      transition: background .15s;
      line-height: 0;
    }
    .vm-topnav-burger:hover {
      background: var(--bg-soft, #F8FAFC);
    }
    .vm-topnav-burger svg {
      width: 22px;
      height: 22px;
      stroke: currentColor;
      fill: none;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
    }
    @media (max-width: 768px) {
      .vm-topnav-burger { display: flex; align-items: center; }
    }

    /* ── Mobile Menu Overlay ── */
    .vm-mob-overlay {
      display: none;
      position: fixed;
      inset: 0;
      z-index: 500;
      background: rgba(0, 0, 0, 0.4);
      backdrop-filter: blur(4px);
      -webkit-backdrop-filter: blur(4px);
    }
    .vm-mob-overlay.open {
      display: block;
    }
    .vm-mob-menu {
      position: absolute;
      top: 0; left: 0; right: 0;
      background: #fff;
      border-bottom: 1px solid var(--border, #E2E8F0);
      padding: 16px 20px 28px;
      transform: translateY(-100%);
      transition: transform .25s cubic-bezier(.4, 0, .2, 1);
    }
    .vm-mob-overlay.open .vm-mob-menu {
      transform: translateY(0);
    }
    .vm-mob-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 18px;
    }
    .vm-mob-close {
      background: none;
      border: none;
      cursor: pointer;
      font-size: 1.2rem;
      color: var(--text-3, #9CA3AF);
      padding: 4px;
      border-radius: 6px;
      line-height: 0;
    }
    .vm-mob-close:hover { color: var(--text, #0F172A); }
    .vm-mob-close svg {
      width: 22px;
      height: 22px;
      stroke: currentColor;
      fill: none;
      stroke-width: 2;
      stroke-linecap: round;
    }
    .vm-mob-links {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .vm-mob-link {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 12px 14px;
      border-radius: 10px;
      text-decoration: none;
      color: var(--text, #0F172A);
      font-size: .9rem;
      font-weight: 500;
      transition: background .12s;
    }
    .vm-mob-link:hover { background: var(--bg-soft, #F8FAFC); }
    .vm-mob-link.active { color: var(--accent, #0EA5E9); }
    .vm-mob-link .vm-mob-icon {
      font-size: 1.1rem;
      width: 24px;
      text-align: center;
    }
    .vm-mob-divider {
      height: 1px;
      background: var(--border, #E2E8F0);
      margin: 10px 0;
    }
    .vm-mob-action {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 12px 14px;
      border-radius: 10px;
      color: var(--text-3, #9CA3AF);
      font-size: .9rem;
      font-weight: 500;
      background: none;
      border: none;
      cursor: pointer;
      width: 100%;
      font-family: inherit;
      text-decoration: none;
      transition: background .12s, color .12s;
    }
    .vm-mob-action:hover {
      background: var(--bg-soft, #F8FAFC);
      color: var(--text, #0F172A);
    }
    .vm-mob-signup-btn {
      display: block;
      text-align: center;
      font-size: .9rem;
      font-weight: 600;
      color: #fff;
      background: var(--accent, #0EA5E9);
      text-decoration: none;
      padding: 12px 14px;
      border-radius: 10px;
      margin-top: 4px;
      transition: background .15s;
    }
    .vm-mob-signup-btn:hover {
      background: var(--accent-dark, #0284C7);
    }

    /* ── Bottom Navigation (mobile tab bar) ── */
    .vm-botnav {
      display: none;
      position: fixed;
      bottom: 0; left: 0; right: 0;
      background: #fff;
      border-top: 1px solid var(--border, #E2E8F0);
      z-index: 1000;
      padding: 6px 0 max(6px, env(safe-area-inset-bottom));
    }
    @media (max-width: 768px) {
      .vm-botnav { display: flex; }
    }
    .vm-botnav .tab {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      color: var(--text-3, #9CA3AF);
      font-size: .62rem;
      font-weight: 600;
      padding: 4px 0;
      gap: 2px;
      transition: color .15s;
    }
    .vm-botnav .tab.active { color: var(--accent, #0EA5E9); }
    .vm-botnav .tab:hover { color: var(--accent, #0EA5E9); }
    .vm-botnav .tab .tab-ic {
      width: 22px;
      height: 22px;
      stroke: currentColor;
      fill: none;
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
    }

    /* ── Footer ── */
    .vm-footer {
      background: #0F172A;
      color: rgba(255, 255, 255, 0.7);
      padding: 60px 24px 32px;
    }
    .vm-footer-inner {
      max-width: 1080px;
      margin: 0 auto;
    }
    .vm-footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 40px;
      margin-bottom: 40px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 36px;
    }
    @media (max-width: 768px) {
      .vm-footer-grid { grid-template-columns: 1fr 1fr; gap: 28px; }
    }
    @media (max-width: 480px) {
      .vm-footer-grid { grid-template-columns: 1fr; gap: 24px; }
    }
    .vm-footer-brand-logo {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.2rem;
      font-weight: 700;
      color: #fff;
      text-decoration: none;
      display: block;
      margin-bottom: 12px;
    }
    .vm-footer-brand-desc {
      font-size: 0.82rem;
      line-height: 1.6;
      color: rgba(255, 255, 255, 0.5);
      max-width: 240px;
    }
    .vm-footer-col h4 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: rgba(255, 255, 255, 0.4);
      margin-bottom: 14px;
    }
    .vm-footer-col a {
      display: block;
      font-size: 0.82rem;
      color: rgba(255, 255, 255, 0.6);
      text-decoration: none;
      margin-bottom: 10px;
      transition: color 0.2s;
    }
    .vm-footer-col a:hover { color: #fff; }
    .vm-footer-bottom {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
    }
    .vm-footer-copy {
      font-size: 0.78rem;
      color: rgba(255, 255, 255, 0.3);
    }
    .vm-footer-socials {
      display: flex;
      gap: 14px;
    }
    .vm-footer-social {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 34px;
      height: 34px;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: rgba(255, 255, 255, 0.5);
      transition: all 0.2s;
      text-decoration: none;
    }
    .vm-footer-social:hover {
      background: rgba(255, 255, 255, 0.13);
      color: #fff;
    }
    .vm-footer-social svg {
      width: 16px;
      height: 16px;
      fill: currentColor;
    }
  `;
  document.head.appendChild(style);

  // ── Wait for DOM ──────────────────────────────────────────────────
  function init() {
    injectTopNav();
    injectMobileMenu();
    if (cfg.bottomNav) injectBottomNav();
    if (cfg.footer) injectFooter();
    applyBodyPadding();
    bindEvents();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // ── Top Navigation Bar ────────────────────────────────────────────
  function injectTopNav() {
    const nav = document.createElement('nav');
    nav.className = 'vm-topnav';
    nav.innerHTML = `
      <a href="${logoHref}" class="vm-topnav-logo">
        ✈️ Viajera<em>Mente</em>
      </a>
      <div class="vm-topnav-links">
        <a href="guias.html"    class="vm-topnav-link${activeClass('guias')}">Guías</a>
        <a href="plan.html"     class="vm-topnav-link${activeClass('plan')}">Planifica</a>
        <a href="mapa.html"     class="vm-topnav-link${activeClass('mapa')}">Mapa</a>
        <a href="discover.html" class="vm-topnav-link${activeClass('discover')}">Descubrir</a>
        <a href="ranking.html"  class="vm-topnav-link${activeClass('ranking')}">Ranking</a>
      </div>
      <div class="vm-topnav-right">
        ${isAuth
          ? `<a href="profile.html" class="vm-topnav-avatar" title="Mi perfil">${initials}</a>`
          : `<a href="${loginUrl}" class="vm-topnav-login">Entrar</a>
             <a href="${signupUrl}" class="vm-topnav-signup">Registrarse</a>`
        }
        <button class="vm-topnav-burger" aria-label="Abrir menú">
          <svg viewBox="0 0 24 24"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    `;
    document.body.insertBefore(nav, document.body.firstChild);
  }

  // ── Mobile Menu Overlay ───────────────────────────────────────────
  function injectMobileMenu() {
    const overlay = document.createElement('div');
    overlay.className = 'vm-mob-overlay';
    overlay.id = 'vmMobileMenu';

    const links = [
      { icon: '🏠', label: 'Inicio',             href: isAuth ? 'main.html' : 'index.html', page: 'home' },
      { icon: '🗺️', label: 'Guías',              href: 'guias.html',          page: 'guias' },
      { icon: '✈️', label: 'Planifica',           href: 'plan.html',           page: 'plan' },
      { icon: '🌍', label: 'Mapa',                href: 'mapa.html',           page: 'mapa' },
      { icon: '📅', label: 'Fechas',              href: 'fechas.html',         page: 'fechas' },
      { icon: '🔍', label: 'Descubrir',             href: 'discover.html',       page: 'discover' },
      { icon: '🏆', label: 'Ranking',             href: 'ranking.html',        page: 'ranking' },
      { icon: '👥', label: 'Viajes en grupo',     href: 'viaje-grupo.html',    page: '' },
      { icon: '🚂', label: 'Interrail & Eurail',  href: 'interrail.html',      page: 'interrail' },
      { icon: '🌎', label: 'Vuelta al mundo',     href: 'round-the-world.html', page: 'rtw' },
    ];

    let linksHtml = links.map(l =>
      `<a href="${l.href}" class="vm-mob-link${activeClass(l.page)}">
        <span class="vm-mob-icon">${l.icon}</span> ${l.label}
      </a>`
    ).join('');

    let bottomHtml = '';
    if (isAuth) {
      bottomHtml = `
        <div class="vm-mob-divider"></div>
        <a href="profile.html" class="vm-mob-link${activeClass('profile')}">
          <span class="vm-mob-icon">👤</span> Mi perfil
        </a>
        <button class="vm-mob-action" onclick="localStorage.removeItem('token');localStorage.removeItem('user_name');window.location.href='index.html';">
          <span class="vm-mob-icon">🚪</span> Cerrar sesión
        </button>
      `;
    } else {
      bottomHtml = `
        <div class="vm-mob-divider"></div>
        <a href="${loginUrl}" class="vm-mob-action">
          <span class="vm-mob-icon">🔑</span> Entrar
        </a>
        <a href="${signupUrl}" class="vm-mob-signup-btn">Registrarse</a>
      `;
    }

    overlay.innerHTML = `
      <div class="vm-mob-menu">
        <div class="vm-mob-head">
          <a href="${logoHref}" class="vm-topnav-logo">✈️ Viajera<em>Mente</em></a>
          <button class="vm-mob-close" aria-label="Cerrar menú">
            <svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          </button>
        </div>
        <div class="vm-mob-links">
          ${linksHtml}
          ${bottomHtml}
        </div>
      </div>
    `;
    document.body.insertBefore(overlay, document.body.firstChild.nextSibling);
  }

  // ── Bottom Navigation (mobile tab bar) ────────────────────────────
  function injectBottomNav() {
    const tabs = [
      {
        label: 'Inicio', href: 'main.html', page: 'home',
        svg: '<svg class="tab-ic" viewBox="0 0 24 24"><path d="M3 10.5L12 3l9 7.5V21a1 1 0 01-1 1h-5v-6h-6v6H4a1 1 0 01-1-1V10.5z"/></svg>'
      },
      {
        label: 'Guías', href: 'guias.html', page: 'guias',
        svg: '<svg class="tab-ic" viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2V3z"/><path d="M22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7V3z"/></svg>'
      },
      {
        label: 'Planifica', href: 'plan.html', page: 'plan',
        svg: '<svg class="tab-ic" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'
      },
      {
        label: 'Mapa', href: 'mapa.html', page: 'mapa',
        svg: '<svg class="tab-ic" viewBox="0 0 24 24"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg>'
      },
      {
        label: 'Perfil', href: 'profile.html', page: 'profile',
        svg: '<svg class="tab-ic" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
      },
    ];

    const nav = document.createElement('nav');
    nav.className = 'vm-botnav';
    nav.innerHTML = tabs.map(t =>
      `<a href="${t.href}" class="tab${activeClass(t.page)}">
        ${t.svg}
        <span>${t.label}</span>
      </a>`
    ).join('');
    document.body.appendChild(nav);
  }

  // ── Footer ────────────────────────────────────────────────────────
  function injectFooter() {
    const footer = document.createElement('footer');
    footer.className = 'vm-footer';
    footer.innerHTML = `
      <div class="vm-footer-inner">
        <div class="vm-footer-grid">
          <div>
            <a href="index.html" class="vm-footer-brand-logo">✈️ ViajeraMente</a>
            <p class="vm-footer-brand-desc">Guías reales, planificador de rutas y tu mapa personal. Viaja más inteligente.</p>
          </div>
          <div class="vm-footer-col">
            <h4>Explorar</h4>
            <a href="guias.html">Guías</a>
            <a href="plan.html">Planifica</a>
            <a href="mapa.html">Mapa</a>
            <a href="discover.html">Descubrir</a>
            <a href="ranking.html">Ranking</a>
          </div>
          <div class="vm-footer-col">
            <h4>Herramientas</h4>
            <a href="plan.html">Planificador</a>
            <a href="fechas.html">Fechas</a>
            <a href="interrail.html">Interrail</a>
            <a href="round-the-world.html">Vuelta al mundo</a>
          </div>
          <div class="vm-footer-col">
            <h4>Legal</h4>
            <a href="privacidad.html">Privacidad</a>
            <a href="terminos.html">Términos</a>
            <a href="cookies.html">Cookies</a>
            <a href="contacto.html">Contacto</a>
          </div>
        </div>
        <div class="vm-footer-bottom">
          <span class="vm-footer-copy">&copy; 2026 ViajeraMente. Todos los derechos reservados.</span>
          <div class="vm-footer-socials">
            <a href="https://instagram.com/viajeramente" class="vm-footer-social" aria-label="Instagram" rel="noopener noreferrer" target="_blank">
              <svg viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
            </a>
            <a href="https://tiktok.com/@viajeramente" class="vm-footer-social" aria-label="TikTok" rel="noopener noreferrer" target="_blank">
              <svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1v-3.5a6.37 6.37 0 00-.79-.05A6.34 6.34 0 003.15 15.2a6.34 6.34 0 0010.86 4.48V13a8.28 8.28 0 005.58 2.17v-3.44a4.85 4.85 0 01-3.58-1.46V6.69h3.58z"/></svg>
            </a>
            <a href="https://youtube.com/@viajeramente" class="vm-footer-social" aria-label="YouTube" rel="noopener noreferrer" target="_blank">
              <svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
            </a>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(footer);
  }

  // ── Body padding adjustments ──────────────────────────────────────
  function applyBodyPadding() {
    // Top padding for fixed nav
    document.body.style.paddingTop = '56px';

    // Bottom padding for mobile bottom nav (applied via media query in CSS
    // but we also need to add it dynamically for pages that opt in)
    if (cfg.bottomNav) {
      const mqStyle = document.createElement('style');
      mqStyle.textContent = `
        @media (max-width: 768px) {
          body { padding-bottom: 60px !important; }
        }
      `;
      document.head.appendChild(mqStyle);
    }
  }

  // ── Event bindings ────────────────────────────────────────────────
  function bindEvents() {
    const overlay = document.getElementById('vmMobileMenu');
    if (!overlay) return;

    const burger = document.querySelector('.vm-topnav-burger');
    const closeBtn = overlay.querySelector('.vm-mob-close');

    // Open mobile menu
    if (burger) {
      burger.addEventListener('click', function () {
        overlay.classList.add('open');
      });
    }

    // Close via X button
    if (closeBtn) {
      closeBtn.addEventListener('click', function () {
        overlay.classList.remove('open');
      });
    }

    // Close by clicking overlay background (not the menu itself)
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) {
        overlay.classList.remove('open');
      }
    });

    // Close on ESC key
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && overlay.classList.contains('open')) {
        overlay.classList.remove('open');
      }
    });
  }

})();
