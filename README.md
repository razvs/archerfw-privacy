# ArcherFW adatvédelmi oldal — szerkeszthető sablon

2026-10-25. **Nem végleges, nem jogi megfelelőségi tanúsítvány.** A felhasználó kérésére az adatkezelő neve, kapcsolata és a kiadási név sablon; a közönség általános, nem kifejezetten gyermekeknek szánt. A szerkeszthető tervezet publikálva: https://razvs.github.io/archerfw-privacy/ ; a Unity Player Accounts provider és a játék adatvédelmi hivatkozása ezt használja. Ez még nem végleges jogi tájékoztató.

## Szerkesztés és feltöltés

- Tartalom: `content.json` — magyar/angol/német, egy helyen szerkeszthető. `build.py` a Python alapkönyvtárával legenerálja a `dist/` fájljait. Nincs csomagtelepítés vagy külső függőség.
- Stílus: `dist/assets/privacy.css`. A feliratok HTML-szövegek, nem képek. Nincs JavaScript, űrlap, saját tracker, analitika, külső font vagy kép.
- Futtatás: `python build.py`, majd előnézethez `python -m http.server 8088 --bind 127.0.0.1 --directory dist`. Közvetlenül az `index.html` is megnyitható.
- Feltöltéskor **csak a `dist/` tartalma** szükséges. A játék forrását, mentéseket, titkokat vagy privát repositoryt nem kell publikálni.
- HU: `/`, EN: `/en/`, DE: `/de/`. Minden nyelvválasztó statikus hivatkozás. Az oldal kis képernyőn is olvasható, nyomtatási stílussal és billentyűzetes navigációval.
- `robots.txt` és a HTML `noindex` címkéje a tervezet keresőindexelését ellenzi, **nem hozzáférésvédelem**. `_headers` opcionális Cloudflare-válaszfejléceket ad; más statikus hoston nem végrehajtható kód, a megfelelő hostbeállítást kell használni.

## Ingyenes tárhely saját szerver nélkül

**Használt megoldás: GitHub Pages**, külön, kizárólag nyilvános dokumentumokat tartalmazó `razvs/archerfw-privacy` repositoryból. A Pages forrása `main /docs`, HTTPS. A privát Unity projekt láthatósága nem változott. Nincs saját szerver, vásárolt domain vagy fizetős tárhely.

Frissítés: szerkeszd a `content.json` fájlt, futtasd a `python build.py` parancsot, és a `dist/` tartalmát másold a nyilvános dokumentumtár `docs/` mappájába. A dokumentumtár gyökerében a `content.json`, `build.py` és ez a README is megtalálható; a generátor ott is `dist/` kimenetet készít. A módosítások commitja után a Pages automatikusan kiadja a weboldalt. Csak a dokumentumfájlokat töltsd fel, soha ne a játékprojektet, mentést vagy hozzáférési kulcsot.

Alternatíva későbbi költözéshez a statikus Cloudflare Pages Direct Upload. Nem lett Cloudflare-előfizetés vagy külön fiók létrehozva.

Unity Cloudra is tölthetők fájlok: a **CCD** tartalomkézbesítésre való. A Cloud Save Player Files személyes mentéshez kötött, nem nyilvános privacy-weboldal. CCD választásakor a stabil nyilvános URL-t, HTML `Content-Type`-ot, letöltés helyetti böngészős megjelenítést és költségkeretet külön ellenőrizni kell; ezt a sablont nem teszteltük CCD-n. Egy ilyen kis dokumentumhoz a Pages egyszerűbb.

## Közzététel előtt kitöltendő

1. Valódi kiadási név, adatkezelő neve, nyilvános e-mail és megfelelő levelezési elérhetőség.
2. Tényleges adatkezelésenkénti jogalap; ahol szükséges, érdekmérlegelés vagy valódi hozzájárulási folyamat. A tájékoztató olvasása nem általános hozzájárulás.
3. Valós megőrzési/törlési rend, napló- és backupkezelés. A sablon nem ígér nem implementált törlési határidőt.
4. Hostszolgáltató, szerződések és nemzetközi adattovábbítás garanciái.
5. A ténylegesen elkészült és kiadott cloud save/restore, jóváírások, esetleges reklám/analitika/IAP működésének pontos leírása. A jelenlegi szöveg a stagingben ellenőrzött teljes profilmentést írja le, és külön jelzi, hogy ez nem egy korábbi telefonos verzió állapota.
6. Működő játékadat-/fióktörlési út, áruházi követelmények szerinti in-app lehetőség; külön a több játékban használt Unity Player Account törlésétől. Jelszót, tokeneket vagy bankkártyaadatot nem kérünk a supportkéréshez.
7. Hatálybalépés és utolsó frissítés, végleges nyelvek ellenőrzése; a draft/noindex jelölések felülvizsgálata.
8. Nyilvános, bejelentkezés nélkül elérhető, stabil HTTPS URL. A providerhez és játékhoz már bekötött URL véglegesítése, majd az áruházi adatlaphoz megadása; a sablon URL-je nem helyettesít végleges, valós tájékoztatót.

## Források (ellenőrizve 2026-10-25)

- [Unity Authentication privacy](https://docs.unity.com/en-us/authentication/privacy-and-consent/overview)
- [Unity Cloud Save privacy](https://docs.unity.com/en-us/cloud-save/privacy-and-consent/overview)
- [Unity Player Accounts privacy és külön fióktörlés](https://docs.unity.com/en-us/authentication/privacy-and-consent/data-privacy-unity-player-accounts)
- [Unity Cloud Save Files hozzáférési célja](https://docs.unity.com/en-us/cloud-save/concepts/files)
- [Unity CCD](https://docs.unity.com/en-us/ccd)
- [Cloudflare Pages Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/)
- [Cloudflare statikus fájlok díjazása](https://developers.cloudflare.com/pages/functions/pricing/)
- [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)
- [Apple 5.1.1](https://developer.apple.com/app-store/review/guidelines/#privacy)
- [Google Play adatvédelmi követelmények](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en)
- [GDPR, különösen 12–14. cikk](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

A szolgáltatások használati keretei később változhatnak; itt nincs fizetős tárhely vagy előfizetés létrehozva. A publikálást és a kiadási/készülékes ellenőrzést a fő feladat külön követi.
