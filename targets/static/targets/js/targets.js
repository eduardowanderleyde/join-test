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

// Abrir modal com os detalhes do alvo para edição
function openTargetDetails(targetId) {
  fetch(`http://127.0.0.1:8000/targets/api/targets/${targetId}/`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then(response => response.json())
    .then(target => {
      // Preencher os campos do modal
      document.getElementById('name').value = target.name;
      document.getElementById('latitude').value = target.latitude;
      document.getElementById('longitude').value = target.longitude;
      document.getElementById('expiration_date').value = target.expiration_date;

      // Atualizar os botões do modal
      document.getElementById('saveButton').setAttribute('data-id', target.id);
      document.getElementById('deleteButton').setAttribute('data-id', target.id);
      document.getElementById('deleteButton').style.display = 'inline-block';

      // Alterar o título do modal
      document.getElementById('modalTitle').innerText = 'Editar Alvo';

      // Abrir o modal
      openModal();
    })
    .catch(error => {
      console.error('Erro ao carregar detalhes do alvo:', error);
      alert('Erro ao carregar os detalhes do alvo.');
    });
}

// Excluir alvo
function deleteTarget() {
  const targetId = document.getElementById('deleteButton').getAttribute('data-id');

  if (!targetId) {
    alert('Nenhum alvo selecionado para exclusão!');
    return;
  }

  fetch(`http://127.0.0.1:8000/targets/api/targets/${targetId}/`, {
    method: 'DELETE',
    headers: {
      'X-CSRFToken': csrfToken,
    },
  })
    .then(response => {
      if (response.ok) {
        alert('Alvo excluído com sucesso!');
        location.reload(); // Recarregar o mapa
      } else {
        alert('Erro ao excluir o alvo!');
      }
    })
    .catch(error => {
      console.error('Erro ao excluir alvo:', error);
      alert('Erro ao excluir o alvo!');
    });
}
