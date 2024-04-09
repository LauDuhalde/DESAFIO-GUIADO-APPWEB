from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
                        <!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Inicio - Mi Aplicación</title>
<!-- Enlace al archivo CSS de Bootstrap -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
<!-- Estilos personalizados -->
<style>
  /* Estilos adicionales para la página de inicio */
  .hero-section {
    background-image: url('https://i.pinimg.com/1200x/79/f7/35/79f735bdc978bb91c3459899cad1a99a.jpg'); /* Cambia la URL por la imagen de fondo que desees */
    background-size: cover;
    background-position: center;
    height: 600px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
  }

  .hero-section h1 {
    font-size: 3rem;
    margin-bottom: 20px;
  }

  .hero-section p {
    font-size: 1.5rem;
    margin-bottom: 30px;
  }

  .btn-primary {
    font-size: 1.2rem;
    padding: 10px 20px;
  }
</style>
</head>
<body>

<!-- Barra de navegación -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="#">Mi Aplicación</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <a class="nav-link" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="about/">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="contact/">Contact</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<!-- Sección de héroe (sección principal) -->
<section class="hero-section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1>Bienvenido a Mi Aplicación</h1>
        <p>Una aplicación increíble para tus necesidades.</p>
      </div>
    </div>
  </div>
</section>

<!-- Sección de características -->
<section class="py-5">
  <div class="container">
    <div class="row">
      <div class="col-lg-4">
        <h2>Característica 1</h2>
        <p>Descripción de la característica 1.</p>
      </div>
      <div class="col-lg-4">
        <h2>Característica 2</h2>
        <p>Descripción de la característica 2.</p>
      </div>
      <div class="col-lg-4">
        <h2>Característica 3</h2>
        <p>Descripción de la característica 3.</p>
      </div>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="bg-dark text-white py-4">
  <div class="container text-center">
    <p>&copy; 2024 Mi Aplicación. Todos los derechos reservados.</p>
  </div>
</footer>

<!-- Enlace al archivo JS de Bootstrap -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>

                        """)
    
def about(request):
    return HttpResponse("""
                        <!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Acerca de - Mi Aplicación</title>
<!-- Enlace al archivo CSS de Bootstrap -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<!-- Barra de navegación -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="#">Mi Aplicación</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <a class="nav-link" href="../">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="../contact/">Contact</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<!-- Contenido de la página de About -->
<section class="py-5">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1>Acerca de Nosotros</h1>
        <p>Somos una increíble aplicación que...</p>
      </div>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="bg-dark text-white py-4">
  <div class="container text-center">
    <p>&copy; 2024 Mi Aplicación. Todos los derechos reservados.</p>
  </div>
</footer>

<!-- Enlace al archivo JS de Bootstrap -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>

                        """)
    
def contact(request):
    return HttpResponse("""
                        <!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contacto - Mi Aplicación</title>
<!-- Enlace al archivo CSS de Bootstrap -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<!-- Barra de navegación -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="#">Mi Aplicación</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <a class="nav-link" href="../">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="../about/">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Contact</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<!-- Contenido de la página de Contacto -->
<section class="py-5">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1>Contacto</h1>
        <p>Por favor, complete el siguiente formulario para contactarnos:</p>
        <form>
          <div class="mb-3">
            <label for="nombre" class="form-label">Nombre</label>
            <input type="text" class="form-control" id="nombre">
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" class="form-control" id="email">
          </div>
          <div class="mb-3">
            <label for="mensaje" class="form-label">Mensaje</label>
            <textarea class="form-control" id="mensaje" rows="5"></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Enviar Mensaje</button>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="bg-dark text-white py-4">
  <div class="container text-center">
    <p>&copy; 2024 Mi Aplicación. Todos los derechos reservados.</p>
  </div>
</footer>

<!-- Enlace al archivo JS de Bootstrap -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>

                        """)
