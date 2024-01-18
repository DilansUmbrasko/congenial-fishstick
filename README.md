# Steam Akciju mekētājs 

## Projekta pārskats 

Steam Akciju meklētājs , jeb SAM, ir vienkārša Python programma, kas paradzēta, lai automatizētu spēļu akcijas atrašanas procesu. Šīs programmas galvenais mērķis ir nodrošināt lietotājiem vienkāršu un efektīvu veidu, kā iegūt informāciju par spēļu atlaidēm. (Lai arī šobrīd, programma nav pārāk efektīva :D) 

## Projekta uzdevuma apraksts 

Šī projekta uzdevums ir izstrādāt Python skriptu, kas ļauj lietotājiem ievadīt spēles nosaukumu un pēc tam automātiski meklēt šo spēli SteamDB saitē. Pēc tam skriptam vajadzētu iegūt informāciju par spēles akciju, piemēram, pārdošanas cenu un atlaides lielumu. Šī informācija lietotājam ir jāparāda skaidrā un kodolīgā formātā. 

## Izmantotās bibliotēkas un to mērķi 

1. Selenium - Selenium ir šī skripta 'bread and butter', bez tā šeit nekas nenotiku. Šajā uzdevumā Selenium tiek izmantots, lai atvērtu SteamDB saiti, ievadītu spēles nosaukumu meklēšanas lodziņā un pārvietotos meklēšanas rezultātos, lai atrastu akcijas informāciju. 

2. WebDriverWait un expected_conditions -  Tie abi ir no Selenium, un bez tiem mans kods nestrādāja vispār.  Ar to abu palīdzību varēja ieviest gaidīšanu, kas gaidīja līdz brīdim kamēr iestājās noteikti apstākļi.  Šeit tie tiek izmantoti, lai gaidītu, līdz tiek ielādēti meklēšanas rezultāti un informācija par akciju būs pieejama saitē. 

## Nākotnes uzlabojumi 

Šī programma ir diezgan vienkārša un to varētu uzlabot. 

1.Gandrīz vispār nav kļūdu apstrāde. Kods izdrukā "Not found', ja nevar atrast pārdošanas cenu vai akcijas procentus. Noteikti, varētu ieviest labāku sistēmu šeit :D. 

2. Varētu paplašināt informācijas daudzumu, ko skripts izdod par noteikto spēli, piemēram, atsauksmes, vērtējumus, izlaišanas datumus vai piedāvāt kādu citu līdzīgu spēli. 
