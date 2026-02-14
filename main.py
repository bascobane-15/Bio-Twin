st.subheader("🧍 Dijital İkiz Görsel Durum")

last = df.iloc[-1]

C_val = last["Kortizol"]
G_val = last["Kan Şekeri"]
B_val = last["Bağışıklık"]
H_val = last["Homeostaz"]

# Renk Mantığı
brain_color = "yellow" if C_val > 70 else "lightgray"
abdomen_color = "orange" if G_val > 70 else "lightgray"
body_color = "red" if H_val < 50 else "#cccccc"
opacity = 0.5 if B_val < 60 else 1

avatar_html = f"""
<svg width="300" height="500" viewBox="0 0 200 400">
    <!-- Body -->
    <ellipse cx="100" cy="200" rx="60" ry="120" fill="{body_color}" opacity="{opacity}" />
    
    <!-- Head -->
    <circle cx="100" cy="80" r="40" fill="{body_color}" opacity="{opacity}" />
    
    <!-- Brain (Stress Area) -->
    <circle cx="100" cy="70" r="15" fill="{brain_color}" />
    
    <!-- Abdomen (Metabolic Area) -->
    <ellipse cx="100" cy="220" rx="30" ry="40" fill="{abdomen_color}" />
</svg>
"""

st.markdown(avatar_html, unsafe_allow_html=True)








