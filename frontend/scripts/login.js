const form = document.querySelector('form')

form.addEventListener('submit', function(event) {
    event.preventDefault()

    const username = document.querySelector('#username').value
    const senha = document.querySelector('#senha').value

    fetch('http://localhost:8000/api/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password: senha })
    })
    .then(res => res.json())
    .then(data => {
        if (data.token) {
            localStorage.setItem('token', data.token)
            window.location.href = 'view-noticias.html'
        } else {
            alert('Usuário ou senha inválidos')
        }
    })
})