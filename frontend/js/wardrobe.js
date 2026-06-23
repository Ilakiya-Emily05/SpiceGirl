// =========================
// CONFIG
// =========================

const BASE_URL = "http://localhost:8000";

// =========================
// SEARCH MODAL
// =========================

const searchBtn =
document.getElementById("searchBtn");

const modal =
document.getElementById("searchModal");

const closeModal =
document.querySelector(".close-modal");

searchBtn.addEventListener("click", () => {

    modal.style.display = "block";

});

closeModal.addEventListener("click", () => {

    modal.style.display = "none";

});

window.addEventListener("click", (e) => {

    if(e.target === modal){

        modal.style.display = "none";

    }

});

// =========================
// FILTER TAGS
// =========================

const filterTags =
document.querySelectorAll(".filter-tag");

const activeFilters =
document.getElementById("activeFilters");

filterTags.forEach(tag => {

    tag.addEventListener("click", () => {

        tag.classList.toggle("active");

    });

});

document
.getElementById("applyFilters")
.addEventListener("click", () => {

    activeFilters.innerHTML = "";

    document
    .querySelectorAll(".filter-tag.active")
    .forEach(tag => {

        const chip =
        document.createElement("span");

        chip.className =
        "filter-chip";

        chip.innerHTML =
        `${tag.textContent} ✕`;

        chip.addEventListener("click", () => {

            chip.remove();

            tag.classList.remove("active");

        });

        activeFilters.appendChild(chip);

    });

    modal.style.display = "none";

});

// =========================
// CARD SELECTION
// =========================

const cards =
document.querySelectorAll(".clothing-card");

const selectedItems =
document.getElementById("selectedItems");

function updateOutfitPanel(){

    const selectedCards =
    document.querySelectorAll(".clothing-card.selected");

    selectedItems.innerHTML = "";

    if(selectedCards.length === 0){

        selectedItems.innerHTML =
        `<p class="empty-state">No items selected yet.</p>`;

        return;
    }

    selectedCards.forEach(card => {

        const name = card.dataset.name;

        const item = document.createElement("div");

        item.className = "selected-item";

        item.textContent = name;

        selectedItems.appendChild(item);

    });

}

// =========================
// CARD CLICK SELECTION
// =========================

cards.forEach(card => {

    card.addEventListener("click", () => {

        card.classList.toggle("selected");

        updateOutfitPanel();

    });

});

// =========================
// SAVE FIT BUTTON (BACKEND CONNECTED)
// =========================

const saveBtn =
document.getElementById("saveFit");

const toast =
document.getElementById("toast");

saveBtn.addEventListener("click", async () => {

    const selectedCards =
    document.querySelectorAll(".clothing-card.selected");

    if(selectedCards.length === 0){

        alert("Select at least one clothing item.");
        return;

    }

    const clothing_ids = Array.from(selectedCards).map(card => card.dataset.name);

    try {

        await fetch(`${BASE_URL}/outfits/save`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                occasion: "College",
                clothing_ids: clothing_ids
            })

        });

    } catch (err) {
        console.error("Save outfit failed:", err);
    }

    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 2500);

});

// =========================
// CATEGORY FILTER
// =========================

const categoryButtons =
document.querySelectorAll(".sidebar li");

const categorySections =
document.querySelectorAll(".category-section");

categoryButtons.forEach(button => {

    button.addEventListener("click", () => {

        const category = button.dataset.category;

        if(category === "all"){

            categorySections.forEach(section => {
                section.style.display = "block";
            });

            return;
        }

        categorySections.forEach(section => {

            if(section.dataset.category === category){
                section.style.display = "block";
            } else {
                section.style.display = "none";
            }

        });

    });

});

// =========================
// SEARCH FUNCTION
// =========================

const searchInput =
document.getElementById("searchInput");

searchInput.addEventListener("keyup", () => {

    const searchValue =
    searchInput.value.toLowerCase();

    document.querySelectorAll(".clothing-card")
    .forEach(card => {

        const name = card.dataset.name.toLowerCase();

        if(name.includes(searchValue)){
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }

    });

});

// =========================
// UPLOAD CLOTHING (BACKEND CONNECTED)
// =========================

const uploadInput =
document.getElementById("uploadInput");

uploadInput.addEventListener("change", function(){

    const file = this.files[0];

    if(!file) return;

    const reader = new FileReader();

    reader.onload = async function(event){

        const imageBase64 = event.target.result;

        const clothingItem = {
            name: file.name,
            category: "Top",
            color: "White",
            season: "Summer",
            style: "Casual",
            image_url: imageBase64
        };

        // SEND TO BACKEND
        try {
            await fetch(`${BASE_URL}/clothes/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(clothingItem)
            });
        } catch (err) {
            console.error("Upload failed:", err);
        }

        // UI LOGIC (UNCHANGED)
        const topsGrid =
        document.querySelector('[data-category="tops"] .clothing-grid');

        const card = document.createElement("div");

        card.className = "clothing-card";

        card.dataset.name = file.name;

        card.innerHTML = `
            <img src="${imageBase64}">
            <h4>${file.name}</h4>
            <div class="tags">
                <span>New</span>
            </div>
        `;

        topsGrid.appendChild(card);

        card.addEventListener("click", () => {
            card.classList.toggle("selected");
            updateOutfitPanel();
        });

    };

    reader.readAsDataURL(file);

});

// =========================
// INITIAL STATE
// =========================

updateOutfitPanel();
