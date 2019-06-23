window.onload = function() {
    function updatePopup() {
        const enabled = chrome.extension.getBackgroundPage().enabled;
        console.log(enabled);
        document.getElementById("enable_toggle").value = enabled ? "Disable" : "Enable";
    }
    document.getElementById('enable_toggle').onclick = () => {
        const bg = chrome.extension.getBackgroundPage();
        bg.enabled = !bg.enabled;
        updatePopup();
    }
    // Update popup one time on first load
    updatePopup();
}