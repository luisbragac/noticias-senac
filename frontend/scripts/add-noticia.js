const token = localStorage.getItem('token')

if (!token) window.location.href = 'login.html'

fetch('http://localhost:8000/api/categoria/', {
    headers: { 'Authorization': `Token ${token}` }
})
.then(res => res.json())
.then(categorias => {
    const select = document.querySelector('#categoria')
    select.innerHTML = '<option value="">Escolha...</option>'
    categorias.forEach(cat => {
        select.innerHTML += `<option value="${cat.id}">${cat.nome}</option>`
    })
})

const form = document.querySelector('form')

form.addEventListener('submit', function(event) {
    event.preventDefault()

    const formData = new FormData()
    formData.append('titulo', document.querySelector('#titulo').value)
    formData.append('subtitulo', document.querySelector('#subtitulo').value)
    formData.append('legenda', document.querySelector('#legenda').value)
    formData.append('conteudo', document.querySelector('#conteudo').value)
    formData.append('categoria', document.querySelector('#categoria').value)
    formData.append('ativa', true)
    formData.append('imagem', document.querySelector('#imagem').files[0])

    fetch('http://localhost:8000/api/noticia/', {
        method: 'POST',
        headers: {
            'Authorization': `Token ${token}`
        },
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.id) {
            alert('Notícia adicionada!')
            form.reset()
        } else {
            console.error(data)
            alert('Erro ao adicionar notícia')
        }
    })
})