import os
import django

# 1. Kažemo sistemu gde su podešavanja
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# 2. "Palimo" Django
django.setup()


# --- SADA MOŽEŠ DA PIŠEŠ KOD ---
from blog.models import Post, Tag
from django.contrib.auth.models import User
from django.db.models import Q



user = User.objects.get(username="vstarcevic")
if not Post.objects.filter(slug='test-post-iz-fajla').exists():
    Post.objects.create(
        title="Test post iz fajla",
        slug='test-post-iz-fajla',
        body="Ovo je iz IDE napisano",
        author=user,
        status=Post.Status.PUBLISHED,
    )
# Svi koji u naslovu imaju reč "Test"
test_postovi = Post.objects.filter(title__contains='test')
print(f"Pronadjeno test postova: {test_postovi.count()}")

print("--- START LABORATORIJE ---")

# Primer: Dohvati sve i ispiši naslove
postovi = Post.objects.all()
for p in postovi:
    print(f"Naslov: {p.title} | Status: {p.status}")

print("--- KRAJ ---")
prva_dva = Post.objects.all()[:2]
for p in prva_dva:
    print(f"Naslov: {p.title} | Status: {p.status}")

upit = Post.objects.filter(status=Post.Status.PUBLISHED)
print(f"SQL koji Django salje bazi: {upit.query}")

objavljeni = Post.published.all()
print(f"Broj objavljenih postova preko managera: {objavljeni.count()}")

for p in objavljeni:
    print(f"Objavljen: {p.title}")