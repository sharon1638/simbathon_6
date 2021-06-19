from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('index/', index, name="index"),
    path('left_sidebar/',left_sidebar, name="left_sidebar"),
    path('no_sidebar/', no_sidebar, name="no_sidebar"),
    path('right_sidebar/', right_sidebar, name="right_sidebar"),
    path('극예술연구회/',극예술연구회,name="극예술연구회"),
    path('로터스/',로터스,name="로터스"),
    path('뭉게구름/',뭉게구름,name="뭉게구름"),
    path('아리랑/',아리랑,name="아리랑"),
    path('음샘/',음샘,name="음샘"),
    path('피어리스던/',피어리스던,name="피어리스던"),
    path('현여울/',현여울,name="현여울"),
    path('AJAX/',AJAX,name="AJAX"),
    path('HOLA/',HOLA,name="HOLA"),
    path('ODC/',ODC,name="ODC"),
    path('OPUS/',OPUS,name="OPUS"),
    path('길/',길,name="길"),
    path('손짓사랑회/',손짓사랑회,name="손짓사랑회"),
    path('젊은새이웃/',젊은새이웃,name="젊은새이웃"),
    path('페인터즈/',페인터즈,name="페인터즈"),
    path('푸름누리/',푸름누리,name="푸름누리"),
    path('한글학교하람/',한글학교하람,name="한글학교하람"),
    path('ELF/',ELF,name="ELF"),
    path('RCY/',RCY,name="RCY"),
    path('동국불교학생회/',동국불교학생회,name="동국불교학생회"),
    path('프론티어/',프론티어,name="프론티어"),
    path('KUSA/',KUSA,name="KUSA"),
    path('RICH/',RICH,name="RICH"),
    path('UNSA/',UNSA,name="UNSA"),
    path('두둠칫/',두둠칫,name="두둠칫"),
    path('멋쟁이사자처럼/',멋쟁이사자처럼,name="멋쟁이사자처럼"),
    path('인액터스/',인액터스,name="인액터스"),
    path('잼잼/',잼잼,name="잼잼"),
    path('FC엘레펜테/',FC엘레펜테,name="FC엘레펜테"),
    path('QUD/',QUD,name="QUD"),
    path('경영학연구회/',경영학연구회,name="경영학연구회"),
    path('경제학연구회/',경제학연구회,name="경제학연구회"),
    path('국제통상연구회/',국제통상연구회,name="국제통상연구회"),
    path('정치학연구회/',정치학연구회,name="정치학연구회"),
    path('그리고그림/',그리고그림,name="그리고그림"),
    path('동국문학회/',동국문학회,name="동국문학회"),
    path('동국서도회/',동국서도회,name="동국서도회"),
    path('동그라미/',동그라미,name="동그라미"),
    path('디딤돌/',디딤돌,name="디딤돌"),
    path('만화얼/',만화얼,name="만화얼"),
    path('애드러쉬/',애드러쉬,name="애드러쉬"),
    path('기우회/',기우회,name="기우회"),
    path('명궁/',명궁,name="명궁"),
    path('선무부/',선무부,name="선무부"),
    path('터스커스/',터스커스,name="터스커스"),
    path('COURTIST/',COURTIST,name="COURTIST"),
    path('DUTC/',DUTC,name="DUTC"),
    path('FC_TOTO/',FC_TOTO,name="FC_TOTO"),
    path('LAE/',LAE,name="LAE"),
    path('동국탐험연구회',동국탐험연구회,name="동국탐험연구회"),
    path('무법/',무법,name="무법"),
    path('바람소리/',바람소리,name="바람소리"),
    path('산악부/',산악부,name="산악부"),
    path('수중탐구연구회/',수중탐구연구회,name="수중탐구연구회"),
    path('DUST/',DUST,name="DUST"),
    path('맑스철학연구회/',맑스철학연구회,name="맑스철학연구회"),
    path('CAFE_IN/',CAFE_IN,name="CAFE_IN"),
    path('DNA/',DNA,name="DNA"),
    path('DUSSA/',DUSSA,name="DUSSA"),
    path('KCC/',KCC,name="KCC"),
    path('MECS/',MECS,name="MECS"),
    path('NSA/',NSA,name="NSA"),
]