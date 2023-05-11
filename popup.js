document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('injectButton').addEventListener('click', function() {
      chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        var currentTab = tabs[0];
        chrome.scripting.executeScript({
          target: { tabId: currentTab.id },
          function: injectDiv
        });
      });
    });
  });

  function injectDiv() {
    var div = document.createElement('div');
    div.innerHTML = 'Contenu de la div';
    var div2 = document.querySelector("#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb");
    if (div2 != null)
        div2.append(div);
    else
        console.log("lalalalala")
    console.log(div2)
    console.log(document.querySelector("#omnibox-directions > div > div:nth-child(2) > div > div > div > div:nth-child(2)"))
  }
