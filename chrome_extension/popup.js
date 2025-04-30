document.getElementById("checkNews").addEventListener("click", async () => {
    let text = document.getElementById("newsText").value;

    if (!text.trim()) {
        alert("Vui lòng nhập nội dung bài báo!");
        return;
    }

    let response = await fetch("http://localhost:5001/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });

    let data = await response.json();
    document.getElementById("result").innerText = `Kết quả: ${data.label} (${data.confidence}%)`;
});
