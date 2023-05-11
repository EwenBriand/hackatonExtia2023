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
  function injectDiv() {
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
                p1.innerHTML = 'Carbon footprint : ' + rand + 'g CO2';
                if (rand < 1000)
                    p1.style.color = 'green';
                else if (rand < 1500)
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
  }
