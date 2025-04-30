chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
        id: "checkFakeNews",
        title: "Kiểm tra tin giả",
        contexts: ["selection"] // Chỉ hiện khi bôi đen nội dung
    });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "checkFakeNews") {
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            function: checkFakeNews,
            args: [info.selectionText]
        });
    }
});

function checkFakeNews(selectedText) {
    fetch("http://localhost:5001/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: selectedText })
    })
    .then(response => response.json())
    .then(data => {
        alert(`🔍 Kết quả: ${data.label} (${data.confidence}%)`);
    })
    .catch(error => {
        alert("❌ Lỗi khi kiểm tra tin giả!");
        console.error(error);
    });
}
