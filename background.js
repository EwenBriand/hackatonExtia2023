// chrome.browserAction.onClicked.addListener(function() {
//     chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//         var currentTab = tabs[0];
//         var url = currentTab.url;
//         var tabId = currentTab.id;
//         var regex = /^https:\/\/www\.google\.com\/maps/;
//         // if (regex.test(url)) {
//             var htmlToInject = "<h1>Ceci est du HTML injecté par l'extension</h1>";
//             // chrome.tabs.create({ url: "https://www.google.com" });
//             chrome
//             chrome.tabs.executeScript(tabId, { code: "var div = document.createElement('div'); div.innerHTML = '" + htmlToInject + "'; document.body.appendChild(div);" });

//         // }
//     });
//     chrome.tabs.executeScript(tab.id, { code: "var div = document.createElement('div'); div.textContent = 'Contenu de la div'; document.body.appendChild(div);" });

// });
chrome.browserAction.onClicked.addListener(function(tab) {
    chrome.tabs.executeScript(tab.id, { code: "var div = document.createElement('div'); div.textContent = 'Contenu de la div'; document.body.appendChild(div);" });
  });
// function injectHTML(html) {
//     chrome.tabs.create({ url: "https://www.google.com" });
//         // }
//     var div = document.createElement("div");
//     div.innerHTML = html;
//     document.body.appendChild(div);

// }