const loginBtn = document.getElementById("loginBtn");

loginBtn.addEventListener("click", async (e) => {

    e.preventDefault();

    const email =
        document.getElementById("email").value;

    const password =
        document.getElementById("password").value;
const loginBtn = document.getElementById("loginBtn");

const BASE_URL = "http://localhost:8000";

loginBtn.addEventListener("click", async (e) => {

    e.preventDefault();

    const email =
        document.getElementById("email").value;

    const password =
        document.getElementById("password").value;

    try {

        const response = await fetch(
            `${BASE_URL}/auth/login`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email,
                    password
                })
            }
        );

        const data = await response.json();

        if(response.ok){

            console.log("Login Successful", data);

            // safer token handling
            localStorage.setItem(
                "token",
                data.access_token || data.token
            );

            window.location.href =
                "dashboard.html";

        } else {

            console.log("Login failed:", data);

            alert(
                data.detail || "Invalid email or password"
            );

        }

    } catch(error){

        console.error("Server error:", error);

        alert("Server connection failed");
    }

});
    try {
s̱
        const response = await fetch(
            "http://localhost:8000/auth/login",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    email,
                    password
                })
            }
        );

        const data = await response.json();

        if(response.ok){

            console.log("Login Successful");

            localStorage.setItem(
                "token",
                data.access_token
            );

            window.location.href =
                "dashboard.html";

        }else{

            console.log("Invalid Credentials");

            alert("Invalid email or password");

        }

    } catch(error){

        console.error(error);

        alert("Server connection failed");

    }

});
