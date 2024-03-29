from parsing_songs_ids import response

import requests

from dotenv import load_dotenv
import os

load_dotenv()


def get_track(ids: str):
    cookies = os.environ.get('COOKIES_FOR_NAME')

    headers = {
        'authority': 'music.yandex.ru',
        'accept': 'application/json; q=1.0, text/*; q=0.8, */*; q=0.1',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': "yandexuid=2369877731701969965; yashr=1915673991701969965; yuidss=2369877731701969965; ymex=2017329966.yrts.1701969966; gdpr=0; _ym_uid=1701969966319056867; _ym_d=1701969966; skid=8873773191701977632; my=YwA=; L=XztZaURGQEZIBAEJTQFUXlpgX3JEbVNbOzw4MB47AzUTJlMjBA==.1703093755.15562.335486.f53ee06aa20f63d8fa72235a542226ae; yandex_login=sumuraaaaaaaa; chromecast=''; device_id=a02d65ab26ea92e67d6baa94fcb92f3f33a066241; font_loaded=YSv1; amcuid=1608681111704635766; is_gdpr=0; is_gdpr_b=CKT6WBC75QEoAg==; yabs-vdrf=FVwvbDW1w6LK0hvfbBW3ems016Ozbd00iGrW0qdrbDW1QGm00l7PbG01wTd410; fullscreen-saved-data=%7B%22no_option_booktillyear-1%22%3A%7B%22compositeId%22%3A%22no_option_booktillyear-1%22%2C%22actualUntil%22%3A1734716160261%7D%2C%22my_wave_unfamiliar-31%22%3A%7B%22compositeId%22%3A%22my_wave_unfamiliar-31%22%2C%22actualUntil%22%3A1740149960226%7D%7D; bh=EjsiTm90X0EgQnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjEyMCIsICJPcGVyYSBHWCI7dj0iMTA2IhoFIng4NiIiDyIxMDYuMC40OTk4Ljc2IioCPzA6CSJXaW5kb3dzIkIIIjE1LjAuMCJKBCI2NCJSVSJOb3RfQSBCcmFuZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMjAuMC42MDk5LjIxNyIsIk9wZXJhIEdYIjt2PSIxMDYuMC40OTk4Ljc2IiI=; Session_id=3:1708861968.5.0.1703093755945:oWyekg:26.1.2:1|1623232884.-1.2.3:1703093755|3:10283625.236836.9wGIqdzh3h-SKQ_ksE0tthDTzvc; sessar=1.1187.CiBKumEastoMTcMPCOi0pn5T2k7LTerfqh2Q7ZfFg5CvoA.3RO304-G3H9xnLXRiMYAbzgZueZTkxJG4Wy-c_AdjQ8; sessionid2=3:1708861968.5.0.1703093755945:oWyekg:26.1.2:1|1623232884.-1.2.3:1703093755|3:10283625.236836.fakesign0000000000000000000; i=yoVZBe47+UocSOHvoqDY6jw8CHm0MWSRGZJHVOu/PywLSp6TvYnunFABU90PBdicvYLF6is5HEdSVeS//xzMYNoVmSw=; _ym_isad=2; cycada=sfPmACbliUiBqNXBPl9AKaHNXt2UGJ6wypCIb37Vxo8=; _yasc=cLBtWFqkowkwg+61jEE5nsRMJSJ4cv3s9SzwhtgSW3n9LtOWdf3jFB1Y+ADLmKcg+66SG2ndajT01IMig2FuwiE=; bh=EjkiTm90X0EgQnJhbmQiO3Y9IjgiLCJDaHJvbWl1bSI7dj0iMTIwIiwiT3BlcmEgR1giO3Y9IjEwNiIaBSJ4ODYiIg8iMTA2LjAuNDk5OC43NiIqAj8wOgkiV2luZG93cyJCCCIxNS4wLjAiSgQiNjQiUlUiTm90X0EgQnJhbmQiO3Y9IjguMC4wLjAiLCJDaHJvbWl1bSI7dj0iMTIwLjAuNjA5OS4yMTciLCJPcGVyYSBHWCI7dj0iMTA2LjAuNDk5OC43NiIi; lastVisitedPage=%7B%221623232884%22%3A%22%2Fusers%2Fsumuraaaaaaaa%2Fplaylists%22%7D; _ym_visorc=b; ys=udn.cDpzdW11cmFhYWFhYWFh#wprid.1708866985893152-15630571235061745986-balancer-l7leveler-kubr-yp-vla-233-BAL#c_chck.921842685; yp=2024226982.pcs.1#1718323404.szm.1_5%3A1280x800%3A1225x664#1711540369.hdrc.0#1735059174.p_sw.1703523173#1712946606.v_sum_b_onb.4%3A1705170605520#1734940170.p_undefined.1703404170#2018453755.udn.cDpzdW11cmFhYWFhYWFh#1711299248.v_smr_onb.t%3D1%3A1703523247674#1737035289.stltp.serp_bk-map_1_1705499289; active-browser-timestamp=1708867170526",
        'referer': 'https://music.yandex.ru/users/sumuraaaaaaaa/playlists',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0',
        'x-current-uid': '1623232884',
        'x-requested-with': 'XMLHttpRequest',
        'x-retpath-y': 'https%3A%2F%2Fmusic.yandex.ru%2Fusers%2Fsumuraaaaaaaa%2Fplaylists',
        'x-yandex-music-client': 'YandexMusicAPI',
        'x-yandex-music-client-now': '2024-02-25T17:19:31+04:00',
    }

    params = {
        'tracks': ids,
        'withProgress': 'true',
        'external-domain': 'music.yandex.ru',
        'overembed': 'no',
        '__t': '1708867171618',
    }

    return requests.get('https://music.yandex.ru/api/v2.1/handlers/tracks', params=params, cookies=cookies,
                             headers=headers)


def get_name():
    songs = []
    track_ids = response.json()['trackIds']
    for i in range(0, len(track_ids), 50):
        response1 = get_track(','.join(track_ids[i:i+50]))
        for track in response1.json():
            try:
                name_song = track.get('title')
                name_artist = track.get('artists')[0].get('name')
                songs.append((name_song, name_artist))
            except:
                print('unknown')

    return songs


songs = get_name()
print(songs)

with open('../utils/songs.txt', 'w', encoding='UTF-8') as file:
    for song in songs:
        file.write(f'{song[0]} - {song[1]}\n')