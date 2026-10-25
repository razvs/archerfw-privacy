# ArcherFW adatvédelmi oldal — szerkeszthető sablon

2026-10-25. **Nem végleges, nem jogi megfelelőségi tanúsítvány.** A felhasználó kérésére az adatkezelő neve, kapcsolata és a kiadási név sablon; a közönség általános, nem kifejezetten gyermekeknek szánt. Ez a változat nem lett publikálva, és nincs a Unity provider éles privacy URL-jeként beállítva.

## Szerkesztés és feltöltés

- Tartalom: `content.json` — magyar/angol/német, egy helyen szerkeszthető. `build.py` a Python alapkönyvtárával legenerálja a `dist/` fájljait. Nincs csomagtelepítés vagy külső függőség.
- Stílus: `dist/assets/privacy.css`. A feliratok HTML-szövegek, nem képek. Nincs JavaScript, űrlap, saját tracker, analitika, külső font vagy kép.
- Futtatás: `python build.py`, majd előnézethez `python -m http.server 8088 --bind 127.0.0.1 --directory dist`. Közvetlenül az `index.html` is megnyitható.
- Feltöltéskor **csak a `dist/` tartalma** szükséges. A játék forrását, mentéseket, titkokat vagy privát repositoryt nem kell publikálni.
- HU: `/`, EN: `/en/`, DE: `/de/`. Minden nyelvválasztó statikus hivatkozás. Az oldal kis képernyőn is olvasható, nyomtatási stílussal és billentyűzetes navigációval.
- `robots.txt` és a HTML `noindex` címkéje a tervezet keresőindexelését ellenzi, **nem hozzáférésvédelem**. `_headers` opcionális Cloudflare-válaszfejléceket ad; más statikus hoston nem végrehajtható kód, a megfelelő hostbeállítást kell használni.

## Ingyenes tárhely saját szerver nélkül

**Elsődleges javaslat: Cloudflare Pages statikus Direct Upload.** A szolgáltató jelenlegi dokumentációja szerint a statikus fájlkérések ingyenesek és nem igényelnek Functions-futtatást. Feltölthető a `dist/` mappa vagy az azt tartalmazó ZIP; a szolgáltató `pages.dev` címet ad. Ne válassz fizetős csomagot, domaint, Worker/Functions-adatbázist vagy opcionális fizetős szolgáltatást ehhez az oldalhoz. A webanalitika maradjon kikapcsolva. A regisztráció/feltételek elfogadása és a végleges nyilvános közzététel a fióktulajdonos, illetve a fő feladat gazdájának munkafolyamata.

**Alternatíva: GitHub Pages**, egy kizárólag a nyilvános tájékoztató fájljait tartalmazó külön public repóból, ha az ingyenes csomag ezt támogatja. A meglévő privát játék- vagy buildrepó láthatóságát nem kell és nem szabad emiatt megváltoztatni. Ez nem játékbackend és nem adminhosting.

Unity Cloudra is tölthetők fájlok: a **CCD** tartalomkézbesítésre való. A Cloud Save Player Files személyes mentéshez kötött, nem nyilvános privacy-weboldal. CCD választásakor a stabil nyilvános URL-t, HTML `Content-Type`-ot, letöltés helyetti böngészős megjelenítést és költségkeretet külön ellenőrizni kell; ezt a sablont nem teszteltük CCD-n. Egy ilyen kis dokumentumhoz a Pages egyszerűbb.

## Közzététel előtt kitöltendő

1. Valódi kiadási név, adatkezelő neve, nyilvános e-mail és megfelelő levelezési elérhetőség.
2. Tényleges adatkezelésenkénti jogalap; ahol szükséges, érdekmérlegelés vagy valódi hozzájárulási folyamat. A tájékoztató olvasása nem általános hozzájárulás.
3. Valós megőrzési/törlési rend, napló- és backupkezelés. A sablon nem ígér nem implementált törlési határidőt.
4. Hostszolgáltató, szerződések és nemzetközi adattovábbítás garanciái.
5. A ténylegesen elkészült és kiadott cloud save/restore, jóváírások, esetleges reklám/analitika/IAP működésének pontos leírása. A jelenlegi szöveg kifejezetten nem állítja késznek az összes játékadat felhőbe írását.
6. Működő játékadat-/fióktörlési út, áruházi követelmények szerinti in-app lehetőség; külön a több játékban használt Unity Player Account törlésétől. Jelszót, tokeneket vagy bankkártyaadatot nem kérünk a supportkéréshez.
7. Hatálybalépés és utolsó frissítés, végleges nyelvek ellenőrzése; a draft/noindex jelölések felülvizsgálata.
8. Nyilvános, bejelentkezés nélkül elérhető, stabil HTTPS URL. Ellenőrzött URL bekötése a Unity providerhez, a játékhoz és az áruházhoz; a sablon URL-je nem helyettesít végleges, valós tájékoztatót.

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
