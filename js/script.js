const loginBtn = document.getElementById("loginBtn");

loginBtn.addEventListener("click", async (e) => {

    e.preventDefault();

    const email =
        document.getElementById("email").value;

    const password =
        document.getElementById("password").value;

    try {

        const response = await fetch(
            "http://localhost:8000/api/v1/auth/login",
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