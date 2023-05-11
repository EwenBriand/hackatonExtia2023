var staticvar = false;

// chrome.webNavigation.onCommitted.addListener((details) => {

function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}


chrome.webNavigation.onCompleted.addListener(function onComplete() {
    chrome.tabs.onUpdated.addListener(function() {;
        console.log("updated");
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            var currentTab = tabs[0];
            var url = currentTab.url;
            var regex = /^https:\/\/www\.google\.com\/maps/;
            if (regex.test(url)) {
                chrome.scripting.executeScript({
                    target: { tabId: currentTab.id },
                    function: injectDiv
                });

                // chrome.tabs.executeAsyncFunction(
                //     currentTab.id,
                //     async () => {
                //         await injectDiv();
                //     }
                // )
            }
        });
    chrome.webNavigation.onCompleted.removeListener(onComplete);
});
    });

// chrome.tabs.onUpdated.addListener(function() {
//     chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//             var currentTab = tabs[0];
//             var url = currentTab.url;
//             var regex = /^https:\/\/www\.google\.com\/maps/;
//             if (regex.test(url)) {
//                 chrome.scripting.executeScript({
//                     target: { tabId: currentTab.id },
//                     function: injectDiv
//                 });
//             }
//         });
//     });
    // async function injectDiv() {
    async function injectDiv() {
    var div = document.querySelector("#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb");
    var divEnfants = div.getElementsByClassName("MespJc");
    for (var i = 0; i < divEnfants.length; i++) {
        var rand = Math.floor(Math.random() * 2000) + 100;
        var divEnfant = divEnfants[i];
        for (var j = 0; j < divEnfant.children.length; j++) {
            var divEnfantEnfant = divEnfant.children[j];
            if (divEnfantEnfant.children.length != 0) {
                // console.log(divEnfantEnfant.innerHTML);
                var type = getType(div.children[0].querySelectorAll('img')[0]);
                var dist = 0;
                if (type != 'transit' && type != 'plane')
                    dist = getDistance(divEnfantEnfant.getElementsByClassName('XdKEzd')[0]);
                var time = 0;
                if (type == 'plane')
                    time = getTime(divEnfantEnfant.getElementsByClassName('uchGue')[0]);
                else
                    time = getTime(divEnfantEnfant.getElementsByClassName('XdKEzd')[0]);

                try {
                    var value = await getFootprint(type, time, dist);
                    console.log("value" + value);
                      let info = document.getElementsByClassName('p_carbon_ext' + i.toString());
                    if (info.length == 0) {
                        var p1 = document.createElement('p_carbon_ext' + i.toString());
                        p1.className = 'p_carbon_ext' + i.toString();
                            p1.innerHTML = 'Carbon footprint : ' + value + 'g CO2';
                            if (value < 1000)
                                p1.style.color = 'green';
                            else if (value < 1500)
                                p1.style.color = 'orange';
                            else
                                p1.style.color = 'red';
                            divEnfantEnfant.append(p1);
                    }
                } catch (error) {
                }
            }
        }
    }

    function getTime(div) {
        if (div.children.length == 0)
            return div.innerText;
        return div.children[0].innerText;
    }

    function getDistance(div) {
        return div.children[1].innerText;
    }

    function getType(div) {
        var type = div.getAttribute('aria-label')
        if (type == '  En transports  ')
            return 'transit';
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
    console.log("in get footprint");
    var knownTypes = ["car", "transit", "bike", "walk", "plane"]
    if (!knownTypes.includes(vehiculeType)) {
        console.log("Error: vehiculeType must be car, transit, bike or foot");
        return "Error";
    }
    return askForFootPrint(vehiculeType, travelTime, distance);
  }


  function askForFootPrint(vehiculeType, travelTime, distance) {
      var myHeaders = new Headers();
      console.log("in getFootprint")
      myHeaders.append("Content-Type", "application/json");
      callbacks = {
          "car": ()=>{
              return askFootPrintInCar(distance)
          },
          "transit": ()=>{
            console.log("in transit");
            var val = askForFootPrintInTransit(travelTime) // here the distance parameter represents the time spent in subway
            console.log("val SDMLFJSQMDLKFJQSLMDKJF");
            return val;
          },
          "bike": ()=>{
                console.log("in bike");
              return 0;
          },
          "walk": ()=>{
                console.log("in walk");
                return 0;
          }
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
      return parseInt(res);
  }

  function askForFootPrintInTransit(distance) {
      // src for the numbers: http://interconnect.one/news-press/news/141-the-concept-of-public-transit-and-its-quality
      var raw = JSON.stringify({
          "km_bus": (distance / 55.7),
          "km_coach": "",
          "km_rail": "",
          "km_int_rail": (distance / 13.60),
          "km_tram": (distance / 14.50),
          "km_sub": (distance / 16.2),
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
      return parseInt(res);
  }
}
