import streamlit as st

st.set_page_config(layout="wide")

st.title("🧬 Dijital İkiz – Holografik Homeostaz")

# =========================
# SIDEBAR
# =========================
st.sidebar.header("Girdi Parametreleri")

stress = st.sidebar.slider("Stres Seviyesi (0-10)", 0, 10, 5)
sleep = st.sidebar.slider("Uyku Süresi (Saat)", 0, 10, 7)
days = st.sidebar.slider("Simülasyon Süresi (Gün)", 1, 60, 30)

# =========================
# HOMEOSTAZ HESABI
# =========================
homeostasis = (sleep * 10) - (stress * 8)
homeostasis = max(0, min(100, homeostasis))

st.subheader(f"Homeostaz Skoru: {homeostasis}")

# =========================
# RENK HESAPLAMA
# =========================
if homeostasis > 70:
    body_color = "#00FFFF"
elif homeostasis > 40:
    body_color = "#FFD700"
else:
    body_color = "#FF3B3B"

brain_glow = min(1, stress / 10)

# =========================
# SVG AVATAR
# =========================
svg_code = f"""
<svg width="300" height="500" viewBox="0 0 300 500">

<style>
@keyframes pulse {{
  0% {{ opacity: 0.7; }}
  50% {{ opacity: 1; }}
  100% {{ opacity: 0.7; }}
}}
.hologram {
  fill: """ + body_color + """;
  opacity: 0.6;
  animation: pulse 2s infinite;
  filter: drop-shadow(0 0 15px """ + body_color + """);
}}

.brain {{
  fill: yellow;
  opacity: {brain_glow};
}}
</style>

<!-- Aura -->
<ellipse cx="150" cy="250" rx="90" ry="200" fill="{body_color}" opacity="0.2"/>

<!-- Body -->
<ellipse cx="150" cy="250" rx="70" ry="180" class="hologram"/>

<!-- Head -->
<circle cx="150" cy="80" r="50" class="hologram"/>

<!-- Brain -->
<circle cx="150" cy="70" r="20" class="brain"/>

</svg>
"""

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)






