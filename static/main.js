
document.getElementById("invite_bot").onclick = function() {
    window.location.href = "https://discord.com/api/oauth2/authorize?client_id=1165452304825204908&permissions=403488&scope=bot";
  };

document.getElementById('imagenLluvia').onclick = function(event) {
    const x = event.clientX;
    const y = event.clientY;

    const imagenLluvia = document.createElement('img');
    imagenLluvia.src = '/static/CS50_DUCK.png   ';
    imagenLluvia.className = 'lluvia-imagen';
    imagenLluvia.style.left = `${x}px`;
    imagenLluvia.style.left = `${Math.random() * window.innerWidth}px`;
    imagenLluvia.style.top = `${Math.random() * window.innerHeight}px`;
    imagenLluvia.style.animationDuration = `${Math.random() * 2 + 1}s`;
    imagenLluvia.style.animationDelay = `${Math.random()}s`;

    document.body.appendChild(imagenLluvia);

    setTimeout(() => {
      document.body.removeChild(imagenLluvia);
    }, 3000);
  };

document.getElementById('menuBtn').addEventListener('click', function() {
    var explicacion = document.getElementById('explicacion');
    var estiloDisplay = window.getComputedStyle(explicacion).getPropertyValue('display');
    explicacion.style.display = (estiloDisplay === 'none') ? 'block' : 'none';
});
