chrome.action.onClicked.addListener(function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            var currentTab = tabs[0];
            var url = currentTab.url;
            var regex = /^https:\/\/www\.google\.com\/maps/;
            if (regex.test(url)) {
                chrome.scripting.executeScript({
                    target: { tabId: currentTab.id },
                    function: injectDiv
                });
            }
        });
});
  async function injectDiv() {
    var div = document.querySelector("#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb");
    var divEnfants = div.getElementsByClassName("MespJc");
    for (var i = 0; i < divEnfants.length; i++) {
        var rand = Math.floor(Math.random() * 2000) + 100;
        var divEnfant = divEnfants[i];
        for (var j = 0; j < divEnfant.children.length; j++) {
            var divEnfantEnfant = divEnfant.children[j];
            if (divEnfantEnfant.children.length != 0) {
                var type = getType(div.children[0].querySelectorAll('img')[0]);
                console.log(type);
                console.log("-----------------")
                var dist = 0;
                if (type != 'transport' && type != 'plane')
                    dist = getDistance(divEnfantEnfant.getElementsByClassName('XdKEzd')[0]);
                console.log(dist);
                console.log("-----------------")
                var time = 0;
                if (type == 'plane')
                    time = getTime(divEnfantEnfant.getElementsByClassName('uchGue')[0]);
                else
                    time = getTime(divEnfantEnfant.getElementsByClassName('XdKEzd')[0]);
                console.log(time);
                console.log("-----------------")

                var p1 = document.createElement('p');
                var value = await getFootprint(type, time, dist);
                p1.innerHTML = 'Carbon footprint : ' + value + 'g CO2';
                if (value < 1000)
                    p1.style.color = 'green';
                else if (value < 1500)
                    p1.style.color = 'orange';
                else
                    p1.style.color = 'red';
                divEnfantEnfant.append(p1);
            }
        }
    }

    function getTime(div) {
        console.log(div);
        if (div.children.length == 0)
            return div.innerText;
        return div.children[0].innerText;
    }

    function getDistance(div) {
        console.log(div);
        return div.children[1].innerText;
    }

    function getType(div) {
        var type = div.getAttribute('aria-label')
        if (type == '  En transports  ')
            return 'transport';
        else if (type.includes("pied"))
            return 'walk';
        else if (type.includes("lo"))
            return 'bike';
        else if (type == '  Voiture  ')
            return 'car';
        else if (type == '  En avion  ')
            return 'plane';
        else
            return 'unknown';
    }

  function getFootprint(vehiculeType, travelTime, distance) {
    var knownTypes = ["car", "transit", "bike", "walk", "plane"]
    console.log("le type est: " + vehiculeType + "dans get footprint");
    if (!knownTypes.includes(vehiculeType)) {
        console.log("Error: vehiculeType must be car, transit, bike or foot");
        return "Error";
    }
    return askForFootPrint(vehiculeType, travelTime, distance);
  }


  function askForFootPrint(vehiculeType, travelTime, distance) {
      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");
      console.log("le type est: " + vehiculeType)
      callbacks = {
          "car": ()=>{
              return askFootPrintInCar(distance)
          },
          "transit": ()=>{
              return askForFootPrintInTransit(travelTime) // here the distance parameter represents the time spent in subway
          },
          "bike": ()=>{
              return askForFootPrintInTransit(distance)
          },
          "walk": ()=>{return 0}
      }

      return callbacks[vehiculeType]();
  }


  async function askFootPrintInCar(distance) {
      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");

      var raw = JSON.stringify({
      "km": distance.toString(),
      "type_v": 2
      });

      var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
      };

      var res = await fetch("http://127.0.0.1:5000/get_CarBone", requestOptions)
      .then(response => response.text())
      .then(result => {return result})
      .catch(error => console.log('error', error));
      console.log("ewen " + res);
      return parseInt(res);
  }

  function askForFootPrintInTransit(distance) {
      // src for the numbers: http://interconnect.one/news-press/news/141-the-concept-of-public-transport-and-its-quality
      var raw = JSON.stringify({
          "km_bus": (distance / 55.7).toString(),
          "type_v": "",
          "km_coach": "",
          "km_rail": "",
          "km_int_rail": (distance / 13.60).toString(),
          "km_tram": (distance / 14.50).toString(),
          "km_sub": (distance / 16.2).toString(),
          "km_taxi": ""
      });

      var requestOptions = {
          method: 'POST',
          headers: myHeaders,
          body: raw,
          redirect: 'follow'
      };

      var res = undefined;
      fetch("http://127.0.0.1:5000/get_commonT_foot", requestOptions)
      .then(response => response.text())
      .then(result => res = result)
      .catch(error => console.log('error', error));
      console.log("die kindern " + res);
      return parseInt(res);
  }
}
