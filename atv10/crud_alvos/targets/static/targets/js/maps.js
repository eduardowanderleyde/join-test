function initMap() {

  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -23.55052, lng: -46.633308 }, // Coordenadas iniciais (São Paulo)
    zoom: 8, // Nível de zoom
  });

  fetch('http://127.0.0.1:8000/targets/api/targets/')
  .then(response => response.json())
  .then(data => {
    data.forEach(target => {
      new google.maps.Marker({
        position: { lat: parseFloat(target.latitude), lng: parseFloat(target.longitude) },
        map: map,
        title: target.name,
      });
    });
  });
}

