/* ============================================================
   ViajeraMente — Shareable Travel Card Generator
   share-card.js
   Canvas-based card rendering with 3 styles:
     1. Mapa   — Dark background, world map, stats overlay
     2. Stats  — Clean gradient, big numbers, minimal
     3. Pasaporte — Vintage passport style with country stamps
   ============================================================ */

(function () {
  'use strict';

  // ── Simplified world map paths (continent outlines for canvas) ──
  // Normalized coordinates 0-1 range, will be scaled to canvas
  const CONTINENT_PATHS = {
    northAmerica: 'M0.08,0.15 L0.12,0.1 L0.18,0.08 L0.22,0.1 L0.28,0.12 L0.3,0.18 L0.28,0.25 L0.22,0.32 L0.18,0.38 L0.14,0.42 L0.12,0.38 L0.1,0.32 L0.08,0.25 Z',
    southAmerica: 'M0.18,0.48 L0.22,0.45 L0.26,0.48 L0.28,0.55 L0.27,0.62 L0.25,0.7 L0.22,0.78 L0.2,0.82 L0.18,0.78 L0.17,0.7 L0.16,0.6 L0.17,0.52 Z',
    europe: 'M0.42,0.12 L0.46,0.1 L0.52,0.12 L0.54,0.16 L0.52,0.2 L0.48,0.24 L0.44,0.26 L0.42,0.22 L0.4,0.18 L0.41,0.14 Z',
    africa: 'M0.42,0.3 L0.46,0.28 L0.52,0.3 L0.56,0.36 L0.55,0.45 L0.52,0.55 L0.48,0.62 L0.44,0.65 L0.42,0.6 L0.4,0.5 L0.38,0.4 L0.4,0.34 Z',
    asia: 'M0.55,0.08 L0.62,0.06 L0.72,0.08 L0.8,0.12 L0.85,0.18 L0.82,0.25 L0.78,0.32 L0.72,0.36 L0.65,0.38 L0.58,0.34 L0.54,0.28 L0.52,0.2 L0.53,0.14 Z',
    oceania: 'M0.75,0.5 L0.82,0.48 L0.88,0.52 L0.9,0.58 L0.88,0.64 L0.82,0.66 L0.76,0.62 L0.74,0.56 Z',
    antarctica: 'M0.2,0.92 L0.35,0.9 L0.5,0.88 L0.65,0.9 L0.8,0.92 L0.7,0.96 L0.5,0.97 L0.3,0.96 Z'
  };

  // Continent name mapping for visited check
  const CONTINENT_KEYS = {
    'europa': 'europe',
    'asia': 'asia',
    'africa': 'africa',
    'norteamerica': 'northAmerica',
    'sudamerica': 'southAmerica',
    'oceania': 'oceania',
    'antartida': 'antarctica'
  };

  // ── Color Palettes ──
  const PALETTES = {
    mapa: {
      bg1: '#0B1426', bg2: '#1A1040', bg3: '#0D2847',
      accent: '#0EA5E9', accent2: '#10B981', accent3: '#8B5CF6',
      text: '#FFFFFF', textSoft: 'rgba(255,255,255,0.7)',
      textMuted: 'rgba(255,255,255,0.4)',
      mapFill: 'rgba(255,255,255,0.06)', mapVisited: '#0EA5E9',
      cardBg: 'rgba(255,255,255,0.06)', cardBorder: 'rgba(255,255,255,0.1)'
    },
    stats: {
      bg1: '#F8FAFC', bg2: '#E0F2FE', bg3: '#F0FDFA',
      accent: '#0EA5E9', accent2: '#10B981', accent3: '#8B5CF6',
      text: '#0F172A', textSoft: '#64748B',
      textMuted: '#94A3B8',
      cardBg: '#FFFFFF', cardBorder: '#E2E8F0'
    },
    pasaporte: {
      bg1: '#1C1510', bg2: '#2A1F15', bg3: '#1E1A14',
      accent: '#D4A853', accent2: '#C49A3C', accent3: '#B8860B',
      text: '#F5E6C8', textSoft: 'rgba(245,230,200,0.7)',
      textMuted: 'rgba(245,230,200,0.4)',
      cardBg: 'rgba(212,168,83,0.08)', cardBorder: 'rgba(212,168,83,0.2)'
    }
  };

  // ── Helper: parse SVG path to canvas commands ──
  function drawSvgPath(ctx, pathStr, offsetX, offsetY, scaleX, scaleY) {
    const commands = pathStr.match(/[ML]\s*[\d.,\s]+/g);
    if (!commands) return;
    ctx.beginPath();
    commands.forEach(cmd => {
      const type = cmd.charAt(0);
      const coords = cmd.slice(1).trim().split(/[\s,]+/).map(Number);
      const x = coords[0] * scaleX + offsetX;
      const y = coords[1] * scaleY + offsetY;
      if (type === 'M') ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    ctx.closePath();
  }

  // ── Draw noise/grain texture ──
  function drawGrain(ctx, w, h, opacity) {
    const imageData = ctx.createImageData(w, h);
    const data = imageData.data;
    for (let i = 0; i < data.length; i += 4) {
      const v = Math.random() * 255;
      data[i] = v;
      data[i + 1] = v;
      data[i + 2] = v;
      data[i + 3] = opacity * 255;
    }
    ctx.putImageData(imageData, 0, 0);
  }

  // ── Draw world map ──
  function drawWorldMap(ctx, x, y, w, h, visitedContinentKeys, palette, style) {
    Object.entries(CONTINENT_PATHS).forEach(([key, path]) => {
      drawSvgPath(ctx, path, x, y, w, h);
      const isVisited = visitedContinentKeys.includes(key);
      if (style === 'mapa') {
        ctx.fillStyle = isVisited ? palette.mapVisited : palette.mapFill;
        ctx.fill();
        if (isVisited) {
          ctx.shadowColor = palette.accent;
          ctx.shadowBlur = 20;
          ctx.fill();
          ctx.shadowBlur = 0;
        }
      } else if (style === 'pasaporte') {
        ctx.fillStyle = isVisited ? 'rgba(212,168,83,0.35)' : 'rgba(212,168,83,0.08)';
        ctx.fill();
        ctx.strokeStyle = isVisited ? 'rgba(212,168,83,0.6)' : 'rgba(212,168,83,0.15)';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      } else {
        ctx.fillStyle = isVisited ? 'rgba(14,165,233,0.2)' : 'rgba(14,165,233,0.06)';
        ctx.fill();
        ctx.strokeStyle = isVisited ? 'rgba(14,165,233,0.4)' : 'rgba(14,165,233,0.12)';
        ctx.lineWidth = 1;
        ctx.stroke();
      }
    });
  }

  // ── Format large numbers ──
  function fmtNum(n) {
    if (!n || n === 0) return '0';
    if (n >= 100000) return Math.round(n / 1000).toLocaleString('es') + 'k';
    return n.toLocaleString('es');
  }

  // ── Rounded rect helper ──
  function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.quadraticCurveTo(x + w, y, x + w, y + r);
    ctx.lineTo(x + w, y + h - r);
    ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    ctx.lineTo(x + r, y + h);
    ctx.quadraticCurveTo(x, y + h, x, y + h - r);
    ctx.lineTo(x, y + r);
    ctx.quadraticCurveTo(x, y, x + r, y);
    ctx.closePath();
  }

  // ── Draw dots pattern (decorative) ──
  function drawDotsPattern(ctx, x, y, w, h, color, spacing) {
    ctx.fillStyle = color;
    for (let dx = 0; dx < w; dx += spacing) {
      for (let dy = 0; dy < h; dy += spacing) {
        ctx.beginPath();
        ctx.arc(x + dx, y + dy, 1, 0, Math.PI * 2);
        ctx.fill();
      }
    }
  }

  // ══════════════════════════════════════════════
  //  STYLE 1: MAPA — Dark background, world map
  // ══════════════════════════════════════════════
  function drawStyleMapa(ctx, w, h, data) {
    const p = PALETTES.mapa;

    // Background gradient
    const bgGrad = ctx.createLinearGradient(0, 0, w, h);
    bgGrad.addColorStop(0, p.bg1);
    bgGrad.addColorStop(0.5, p.bg2);
    bgGrad.addColorStop(1, p.bg3);
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, w, h);

    // Subtle radial glow
    const glow = ctx.createRadialGradient(w * 0.3, h * 0.4, 0, w * 0.3, h * 0.4, w * 0.6);
    glow.addColorStop(0, 'rgba(14,165,233,0.08)');
    glow.addColorStop(1, 'transparent');
    ctx.fillStyle = glow;
    ctx.fillRect(0, 0, w, h);

    // Grain texture
    ctx.save();
    ctx.globalAlpha = 0.03;
    drawGrain(ctx, w, h, 1);
    ctx.restore();

    // World map (centered, large)
    const mapW = w * 0.85;
    const mapH = h * 0.38;
    const mapX = (w - mapW) / 2;
    const mapY = h * 0.14;
    drawWorldMap(ctx, mapX, mapY, mapW, mapH, data.visitedContinentKeys, p, 'mapa');

    // User name + rank at top
    ctx.textAlign = 'center';
    ctx.fillStyle = p.text;
    ctx.font = `800 ${w * 0.055}px 'Space Grotesk', sans-serif`;
    ctx.fillText(data.name || 'Viajero', w / 2, h * 0.09);

    // Rank badge
    ctx.font = `600 ${w * 0.028}px 'Inter', sans-serif`;
    ctx.fillStyle = p.accent;
    const rankText = `${data.rankEmoji} ${data.rankName}`;
    const rankW = ctx.measureText(rankText).width + 24;
    roundRect(ctx, (w - rankW) / 2, h * 0.1, rankW, w * 0.038, w * 0.019);
    ctx.fillStyle = 'rgba(14,165,233,0.15)';
    ctx.fill();
    ctx.strokeStyle = 'rgba(14,165,233,0.4)';
    ctx.lineWidth = 1;
    ctx.stroke();
    ctx.fillStyle = p.accent;
    ctx.font = `600 ${w * 0.025}px 'Inter', sans-serif`;
    ctx.fillText(rankText, w / 2, h * 0.1 + w * 0.028);

    // Stats row below map
    const statsY = h * 0.56;
    const stats = [
      { icon: '🌍', value: data.countries, label: 'Países' },
      { icon: '🏙️', value: data.cities, label: 'Ciudades' },
      { icon: '✈️', value: fmtNum(data.km), label: 'Km' },
      { icon: '🗺️', value: `${data.continents}/7`, label: 'Continentes' },
      { icon: '🏛️', value: `${data.wonders}/7`, label: 'Maravillas' },
    ];

    const cardW = w * 0.17;
    const cardH = h * 0.14;
    const totalW = stats.length * cardW + (stats.length - 1) * (w * 0.015);
    const startX = (w - totalW) / 2;

    stats.forEach((s, i) => {
      const cx = startX + i * (cardW + w * 0.015);
      const cy = statsY;

      // Card background
      roundRect(ctx, cx, cy, cardW, cardH, 12);
      ctx.fillStyle = p.cardBg;
      ctx.fill();
      ctx.strokeStyle = p.cardBorder;
      ctx.lineWidth = 1;
      ctx.stroke();

      // Icon
      ctx.textAlign = 'center';
      ctx.font = `${w * 0.032}px serif`;
      ctx.fillText(s.icon, cx + cardW / 2, cy + cardH * 0.3);

      // Value
      ctx.fillStyle = p.text;
      ctx.font = `800 ${w * 0.038}px 'Space Grotesk', sans-serif`;
      ctx.fillText(String(s.value), cx + cardW / 2, cy + cardH * 0.6);

      // Label
      ctx.fillStyle = p.textMuted;
      ctx.font = `500 ${w * 0.018}px 'Inter', sans-serif`;
      ctx.fillText(s.label, cx + cardW / 2, cy + cardH * 0.82);
    });

    // Percentile badge
    if (data.percentile) {
      const percY = h * 0.76;
      ctx.textAlign = 'center';
      ctx.font = `700 ${w * 0.026}px 'Inter', sans-serif`;
      ctx.fillStyle = p.accent2;
      ctx.fillText(`Top ${data.percentile}% de viajeros`, w / 2, percY);
    }

    // Decorative line
    ctx.strokeStyle = 'rgba(255,255,255,0.06)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(w * 0.15, h * 0.82);
    ctx.lineTo(w * 0.85, h * 0.82);
    ctx.stroke();

    // Brand footer
    drawBrandFooter(ctx, w, h, p, 'mapa');
  }

  // ══════════════════════════════════════════════
  //  STYLE 2: STATS — Clean gradient, big numbers
  // ══════════════════════════════════════════════
  function drawStyleStats(ctx, w, h, data) {
    const p = PALETTES.stats;

    // Light gradient background
    const bgGrad = ctx.createLinearGradient(0, 0, w, h);
    bgGrad.addColorStop(0, '#F8FAFC');
    bgGrad.addColorStop(0.4, '#E0F2FE');
    bgGrad.addColorStop(0.7, '#F0FDFA');
    bgGrad.addColorStop(1, '#EDE9FE');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, w, h);

    // Decorative circles
    ctx.fillStyle = 'rgba(14,165,233,0.06)';
    ctx.beginPath();
    ctx.arc(w * 0.85, h * 0.15, w * 0.25, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = 'rgba(16,185,129,0.05)';
    ctx.beginPath();
    ctx.arc(w * 0.1, h * 0.8, w * 0.2, 0, Math.PI * 2);
    ctx.fill();

    // Top section: name + rank
    ctx.textAlign = 'center';
    ctx.fillStyle = p.text;
    ctx.font = `800 ${w * 0.06}px 'Space Grotesk', sans-serif`;
    ctx.fillText(data.name || 'Viajero', w / 2, h * 0.1);

    // Rank pill
    const rankText = `${data.rankEmoji} ${data.rankName}`;
    ctx.font = `600 ${w * 0.025}px 'Inter', sans-serif`;
    const rw = ctx.measureText(rankText).width + 28;
    roundRect(ctx, (w - rw) / 2, h * 0.115, rw, w * 0.04, w * 0.02);
    ctx.fillStyle = 'rgba(14,165,233,0.1)';
    ctx.fill();
    ctx.strokeStyle = 'rgba(14,165,233,0.3)';
    ctx.lineWidth = 1.5;
    ctx.stroke();
    ctx.fillStyle = p.accent;
    ctx.fillText(rankText, w / 2, h * 0.115 + w * 0.03);

    // Big stats — 2 columns, 3 rows
    const statsData = [
      { icon: '🌍', value: String(data.countries), label: 'países visitados' },
      { icon: '🏙️', value: String(data.cities), label: 'ciudades' },
      { icon: '✈️', value: fmtNum(data.km), label: 'km recorridos' },
      { icon: '🗺️', value: `${data.continents}/7`, label: 'continentes' },
      { icon: '🏛️', value: `${data.wonders}/7`, label: 'maravillas' },
      { icon: '⭐', value: String(data.points || 0), label: 'puntos' },
    ];

    const cols = 2;
    const rows = 3;
    const cardW = w * 0.38;
    const cardH = h * 0.135;
    const gapX = w * 0.06;
    const gapY = h * 0.02;
    const gridW = cols * cardW + (cols - 1) * gapX;
    const gridStartX = (w - gridW) / 2;
    const gridStartY = h * 0.2;

    statsData.forEach((s, i) => {
      const col = i % cols;
      const row = Math.floor(i / cols);
      const cx = gridStartX + col * (cardW + gapX);
      const cy = gridStartY + row * (cardH + gapY);

      // White card
      roundRect(ctx, cx, cy, cardW, cardH, 16);
      ctx.fillStyle = 'rgba(255,255,255,0.85)';
      ctx.fill();
      ctx.shadowColor = 'rgba(0,0,0,0.06)';
      ctx.shadowBlur = 12;
      ctx.shadowOffsetY = 4;
      ctx.fill();
      ctx.shadowBlur = 0;
      ctx.shadowOffsetY = 0;
      ctx.strokeStyle = p.cardBorder;
      ctx.lineWidth = 1;
      ctx.stroke();

      // Icon
      ctx.textAlign = 'left';
      ctx.font = `${w * 0.035}px serif`;
      ctx.fillText(s.icon, cx + cardW * 0.08, cy + cardH * 0.5);

      // Value
      ctx.fillStyle = p.text;
      ctx.font = `800 ${w * 0.05}px 'Space Grotesk', sans-serif`;
      ctx.fillText(s.value, cx + cardW * 0.28, cy + cardH * 0.48);

      // Label
      ctx.fillStyle = p.textSoft;
      ctx.font = `500 ${w * 0.02}px 'Inter', sans-serif`;
      ctx.fillText(s.label, cx + cardW * 0.28, cy + cardH * 0.72);
    });

    // Mini world map (subtle, in background between stats and footer)
    const mapW = w * 0.6;
    const mapH = h * 0.2;
    const mapX = (w - mapW) / 2;
    const mapY = h * 0.68;
    drawWorldMap(ctx, mapX, mapY, mapW, mapH, data.visitedContinentKeys, p, 'stats');

    // Percentile
    if (data.percentile) {
      ctx.textAlign = 'center';
      ctx.fillStyle = p.accent2;
      ctx.font = `700 ${w * 0.026}px 'Inter', sans-serif`;
      ctx.fillText(`Top ${data.percentile}% de viajeros`, w / 2, h * 0.67);
    }

    // Brand footer
    drawBrandFooter(ctx, w, h, p, 'stats');
  }

  // ══════════════════════════════════════════════
  //  STYLE 3: PASAPORTE — Vintage passport style
  // ══════════════════════════════════════════════
  function drawStylePasaporte(ctx, w, h, data) {
    const p = PALETTES.pasaporte;

    // Dark leather background
    const bgGrad = ctx.createLinearGradient(0, 0, w, h);
    bgGrad.addColorStop(0, p.bg1);
    bgGrad.addColorStop(0.5, p.bg2);
    bgGrad.addColorStop(1, p.bg3);
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, w, h);

    // Leather grain texture
    ctx.save();
    ctx.globalAlpha = 0.04;
    drawGrain(ctx, w, h, 1);
    ctx.restore();

    // Gold border (double line)
    ctx.strokeStyle = 'rgba(212,168,83,0.4)';
    ctx.lineWidth = 3;
    roundRect(ctx, w * 0.04, h * 0.03, w * 0.92, h * 0.94, 16);
    ctx.stroke();
    ctx.strokeStyle = 'rgba(212,168,83,0.2)';
    ctx.lineWidth = 1;
    roundRect(ctx, w * 0.06, h * 0.05, w * 0.88, h * 0.9, 12);
    ctx.stroke();

    // Gold dots pattern in corners
    drawDotsPattern(ctx, w * 0.07, h * 0.06, w * 0.1, h * 0.06, 'rgba(212,168,83,0.12)', 8);
    drawDotsPattern(ctx, w * 0.83, h * 0.88, w * 0.1, h * 0.06, 'rgba(212,168,83,0.12)', 8);

    // "PASAPORTE" header
    ctx.textAlign = 'center';
    ctx.fillStyle = p.accent;
    ctx.font = `700 ${w * 0.022}px 'Inter', sans-serif`;
    ctx.letterSpacing = '0.2em';
    ctx.fillText('P A S A P O R T E   V I A J E R O', w / 2, h * 0.1);

    // Decorative line under header
    const lineGrad = ctx.createLinearGradient(w * 0.2, 0, w * 0.8, 0);
    lineGrad.addColorStop(0, 'transparent');
    lineGrad.addColorStop(0.5, 'rgba(212,168,83,0.5)');
    lineGrad.addColorStop(1, 'transparent');
    ctx.strokeStyle = lineGrad;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(w * 0.2, h * 0.12);
    ctx.lineTo(w * 0.8, h * 0.12);
    ctx.stroke();

    // Name
    ctx.fillStyle = p.text;
    ctx.font = `800 ${w * 0.052}px 'Space Grotesk', sans-serif`;
    ctx.fillText(data.name || 'Viajero', w / 2, h * 0.18);

    // Rank badge (gold style)
    const rankText = `${data.rankEmoji} ${data.rankName}`;
    ctx.font = `600 ${w * 0.024}px 'Inter', sans-serif`;
    const rw = ctx.measureText(rankText).width + 24;
    roundRect(ctx, (w - rw) / 2, h * 0.195, rw, w * 0.038, w * 0.019);
    ctx.fillStyle = 'rgba(212,168,83,0.12)';
    ctx.fill();
    ctx.strokeStyle = 'rgba(212,168,83,0.4)';
    ctx.lineWidth = 1;
    ctx.stroke();
    ctx.fillStyle = p.accent;
    ctx.fillText(rankText, w / 2, h * 0.195 + w * 0.028);

    // World map (passport style, centered)
    const mapW = w * 0.7;
    const mapH = h * 0.22;
    const mapX = (w - mapW) / 2;
    const mapY = h * 0.26;
    drawWorldMap(ctx, mapX, mapY, mapW, mapH, data.visitedContinentKeys, p, 'pasaporte');

    // Stats as passport "stamps"
    const stamps = [
      { icon: '🌍', value: data.countries, label: 'PAÍSES' },
      { icon: '🏙️', value: data.cities, label: 'CIUDADES' },
      { icon: '✈️', value: fmtNum(data.km), label: 'KM' },
    ];
    const stamps2 = [
      { icon: '🗺️', value: `${data.continents}/7`, label: 'CONTINENTES' },
      { icon: '🏛️', value: `${data.wonders}/7`, label: 'MARAVILLAS' },
    ];

    // First row of stamps
    const stampW = w * 0.25;
    const stampH = h * 0.12;
    const stampStartY = h * 0.52;

    stamps.forEach((s, i) => {
      const sx = w * 0.1 + i * (stampW + w * 0.025);
      const sy = stampStartY;

      // Stamp circle/rect with rotation
      ctx.save();
      ctx.translate(sx + stampW / 2, sy + stampH / 2);
      ctx.rotate((Math.random() - 0.5) * 0.08);
      ctx.translate(-(sx + stampW / 2), -(sy + stampH / 2));

      roundRect(ctx, sx, sy, stampW, stampH, 8);
      ctx.fillStyle = p.cardBg;
      ctx.fill();
      ctx.strokeStyle = p.cardBorder;
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 3]);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.textAlign = 'center';
      ctx.font = `${w * 0.03}px serif`;
      ctx.fillText(s.icon, sx + stampW / 2, sy + stampH * 0.35);

      ctx.fillStyle = p.text;
      ctx.font = `800 ${w * 0.04}px 'Space Grotesk', sans-serif`;
      ctx.fillText(String(s.value), sx + stampW / 2, sy + stampH * 0.65);

      ctx.fillStyle = p.textMuted;
      ctx.font = `600 ${w * 0.015}px 'Inter', sans-serif`;
      ctx.fillText(s.label, sx + stampW / 2, sy + stampH * 0.88);

      ctx.restore();
    });

    // Second row of stamps
    const stamp2W = w * 0.35;
    const stamp2StartY = h * 0.67;

    stamps2.forEach((s, i) => {
      const sx = w * 0.1 + i * (stamp2W + w * 0.05);
      const sy = stamp2StartY;

      ctx.save();
      ctx.translate(sx + stamp2W / 2, sy + stampH / 2);
      ctx.rotate((Math.random() - 0.5) * 0.06);
      ctx.translate(-(sx + stamp2W / 2), -(sy + stampH / 2));

      roundRect(ctx, sx, sy, stamp2W, stampH, 8);
      ctx.fillStyle = p.cardBg;
      ctx.fill();
      ctx.strokeStyle = p.cardBorder;
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 3]);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.textAlign = 'center';
      ctx.font = `${w * 0.03}px serif`;
      ctx.fillText(s.icon, sx + stamp2W / 2, sy + stampH * 0.35);

      ctx.fillStyle = p.text;
      ctx.font = `800 ${w * 0.04}px 'Space Grotesk', sans-serif`;
      ctx.fillText(String(s.value), sx + stamp2W / 2, sy + stampH * 0.65);

      ctx.fillStyle = p.textMuted;
      ctx.font = `600 ${w * 0.015}px 'Inter', sans-serif`;
      ctx.fillText(s.label, sx + stamp2W / 2, sy + stampH * 0.88);

      ctx.restore();
    });

    // Percentile
    if (data.percentile) {
      ctx.textAlign = 'center';
      ctx.fillStyle = p.accent;
      ctx.font = `700 ${w * 0.024}px 'Inter', sans-serif`;
      ctx.fillText(`Top ${data.percentile}% de viajeros`, w / 2, h * 0.84);
    }

    // Brand footer
    drawBrandFooter(ctx, w, h, p, 'pasaporte');
  }

  // ── Brand Footer ──
  function drawBrandFooter(ctx, w, h, palette, style) {
    ctx.textAlign = 'center';

    if (style === 'pasaporte') {
      // Gold decorative line
      const lineGrad = ctx.createLinearGradient(w * 0.2, 0, w * 0.8, 0);
      lineGrad.addColorStop(0, 'transparent');
      lineGrad.addColorStop(0.5, 'rgba(212,168,83,0.4)');
      lineGrad.addColorStop(1, 'transparent');
      ctx.strokeStyle = lineGrad;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(w * 0.2, h * 0.88);
      ctx.lineTo(w * 0.8, h * 0.88);
      ctx.stroke();
    }

    // Logo text
    const logoY = h * 0.93;
    ctx.font = `700 ${w * 0.032}px 'Space Grotesk', sans-serif`;
    ctx.fillStyle = style === 'stats' ? '#0F172A' : palette.text;
    ctx.fillText('ViajeraMente', w / 2, logoY);

    // URL
    ctx.font = `400 ${w * 0.02}px 'Inter', sans-serif`;
    ctx.fillStyle = style === 'stats' ? '#64748B' : palette.textSoft;
    ctx.fillText('viajeramente.com', w / 2, logoY + w * 0.032);
  }

  // ══════════════════════════════════════════════
  //  PUBLIC API
  // ══════════════════════════════════════════════

  /**
   * Generate travel card as canvas.
   * @param {Object} data - User travel data
   * @param {string} style - 'mapa' | 'stats' | 'pasaporte'
   * @param {string} format - 'square' (1080x1080) | 'story' (1080x1920)
   * @returns {HTMLCanvasElement}
   */
  function generateCard(data, style = 'mapa', format = 'square') {
    const canvas = document.createElement('canvas');
    const w = 1080;
    const h = format === 'story' ? 1920 : 1080;
    canvas.width = w;
    canvas.height = h;
    const ctx = canvas.getContext('2d');

    // Map visited continents to internal keys
    const visitedContinentKeys = [];
    if (data.visitedContinents) {
      data.visitedContinents.forEach(c => {
        const key = CONTINENT_KEYS[c.toLowerCase()] || CONTINENT_KEYS[c];
        if (key) visitedContinentKeys.push(key);
      });
    }
    data.visitedContinentKeys = visitedContinentKeys;

    // Draw based on style
    switch (style) {
      case 'stats':
        drawStyleStats(ctx, w, h, data);
        break;
      case 'pasaporte':
        drawStylePasaporte(ctx, w, h, data);
        break;
      case 'mapa':
      default:
        drawStyleMapa(ctx, w, h, data);
        break;
    }

    return canvas;
  }

  /**
   * Get card as data URL (PNG).
   */
  function getCardDataURL(data, style, format) {
    const canvas = generateCard(data, style, format);
    return canvas.toDataURL('image/png');
  }

  /**
   * Download the card as PNG.
   */
  function downloadCard(data, style, format) {
    const dataUrl = getCardDataURL(data, style, format);
    const link = document.createElement('a');
    link.download = `viajeramente-${data.name || 'viajero'}-${style}.png`;
    link.href = dataUrl;
    link.click();
  }

  /**
   * Share via Web Share API (mobile), fallback to download.
   */
  async function shareCard(data, style, format) {
    const canvas = generateCard(data, style, format);

    if (navigator.share && navigator.canShare) {
      try {
        const blob = await new Promise(resolve => canvas.toBlob(resolve, 'image/png'));
        const file = new File([blob], `viajeramente-${style}.png`, { type: 'image/png' });

        if (navigator.canShare({ files: [file] })) {
          await navigator.share({
            title: `Mi mapa de viajes — ViajeraMente`,
            text: `He visitado ${data.countries} países y ${data.cities} ciudades. ¿Cuántos llevas tú? 🌍`,
            files: [file],
            url: 'https://viajeramente.com'
          });
          return true;
        }
      } catch (err) {
        if (err.name === 'AbortError') return false;
        console.warn('Web Share API failed, falling back to download:', err);
      }
    }

    // Fallback: download
    downloadCard(data, style, format);
    return true;
  }

  /**
   * Gather current user data from the page state.
   */
  function gatherUserData() {
    const user = (typeof currentUser !== 'undefined') ? currentUser : {};
    const visitedCodesSet = (typeof visitedCodes !== 'undefined') ? visitedCodes : new Set();
    const visitedContinentsSet = (typeof visitedContinents !== 'undefined') ? visitedContinents : new Set();
    const visitedWondersSet = (typeof visitedWonders !== 'undefined') ? visitedWonders : new Set();

    const countries = visitedCodesSet.size;
    const cityCount = (typeof visitedCitiesCount !== 'undefined') ? visitedCitiesCount : 0;
    const km = user.km_traveled || 0;
    const points = user.points || 0;
    const rankName = user.rank_level || 'Curioso';

    // Get rank emoji
    const rankThresholds = (typeof RANK_THRESHOLDS !== 'undefined') ? RANK_THRESHOLDS : [];
    const rankInfo = rankThresholds.find(r => r.name === rankName) || { emoji: '🌱' };

    // Calculate percentile (rough estimate based on points)
    // We'll do a simple calculation; the API endpoint provides real data
    let percentile = null;
    if (points > 0) {
      // Rough estimate: most users have low points
      if (points >= 1000) percentile = 1;
      else if (points >= 500) percentile = 5;
      else if (points >= 200) percentile = 15;
      else if (points >= 50) percentile = 30;
      else percentile = 50;
    }

    return {
      name: user.name || user.username || 'Viajero',
      username: user.username || 'viajero',
      avatarUrl: user.avatar_url || null,
      countries: countries,
      cities: cityCount,
      km: km,
      continents: visitedContinentsSet.size,
      wonders: visitedWondersSet.size,
      points: points,
      rankName: rankName,
      rankEmoji: rankInfo.emoji || '🌱',
      percentile: percentile,
      visitedContinents: [...visitedContinentsSet]
    };
  }

  // Expose globally
  window.ShareCard = {
    generate: generateCard,
    getDataURL: getCardDataURL,
    download: downloadCard,
    share: shareCard,
    gatherData: gatherUserData
  };

})();
