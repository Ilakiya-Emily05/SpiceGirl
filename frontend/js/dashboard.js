// ======================================
// SPICE GIRLS DASHBOARD JS
// ======================================

document.addEventListener("DOMContentLoaded", () => {

    const uploadInput = document.getElementById("uploadInput");
    const uploadMessage = document.getElementById("uploadMessage");

    // ======================================
    // LOAD PREVIOUS DATA
    // ======================================

    const savedItems =
        JSON.parse(localStorage.getItem("spiceGirlsWardrobe")) || [];

    if (savedItems.length > 0) {

        const latestItem = savedItems[savedItems.length - 1];

        uploadMessage.innerHTML =
            `✨ Last uploaded: <strong>${latestItem.name}</strong>`;

    }

    // ======================================
    // IMAGE UPLOAD
    // ======================================

    uploadInput.addEventListener("change", function () {

        const file = this.files[0];

        if (!file) return;

        const reader = new FileReader();

        reader.onload = function (event) {

            const clothingItem = {

                id: Date.now(),

                name: file.name,

                image: event.target.result,

                uploadDate: new Date().toLocaleString()

            };

            const wardrobe =
                JSON.parse(
                    localStorage.getItem("spiceGirlsWardrobe")
                ) || [];

            wardrobe.push(clothingItem);

            localStorage.setItem(
                "spiceGirlsWardrobe",
                JSON.stringify(wardrobe)
            );

            uploadMessage.innerHTML =
                `✨ ${file.name} added to your wardrobe successfully!`;

            uploadMessage.style.color = "#28a745";

            alert(
                "✨ Added to your wardrobe successfully!"
            );

        };

        reader.readAsDataURL(file);

    });

    // ======================================
    // CURRENT OUTFIT CARD
    // ======================================

    const outfitTags =
        document.querySelectorAll(".tags span");

    outfitTags.forEach(tag => {

        tag.addEventListener("click", () => {

            alert(
                `Selected Tag: ${tag.textContent}`
            );

        });

    });

    // ======================================
    // WEATHER CARD
    // ======================================

    const weatherCard =
        document.querySelector(".weather-card");

    if (weatherCard) {

        weatherCard.addEventListener("mouseenter", () => {

            weatherCard.style.transform =
                "translateY(-4px)";

            weatherCard.style.transition =
                "0.3s";

        });

        weatherCard.addEventListener("mouseleave", () => {

            weatherCard.style.transform =
                "translateY(0px)";

        });

    }

    // ======================================
    // EVENT CARD
    // ======================================

    const eventCard =
        document.querySelector(".event-card");

    if (eventCard) {

        eventCard.addEventListener("mouseenter", () => {

            eventCard.style.transform =
                "translateY(-4px)";

            eventCard.style.transition =
                "0.3s";

        });

        eventCard.addEventListener("mouseleave", () => {

            eventCard.style.transform =
                "translateY(0px)";

        });

    }

    // ======================================
    // CONSOLE CHECK
    // ======================================

    console.log(
        "Spice Girls Dashboard Loaded Successfully 💖"
    );

});