import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gamepoisk.settings")
django.setup()

from django.core.files import File
from games.models import Game, Screenshot


def add_rdr2():

    if Game.objects.filter(slug="red-dead-redemption-2").exists():
        print("RDR2 уже существует.")
        return

    game = Game.objects.create(
        title="Red Dead Redemption 2",
        description="Открытый мир на Диком Западе с глубоким сюжетом и реалистичной графикой.",
        release_date=date(2018, 10, 26),
        genre="Action, Adventure",
        developer="Rockstar Studios",
        publisher="Rockstar Games",
        platform="PC, PS4, Xbox One",
        edition="Ultimate Edition",
        os_req="Windows 7/8/10 (64-bit)",
        cpu_req="Intel Core i5-2500K / AMD FX-6300",
        ram_req="8 GB",
        gpu_req="NVIDIA GTX 770 2GB / AMD R9 280 3GB",
        disk_req="150 GB",
        slug="red-dead-redemption-2"
    )

    # Главное изображение
    with open("media/game_images/rdr2.jpg", "rb") as img:
        game.image.save("rdr2.jpg", File(img), save=True)

    # Видео
    with open("media/videos/rdr2_trailer.mp4", "rb") as video:
        game.video_url.save("rdr2_trailer.mp4", File(video), save=True)

    # Скриншот 1
    with open("media/screenshots/rdr2_1.jpg", "rb") as img1:
        Screenshot.objects.create(
            game=game,
            image=File(img1, name="rdr2_1.jpg")
        )

    # Скриншот 2
    with open("media/screenshots/rdr2_2.jpg", "rb") as img2:
        Screenshot.objects.create(
            game=game,
            image=File(img2, name="rdr2_2.jpg")
        )

    # Скриншот 3
    with open("media/screenshots/rdr2_3.jpg", "rb") as img3:
        Screenshot.objects.create(
            game=game,
            image=File(img3, name="rdr2_3.jpg")
        )

    print("RDR2 успешно добавлен.")


if __name__ == "__main__":
    add_rdr2()