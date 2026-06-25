
const loginForm = document.getElementById("loginForm");

const BASE_URL = "http://localhost:8000";

loginForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    try {

        const response = await fetch(`${BASE_URL}/auth/login`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                email,
                password
            })

        });

        const data = await response.json();

        console.log("Server Response:", data);

        if (response.ok) {

            localStorage.setItem(
                "token",
                data.access_token || data.token
            );

            alert("✨ Login Successful!");

            window.location.href = "dashboard.html";

        } else {

            alert(
                data.detail || "Invalid email or password."
            );

        }

    } catch (error) {

        console.error("Login Error:", error);

        alert("Unable to connect to backend server.");

    }

});