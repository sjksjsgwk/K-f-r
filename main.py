from telethon import TelegramClient
from telethon.sessions import StringSession
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session = os.getenv("SESSION")

client = TelegramClient(StringSession(session), api_id, api_hash)

mesajlar = ["OROSPU ÇOCUĞU", "PİÇ KURUSU", "AMINA KOYIM", "SİKTİR GİT", "GÖTVEREN", "YAVŞAK", "SİKİK", "KALTAK", "İT OĞLU İT", "ŞEREFSİZ",
    "AQ", "ANANI SİKEYİM", "BABANI SİKEYİM", "KARDEŞİNİ SİKEYİM", "SENİ SİKEYİM", "ÖL LAN", "GEBER", "DEFOL", "BEYİNSİZ", "SALAK",
    "MAL", "GERİZEKALI", "KOYAYIM", "AMCİK", "GÖT", "YARRAK", "TAŞAK", "İBNE", "TOP", "KANCIK",
    "BACINI GÖTÜNDEN SİKİM", "O BABANIN KEL KAFASINA BOŞALIRIM", "O ANANIN AMINA İŞER BABANIN KAFASINI KOPARIRIM", "ANDAVAL OROSPU EVLADI",
    "ATANI YURDUNU SİKEYİM", "AVEL OROSPU EVLADI", "YA SUS ATANI SİKERİM SENİN", "ANANI SİKİM", "OROSPU EVLADI",
    "BABANIN KAFASINA SİKİM", "BABANI GÖTÜNDEN SİKEYİM", "BACINI SİKİM OÇ", "O ANANI GÖTÜNDEN SİKERİM", "ATASINI SİKTİĞİMİN OROSPU EVLADI",
    "O YURDUNU SİKERİM SENİN GAVAT OROSPU EVLADI", "SÜBYANCI PİÇ", "YAŞIT KIZLARDAN YÜZ BULAMAYINCA KÜÇÜK KIZLARA YÖNELEN OROSPU EVLADI",
    "O ANANIN AMINA İŞERİM SENİN BABANIN AĞZINI SİKERİM", "O ANANIN AMINA UÇAN TEKME ATARIM", "AMINA KOYDUĞUMUN ÇOCUĞU",
    "O ANANIN AMINI YERLE BİR EDERİM", "O BACINI GÖTÜNDEN BAŞINDAN SİKERİM BİÇERİM İÇİNDEN GEÇERİM", "ATATÜRKÜNÜ SİKTİĞİMİN ÇOCUĞU",
    "OROSPU EVLADI DAĞLARA TAŞLARA ÇIKAR ANANI MAĞARA İÇİNDE SİKERİM", "ANININ AMINA YARRAĞIMI SAPLADIĞIMIN EVLADI",
    "O ANNENİN DAĞINI TAŞINI TOPRAĞINI GÖZÜNÜ KAŞINI ŞALVARINI SİKERİM", "O BACININ AMINA BİR BAKIŞ ATARIM NAMUSU KAYAR",
    "ANNENİ MAHALLE ARASINDA YAKALAR ANNENİN AMINA PANDİK AÇAR", "EVİNİZE KAÇARIM ORDA BABANIN KAFASINA ŞAPLAĞI VURUP BAYILTIRIM",
    "MURAT GİLİN DAMINDAN ANANIN EVİNE ATLAR ANANA TECAVÜZ EDER", "BABANI BACAKLARINDAN TAVANA ASAR KAFATASINI KESER ÇÖPE ATARIM",
    "SENİN AKLINI SİKEYİM", "KIZ KARDEŞİNİN AMINA KOYAYIM", "ANNENİN GÖTÜNE SOKAYIM", "BABANIN TAŞAKLARINI YİYEYİM", "SÜLALENİ SİKERİM",
    "SOYUN TACİZCİ OROSPU ÇOCUĞU", "SENİ DOĞURANI SİKERİM", "SENİ DOĞURANIN AMINI DAĞITIRIM", "BABANIN GÖTÜNE DİNAMİT KOYARIM",
    "ANNENİN AMINA BENZİN DÖKER YAKARIM", "AĞZINA SIÇAYIM", "GÖTÜNE İŞEYEYİM", "YÜZÜNE TÜKÜRÜRÜM", "SENİ KÖPEK GİBİ GEBERTİRİM",
    "KANINI İÇERİM", "KEMİKLERİNİ KIRARIM", "ETİNİ YERİM", "SENİ PARÇALARIM", "OROSPU DÖLÜ", "PİÇ KURUSUNUN PİÇİ",
    "AMCİK YALAYICI", "GÖT YALAYICI", "SİK YALAYICI", "TAŞAK EMİCİ", "İBNE OĞLU İBNE", "TOP OĞLU TOP", "KANCIK OĞLU KANCIK",
    "ŞEREFSİZİN ŞEREFSİZİ", "HAYSIYETSİZ", "NAMUSSUZ", "ALÇAK", "SOYSUZ", "TERBİYESİZ", "EDEPSİZ", "ARSIZ", "REZİL", "AŞAĞILIK",
    "PİSLİK", "ÇÖPLÜK", "BOK ÇUVALI", "GÖT LALESİ", "AM DUDAKLI", "YARRAK BAŞLI", "TAŞAK SURATLI", "ANNENİN AMINA KAMYON SÜRERİM",
    "BABANIN GÖTÜNE ROKET SOKARIM", "SÜLALENİN AMINI TOPLU SİKERİM", "SENİ ÇÖPE ATARIM", "OROSPU ÇOCUĞUNUN OROSPU ÇOCUĞU",
    "AMINA KOYAYIM SENİN", "GÖTÜNDEN VURAYIM", "YARRAK GİBİ SURAT", "TAŞAK KADAR BEYNİN VAR", "ANNENİ SİKE SİKE BİTİRİRİM",
    "BABANI KÖPEK GİBİ GEZDİRİRİM", "KIZ KARDEŞİNİ SATARIM", "AİLENİ YAKARIM", "EVİNİ BAŞINIZA YIKARIM", "SENİ DİRİ DİRİ GÖMERİM",
    "KEMİKLERİNLE OYNARIM", "KANINI AKITIRIM", "BAĞIRSAKLARINI SÖKERİM", "GÖZLERİNİ OYARIM", "DİLİNİ KESERİM", "KAFANI EZERİM",
    "SENİ FARE GİBİ EZERİM", "OROSPU EVLATLARININ KRALISIN", "PİÇLERİN EFENDİSİ", "AMCİK BEYİNLİ", "GÖT BEYİNLİ", "SİK SURATLI",
    "TAŞAK KAFA", "ANNENİN AMINDAN ÇIKTIĞIN GÜN GEBERSEYDİN", "BABANIN TAŞAKLARINDAN DÜŞSEYDİN", "SENİ DOĞURAN PIŞMAN OLSUN",
    "SENİ DOĞURANIN AMI KURUSUN", "BABANIN GÖTÜ PATLASIN", "SÜLALENİN NAMUSU SIFIR", "SEN NAMUSSUZUN ÖNDE GİDENİSİN",
    "ALÇAK HERİF", "SOYSUZ PİÇ", "TERBİYESİZ OROSPU ÇOCUĞU", "EDEPSİZ YAVŞAK", "ARSIZ KALTAK", "REZİL KÖPEK", "AŞAĞILIK HERİF",
    "PİSLİK YIĞINI", "BOK BÖCEĞİ", "GÖT DELİĞİ", "AM YARIĞI", "YARRAK KILI", "TAŞAK TORBASI", "İBNE PİÇİ", "TOP OĞLAN", "KANCIK PİÇ",
    "ŞEREFSİZ OROSPU", "HAYSIYETSİZ KALTAK", "NAMUSSUZ PİÇKURUSU", "ALÇAK ŞEREFSİZ", "SOYSUZ KALTAK", "TERBİYESİZ PİÇ",
    "EDEPSİZ OROSPU", "ARSIZ YAVŞAK", "REZİL ŞEREFSİZ", "AŞAĞILIK PİÇ", "PİSLİK OROSPU", "ÇÖPLÜK ÇOCUĞU", "BOK TORBASI",
    "GÖTVEREN PİÇ", "AMCİK SURATLI", "YARRAKLI HERİF", "TAŞAKLI KALTAK", "ANNENİN AMINA KOYAYIM", "BABANIN GÖTÜNE KOYAYIM",
    "KIZ KARDEŞİNİN AMINA KOYAYIM", "ERKEK KARDEŞİNİN GÖTÜNE KOYAYIM", "SÜLALENİN HEPSİNE KOYAYIM", "SENİ VE AİLENİ SİKERİM",
    "HEPINİZİ GEBERTİRİM", "HEPINİZİN KANINI DÖKERİM", "HEPINİZİ YAKARIM", "HEPINİZİ PARÇALARIM", "OROSPU ÇOCUKLARI",
    "PİÇLER SÜRÜSÜ", "AMINA KOYDUĞUMUN AİLESİ", "GÖTÜNDEN SİKENLER", "YARRAK YİYENLER", "TAŞAK YALAYANLAR", "İBNE TAYFASI",
    "TOP ÇETESİ", "KANCIK ORDUSU", "ŞEREFSİZLER TOPLULUĞU", "ANNENİN AMINA TANK SÜRERİM", "BABANIN GÖTÜNE FÜZE ATARIM",
    "SÜLALENİ TOPLU MEZARA GÖMERİM", "SENİ TUVALETE DÖKERİM", "OROSPU DÖLÜ PİÇ KURUSU", "AMINA KOYDUĞUMUN PİÇİ",
    "GÖTÜNDEN SİKEN PİÇ", "YARRAK YALAYAN OROSPU", "TAŞAK EMEN KALTAK", "İBNE PİÇ KURUSU", "TOP OĞLU OROSPU", "KANCIK ŞEREFSİZ",
    "NAMUSSUZ KALTAK", "ALÇAK PİÇ", "SOYSUZ OROSPU", "TERBİYESİZ PİÇKURUSU", "EDEPSİZ YAVŞAK", "ARSIZ ŞEREFSİZ", "REZİL KALTAK",
    "AŞAĞILIK OROSPU", "PİSLİK PİÇ", "ÇÖPLÜK OROSPUSU", "BOK YIĞINI", "GÖT DELİĞİ PİÇ", "AM YARIĞI KALTAK", "YARRAK KILI OROSPU",
    "TAŞAK TORBASI PİÇ", "ANNENİN AMINA BETON DÖKERİM", "BABANIN GÖTÜNE ASİT DÖKERİM", "KIZ KARDEŞİNİ KÖPEK GİBİ GEZDİRİRİM",
    "AİLENİ ZİNCİRE VURURUM", "SENİ KAFESE KOYARIM", "KEMİKLERİNİ KIRIP KÖPEK GİBİ GEZDİRİRİM", "KANINI ŞİŞEYE DOLDURURUM",
    "BAĞIRSAKLARINI BOYNUMA DOLARIM", "GÖZLERİNİ CEBİME KOYARIM", "DİLİNİ KESİP DUVARINA ASARIM", "KAFANI TEKMELERİM",
    "SENİ ÇAMAŞIR MAKİNESİNE ATARIM", "OROSPU EVLADI PİÇ KURUSU", "AMCİK SURATLI KALTAK", "GÖT BEYİNLİ ŞEREFSİZ",
    "SİK SURATLI YAVŞAK", "TAŞAK KAFA PİÇ", "ANNENİN AMINA VOLKAN PATLATIRIM", "BABANIN GÖTÜNE NÜKLEER BOMBA SOKARIM",
    "SÜLALENİ TOPLU SİKECEĞİM", "SENİ VE AİLENİ YAKIP KÜL EDERİM", "HEPINİZİN KEMİKLERİNİ ÖĞÜTÜRÜM", "OROSPU ÇOCUKLARININ KRALISIN",
    "PİÇLERİN İMPARATORU", "AMINA KOYDUĞUMUN ŞEREFSİZİ", "GÖTÜNDEN SİKENLERİN EFENDİSİ", "YARRAK YİYENLERİN PADİŞAHI",
    "TAŞAK EMENLERİN SULTANI", "İBNE TAYFASININ KRALI", "OROSPU EVLADI ŞEREFSİZ", "PİÇ KURUSU KALTAK", "AMINA KOYAYIM SENİN PİÇ",
    "GÖTÜNE KOYAYIM OROSPU", "ANNENİN AMINA SOKAYIM", "BABANIN GÖTÜNE SOKAYIM", "SÜLALENİN AMINI DAĞITICAM",
    "SENİN GÖZLERİNİ OYARIM KAFATASINI KÜP YAPARIM", "ANNENİ KÖPEK GİBİ GEZDİRİRİM", "BABANI TUVALET KAĞIDI GİBİ KULLANIRIM",
    "KIZ KARDEŞİNİ PAZARDA SATARIM", "AİLENİ TOPLU KATLİAM YAPARIM", "SENİ DİRİ DİRİ DERİSİNİ YÜZERİM", "KEMİKLERİNİ KÖPEKLERE ATARIM",
    "KANINI ŞARAP GİBİ İÇERİM", "BAĞIRSAKLARINI İP GİBİ ÇEKERİM", "SENİ ASİT HAVUZUNA ATARIM", "EVİNİ BAŞINA YIKAR GÖMERİM"]

running = False
task = None
chat_id = None
reply_id = None
delay = 2

async def loop():
    global running, chat_id, reply_id, delay

    while running:
        msg = random.choice(mesajlar)

        await client.send_message(
            chat_id,
            msg,
            reply_to=reply_id
        )

        print("Gönderildi:", msg)
        await asyncio.sleep(delay)

@client.on(events.NewMessage(pattern=r'\.a'))
async def start(event):
    global running, task, chat_id, reply_id

    if running:
        return await event.reply("Zaten çalışıyor")

    if not event.is_reply:
        return await event.reply("Bir mesaja reply yapıp .a yaz")

    replied = await event.get_reply_message()

    chat_id = event.chat_id
    reply_id = replied.id

    running = True
    task = asyncio.create_task(loop())

    await event.reply("Başlatıldı")

@client.on(events.NewMessage(pattern=r'\.b'))
async def stop(event):
    global running, task

    running = False

    if task:
        task.cancel()
        task = None

    await event.reply("Durduruldu")

@client.on(events.NewMessage(pattern=r'\.hız (\\d+)'))
async def speed(event):
    global delay

    new_delay = int(event.pattern_match.group(1))

    if new_delay < 1:
        return await event.reply("En az 1 saniye olmalı")

    delay = new_delay
    await event.reply(f"Hız: {delay} saniye")

async def main():
    await client.start(phone)
    print("Bot aktif")
    await client.run_until_disconnected()

asyncio.run(main())
