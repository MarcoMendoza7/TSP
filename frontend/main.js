const mapa = L.map('mapa').setView([19.43, -99.13], 6);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(mapa);

let seleccion = 'origen';

mapa.on('click', (e) => {
  const latlng = e.latlng;
  fetch(`https://nominatim.openstreetmap.org/reverse?lat=${latlng.lat}&lon=${latlng.lng}&format=json`)
    .then(res => res.json())
    .then(data => {
      const ciudad = data.address.city || data.address.town || data.address.village || "Desconocida";
      document.getElementById(seleccion).value = ciudad;
    });
});

document.getElementById('origen').addEventListener('focus', () => seleccion = 'origen');
document.getElementById('destino').addEventListener('focus', () => seleccion = 'destino');

async function calcularRuta() {
  const origen = document.getElementById('origen').value;
  const destino = document.getElementById('destino').value;
  const medio = document.getElementById('medio').value;
  const gasolina = document.getElementById('gasolina').value;
  const clima = document.getElementById('clima').value;

  const res = await fetch('/api/ruta', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ origen, destino, medio, gasolina, clima })
  });

  const datos = await res.json();
  document.getElementById('info').innerText = JSON.stringify(datos, null, 2);
}
