## 📋 Uppgifter

| # | Uppgift   | Beskrivning                                                      | Status |
|---|-----------|------------------------------------------------------------------|--------|
| 1 | Uppgift:1 | [Diskutera tillsammans](#1-diskutera-tillsammans)                | 🟢 Klar |
| 2 | Uppgift:2 | [Prestandatest: insertion sort](#2-prestandatest-insertion-sort) | 🟡 Pågår |
| 3 | Uppgift:3 | Prestandatest: merge sort                                        | 🔴 Ej påbörjad |
### Status
- 🟢 **Klart**
- 🟡 **Halvvägs klar**
- 🔴 **Ej påbörjad**



# 1 Diskutera tillsammans
Frågorna utgår från innehållet i presentationen.

1. Vad är en regression? När inträffar de oftast under ett projekts livstid?
2. Vad är skillnaden mellan enhetstest och regressionstest?
3. Vad är en feature? Hur förhåller det sig till kraven?
4. Varför kan man inte veta exakt hur lång tid det kommer ta att köra kod?
5. Varför skriver man till exempel O(n) men inte O(2*n + 10) ?
---

1. Regression är något som konstant sker under utvecklingens gång. Så fort något i projektet blivit fixat så bör man som utvecklare eller testar ha koll på vad för saker som kan ha blivit påverkade och kanske inte längre fungerar som behöver testas igen, alternativt tidigare funna buggar som fixats som kan eller har koppling till en ny ändring i koden bör kollar igen för att se att ingen tidigare bug återkommit.
---
2. Enhetstest är test som fokuserar på specifika funktioner i ett slutet system där de ej påverkar eller jobbar men andra system eller moduler. Regressionstest är dock testning där man återblickar så att inte ens tidigare funktion slutat fungera eller att en tidigare fixat bug återkommit med nya kodförändringar.
---
3. En feature är en funktion som ger användaren någon möjlighet eller nytta. Hur en feature förhåller sig till kraven skrivs i krav och acceptanskriterier. Tex, om jag har en feature som säger att jag skall kunna lägga varor i korgen. I detta skall de finnas flera krav så som, rätt antal varor syns i korgen, de varor som lagts i korgen skall ligga kvar i korgen, användaren skall kunna plocka ur varor i korgen.När alla krav är uppfyllda kan vi anse featuren som klar.
---
4. När man kör tester finns det många faktorer som påverkar dess tid. Först har vi hårdvara, vi alla har oftast olika hårdvaror så som CPU,GPU,Ram och nätverk, dessa påverkar hur snabbt eller långsamt ett test körs. Vi har även bakrundsappar, en person som kör fler appar i bakrunden kan uppleva att testerna körs långsammare än en person som har färre appar igång. Uppdaterade drivrutiner kan även vara en faktor då dessa kan påverka hur effektivt en hårdvara eller app arbetar.
---
5.  n står för mängden data och ju mer n ökar desto mer tid kommer ta kräva av programmet och desto längre tid kommer det att ta. Big O beskriver hur arbetet växer när n växer. Har vi då O(2*n 10) kommer mängden data öka betydligt mer än om O(n) efter vi då får tex om n = 10 (2*10 + 10) och detta kommer bli betydligen större ju mer n ökar.

---


# 2 Prestandatest: insertion sort