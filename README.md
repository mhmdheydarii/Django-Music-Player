<section style="max-width:700px; margin:auto; font-family:Arial, sans-serif; line-height:1.7; color:#333;">
  <h1 style="text-align:center; color:#2c3e50;">Django Music Player</h1>

  <p align="center">
  <img src="./docs/music_player.png" width="700"/>
  </p>
</section>

<h2>⚙️ Installation (Windows)</h2>

<p>Follow these steps to set up and run the project locally.</p>

<hr>

<h3>1. Clone the repository</h3>

```bash
git clone https://github.com/mhmdheydarii/Django-Music-Player.git
```

<br>

<h3>2. Navigate to the project directory</h3>

```bash
cd django_music_player
```

<br>

<h3>6. Run the project</h3>


```bash
docker compose up --build
```

<h3>7. Migrations </h3>
```bash
docker compose exec backend python manage.py makemigrations
```
```bash
docker compose exec backend python manage.py migrate
```

</details>

<br>

<p align="center">
⭐ If you found this project useful, consider giving it a star.
</p>
