chrome.browserAction.onClicked.addListener(function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        var currentTab = tabs[0];
        var url = currentTab.url;
        var tabId = currentTab.id;
        var regex = /^https:\/\/www\.google\.com\/maps/;
        // if (regex.test(url)) {
            var htmlToInject = "<h1>Ceci est du HTML injecté par l'extension</h1>";
            chrome.tabs.create({ url: "https://www.google.com" });
            chrome.scripting.executeScript(
                {
                    target: { tabId: tabId },
                    function: injectHTML,
                    args: [htmlToInject],
                }
            );
        // }
    });
});

function injectHTML(html) {
    chrome.tabs.create({ url: "https://www.google.com" });
        // }
    var div = document.createElement("div");
    div.innerHTML = html;
    document.body.appendChild(div);

}