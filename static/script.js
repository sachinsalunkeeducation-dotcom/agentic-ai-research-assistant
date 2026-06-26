async function generateReport() {

    let query = document.getElementById("query").value;

    document.getElementById("report").innerHTML = "";
    document.getElementById("status").innerHTML = "Starting Workflow...";

    // Poll status every second
    let statusInterval = setInterval(async () => {

        let response = await fetch("/status");

        let data = await response.json();

        document.getElementById("status").innerHTML =
            data.messages.join("<br>");

    }, 1000);

    // Start report generation
    let response = await fetch("/generate-report", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            query: query
        })

    });

    // Stop polling
    clearInterval(statusInterval);

    let data = await response.json();

    document.getElementById("status").innerHTML +=
        "<br><br>✅ Workflow Completed";

    document.getElementById("report").innerHTML =
        data.report;

}