import streamlit as st
import folium
from streamlit_folium import st_folium

FLOOD_ZONES = {
    'velachery': [12.9759, 80.2206, 95],
    'tambaram': [12.9249, 80.1000, 80],
    't nagar': [13.0418, 80.2341, 80],
    'adyar': [13.0067, 80.2570, 70],
    'anna nagar': [13.0850, 80.2101, 20],
    'mogappair': [13.0800, 80.1900, 15],
    'marina beach': [13.0500, 80.2824, 60],
}

st.set_page_config(layout='wide')
st.title('Chennai Flood Safe Route Finder')
st.write('Flood Avoidance Path System with Live Map')

col1, col2 = st.columns([1, 2])

with col1:
    from_place = st.text_input('FROM Location', 'anna nagar')
    to_place = st.text_input('TO Location', 'velachery')
    find = st.button('Find Safe Route')
    if find:
        to_data = FLOOD_ZONES.get(to_place.lower(), [13.0827, 80.2707, 25])
        risk = to_data[2]
        if risk > 70:
            st.error(f'DANGER - AVOID {to_place.upper()}! Risk {risk}%')
            st.warning('Safe Route: Go via Anna Nagar -> Mogappair')
        elif risk > 40:
            st.warning(f'CAUTION - {to_place} Risk {risk}%')
        else:
            st.success(f'SAFE - {to_place} route is clear')

with col2:
    m = folium.Map(location=[13.0827, 80.2707], zoom_start=11)
    for place, data in FLOOD_ZONES.items():
        lat, lon, risk = data
        color = 'red' if risk > 70 else 'orange' if risk > 40 else 'green'
        folium.CircleMarker(location=[lat, lon], radius=10, color=color, fill=True, popup=f'{place} - {risk}%').add_to(m)
    st_folium(m, width=700, height=500)
