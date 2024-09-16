from flask import Flask, render_template, request
import folium

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map', methods=['POST'])
def show_map():
    lat = float(request.form['lat'])
    lon = float(request.form['lon'])

    m = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon]).add_to(m)

    # Add rectangle representing the 100x100m square
    folium.Rectangle(bounds=[[lat - 0.00005, lon - 0.00005], [lat + 0.00005, lon + 0.00005]], color='blue', fill=True, fill_color='blue').add_to(m)

    return m._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)
