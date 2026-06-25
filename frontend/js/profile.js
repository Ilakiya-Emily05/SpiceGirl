// ==============================
// PROFILE IMAGE UPLOAD
// ==============================

const profileUpload = document.getElementById("profileUpload");
const profileImage = document.getElementById("profileImage");

if (profileUpload && profileImage) {

    // Load saved image
    const savedImage = localStorage.getItem("profileImage");

    if (savedImage) {
        profileImage.src = savedImage;
    }

    profileUpload.addEventListener("change", function (event) {

        const file = event.target.files[0];

        if (!file) return;

        const reader = new FileReader();

        reader.onload = function (e) {

            profileImage.src = e.target.result;

            // Save image locally
            localStorage.setItem(
                "profileImage",
                e.target.result
            );

        };

        reader.readAsDataURL(file);

    });

}


// ==============================
// SAVE PREFERENCES
// ==============================

const saveBtn = document.getElementById("saveBtn");

if (saveBtn) {

    saveBtn.addEventListener("click", function () {

        const profileData = {

            style:
                document.getElementById("favoriteStyle").value,

            color:
                document.getElementById("favoriteColor").value,

            season:
                document.getElementById("season").value

        };

        localStorage.setItem(
          "profileData",
        JSON.stringify(profileData)
    );
        alert("Profile preferences saved!");

    });

}


// ==============================
// LOAD SAVED PREFERENCES
// ==============================

const savedData = JSON.parse(
    localStorage.getItem("profileData")
);

if (savedData) {

    document.getElementById("favoriteStyle").value =
        savedData.style;

    document.getElementById("favoriteColor").value =
        savedData.color;

    document.getElementById("season").value =
        savedData.season;

}


// ==============================
// LOGOUT
// ==============================

const logoutBtn = document.getElementById("logoutBtn");

if (logoutBtn) {

    logoutBtn.addEventListener("click", function () {

        localStorage.removeItem("token");

        window.location.href = "index.html";

    });

}