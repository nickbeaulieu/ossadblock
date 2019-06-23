console.info("Loading blocker...");
var enabled = true;
chrome.webRequest.onBeforeRequest.addListener((requestDetails) => {
    console.log("Blocking ", requestDetails.url);
    console.log("Blocking ", requestDetails);

    return {cancel: enabled};  
},
{urls: blocked},
["blocking"]);