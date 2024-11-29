function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -23.55052, lng: -46.633308 }, // Coordenadas iniciais (São Paulo)
    zoom: 8, // Nível de zoom
  });

  // Buscar os alvos da API
  fetch('http://127.0.0.1:8000/targets/api/targets/')
    .then(response => response.json())
    .then(data => {
      data.forEach(target => {
        const marker = new google.maps.Marker({
          position: { lat: parseFloat(target.latitude), lng: parseFloat(target.longitude) },
          map: map,
          title: target.name,
        });

        // Evento de clique para abrir o modal com os detalhes
        marker.addListener('click', () => {
          openTargetDetails(target.id);
        });
      });
    })
    .catch(error => {
      console.error('Erro ao carregar os alvos:', error);
    });
}
