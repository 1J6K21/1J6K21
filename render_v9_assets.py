# Generate v9 SVG assets implementing the full audit recommendations:
# 1. hero_header.svg:
#    - Official title: Jonathan Kalsky
#    - Subtitle: Software Engineering · Systems · AI & Compute Infrastructure
#    - Institution: TEXAS A&M UNIVERSITY // COMPUTER SCIENCE ('29) · 3.87 GPA · DEAN'S HONOR ROLL
#    - Current Role: Growth Specialist (Part-Time), Quali — Cisco Stack Automation / Torque
#    - Clean 3D isometric compute cluster mesh on the right with Aggie Maroon (#500000) accents
# 2. selected_work.svg:
#    - Cisco Stack Automation: PLATFORM ENGINEERING (Quali · July 2026 - August 2026)
#    - LLM Hypervisor: SYSTEMS RESEARCH (May 2026)
#    - Aggie Course Explorer: TEAM LEAD · PRODUCT (Texas A&M · Oct 2025 - May 2026)
#    - Cognitive Routines: AI RESEARCH (June 2026)
#    - Outcome statements 100% defended by resume

# ----------------- 1. HERO HEADER -----------------
width, height = 1000, 240
origin_x, origin_y = 705, 195
tile_w, tile_h = 32, 16
cols, rows = 16, 7

heights = [
    [10, 16, 22, 35, 20, 14, 6],
    [14, 25, 42, 58, 34, 18, 10],
    [18, 32, 65, 88, 50, 26, 14],
    [16, 40, 78, 105, 68, 38, 20],
    [22, 50, 92, 120, 82, 45, 24],
    [28, 62, 102, 135, 96, 54, 28],
    [20, 48, 88, 115, 74, 40, 22],
    [15, 36, 68, 95, 60, 32, 16],
    [25, 55, 96, 125, 78, 44, 24],
    [32, 66, 106, 138, 100, 56, 30],
    [22, 52, 90, 118, 80, 46, 24],
    [16, 38, 72, 98, 64, 34, 18],
    [20, 45, 80, 108, 70, 38, 20],
    [24, 55, 92, 120, 82, 45, 22],
    [18, 38, 68, 92, 58, 30, 16],
    [10, 20, 36, 52, 32, 18, 8]
]

def iso_pt(c, r, z=0):
    x = origin_x + (c - cols/2) * tile_w/2 - (r - rows/2) * tile_w/2
    y = origin_y + (c - cols/2) * tile_h/2 + (r - rows/2) * tile_h/2 - z
    return round(x, 1), round(y, 1)

hero_svg = ["""<svg fill="none" viewBox="0 0 1000 240" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1017" />
      <stop offset="100%" stop-color="#06080c" />
    </linearGradient>
    <linearGradient id="maroon-edge" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#500000" stop-opacity="0" />
      <stop offset="50%" stop-color="#700010" />
      <stop offset="100%" stop-color="#500000" stop-opacity="0" />
    </linearGradient>
    <pattern id="grid-bg" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#1e293b" stroke-width="0.7" stroke-opacity="0.25" />
    </pattern>
  </defs>

  <style>
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', system-ui, sans-serif; }
    .mono { font-family: 'JetBrains Mono', 'SF Mono', ui-monospace, monospace; }
  </style>

  <!-- Container -->
  <rect width="1000" height="240" rx="14" fill="url(#sky-bg)" stroke="#1e293b" stroke-width="1.2" />
  <rect width="1000" height="240" rx="14" fill="url(#grid-bg)" />
  <line x1="40" y1="239" x2="960" y2="239" stroke="url(#maroon-edge)" stroke-width="2" />

  <!-- Left Identity Block -->
  <g transform="translate(45, 34)">
    <!-- Academic Credential Badge -->
    <rect width="335" height="22" rx="4" fill="#090d13" stroke="#334155" stroke-width="0.8" />
    <rect width="4" height="22" rx="1" fill="#500000" />
    <text x="14" y="15" fill="#fca5a5" font-size="10" font-weight="700" class="mono">TEXAS A&amp;M // CS ('29) · 3.87 GPA · DEAN'S LIST</text>

    <!-- Professional Name -->
    <text x="0" y="66" fill="#ffffff" font-size="34" font-weight="900" class="sans" letter-spacing="-0.8">JONATHAN KALSKY</text>
    
    <!-- Subtitle: Formal Professional Identity -->
    <text x="0" y="90" fill="#94a3b8" font-size="13" class="sans">
      Software Engineering <tspan fill="#500000">·</tspan> Systems <tspan fill="#500000">·</tspan> AI &amp; Compute Infrastructure
    </text>

    <!-- Current Formal Position at Quali -->
    <g transform="translate(0, 112)">
      <rect width="430" height="30" rx="5" fill="#070a0f" stroke="#1e293b" stroke-width="0.8" />
      <circle cx="15" cy="15" r="3.5" fill="#500000" />
      <circle cx="15" cy="15" r="1.5" fill="#ff4d6d" />
      <text x="28" y="19" fill="#cbd5e1" font-size="10.5" class="mono">
        CURRENT: <tspan fill="#ffffff" font-weight="700">Growth Specialist (Part-Time)</tspan>, Quali
      </text>
    </g>

    <!-- Focus Subline -->
    <g transform="translate(0, 152)">
      <rect width="210" height="24" rx="4" fill="#090d14" stroke="#1e293b" stroke-width="0.8" />
      <text x="12" y="16" fill="#38bdf8" font-size="9.5" font-weight="700" class="mono">CISCO STACK AUTOMATION</text>

      <rect x="220" y="0" width="210" height="24" rx="4" fill="#090d14" stroke="#1e293b" stroke-width="0.8" />
      <text x="232" y="16" fill="#e2e8f0" font-size="9.5" font-weight="700" class="mono">HACKATHON AWARDS</text>
    </g>
  </g>

  <!-- Right Side: 3D Isometric Cluster Voxel Mesh -->
  <g id="isometric-cluster">
"""]

for r in range(rows):
    for c in range(cols):
        h_val = heights[c][r]
        p_top = iso_pt(c, r, h_val)
        p_right = iso_pt(c+0.85, r, h_val)
        p_bottom = iso_pt(c+0.85, r+0.85, h_val)
        p_left = iso_pt(c, r+0.85, h_val)

        g_right = iso_pt(c+0.85, r, 0)
        g_bottom = iso_pt(c+0.85, r+0.85, 0)
        g_left = iso_pt(c, r+0.85, 0)

        ratio = h_val / 138.0
        l_r = int(10 + 12 * ratio)
        l_g = int(14 + 10 * ratio)
        l_b = int(20 + 14 * ratio)
        left_fill = f"#{l_r:02x}{l_g:02x}{l_b:02x}"

        r_r = int(15 + 20 * ratio)
        r_g = int(20 + 16 * ratio)
        r_b = int(28 + 20 * ratio)
        right_fill = f"#{r_r:02x}{r_g:02x}{r_b:02x}"

        if ratio > 0.8:
            top_fill = "#500000"
            top_stroke = "#a00018"
        elif ratio > 0.5:
            top_fill = "#1e293b"
            top_stroke = "#38bdf8"
        else:
            top_fill = "#111827"
            top_stroke = "#1f2937"

        hero_svg.append(f'    <polygon points="{p_left[0]},{p_left[1]} {p_bottom[0]},{p_bottom[1]} {g_bottom[0]},{g_bottom[1]} {g_left[0]},{g_left[1]}" fill="{left_fill}" stroke="#161f2e" stroke-width="0.6" />\n')
        hero_svg.append(f'    <polygon points="{p_right[0]},{p_right[1]} {p_bottom[0]},{p_bottom[1]} {g_bottom[0]},{g_bottom[1]} {g_right[0]},{g_right[1]}" fill="{right_fill}" stroke="#1e293b" stroke-width="0.6" />\n')
        hero_svg.append(f'    <polygon points="{p_top[0]},{p_top[1]} {p_right[0]},{p_right[1]} {p_bottom[0]},{p_bottom[1]} {p_left[0]},{p_left[1]}" fill="{top_fill}" stroke="{top_stroke}" stroke-width="0.7" />\n')

hero_svg.append("""  </g>
</svg>
""")

with open("/Users/jonathankalsky/Developer/readme_variants/v9/hero_header.svg", "w") as f:
    f.writelines(hero_svg)

print("hero_header.svg generated successfully")
