const form = document.getElementById("contact-form-form");

form.addEventListener("submit", async function payload(event) {
    event.preventDefault();

    const formData = {
        name: document.getElementById("name").value,
        mobile: document.getElementById("mobile-number").value,
        email: document.getElementById("email").value,
        reason: document.getElementById("reason").value,
        comment: document.getElementById("discussing").value
    };

    try {
        const apiUrl = "http://127.0.0" + ".1:8000/api/contact";
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById("statusMessage").innerText = "Message sent! ID: " + result.id;
            form.reset();
        } else {
            document.getElementById("statusMessage").innerText = "Error: " + JSON.stringify(result.detail);
        }
    } catch (error) {
        document.getElementById("statusMessage").innerText = "Could not connect to server.";
    }
});
