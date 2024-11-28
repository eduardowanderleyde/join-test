// Open modal
function openModal() {
  document.getElementById("targetModal").style.display = "block";
  document.getElementById("modalBackdrop").style.display = "block";
}

// Close modal
function closeModal() {
  document.getElementById("targetModal").style.display = "none";
  document.getElementById("modalBackdrop").style.display = "none";
}

// Save new target
function saveTarget() {
  const data = {
    //identifier: document.getElementById('identifier').value,
    name: document.getElementById('name').value,
    latitude: document.getElementById('latitude').value,
    longitude: document.getElementById('longitude').value,
    expiration_date: document.getElementById('expiration_date').value,
  };

  fetch('http://127.0.0.1:8000/targets/api/targets/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    body: JSON.stringify(data),
  })
  .then(response => {
    if (response.ok) {
      alert('Alvo salvo com sucesso!');
      location.reload(); 
    } else {
      alert('Erro ao salvar o alvo!');
    }
  })
  .catch(error => {
    console.error('Erro ao salvar alvo:', error);
    alert('Erro ao salvar o alvo!');
  });

}
