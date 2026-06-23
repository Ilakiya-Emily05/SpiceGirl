const monthTitle = document.getElementById("monthTitle");
const calendarGrid = document.getElementById("calendarGrid");

const outfitImage = document.getElementById("outfitImage");
const outfitName = document.getElementById("outfitName");
const outfitDate = document.getElementById("outfitDate");
const eventTitle = document.getElementById("eventTitle");
const eventDescription = document.getElementById("eventDescription");

let currentDate = new Date();

const outfits = {

    5: {
        name: "College Presentation",
        image: "images/college-fit.jpg",
        event: "UX Presentation",
        description: "Smart casual outfit for presentation."
    },

    12: {
        name: "Movie Night",
        image: "images/movie-fit.jpg",
        event: "Movie Night",
        description: "Cute and comfortable outfit."
    },

    18: {
        name: "Birthday Party",
        image: "images/party-fit.jpg",
        event: "Birthday Celebration",
        description: "Elegant party look."
    },

    24: {
        name: "Interview Outfit",
        image: "images/interview-fit.jpg",
        event: "Google Interview",
        description: "Professional and polished style."
    }
};

// =========================
// CALENDAR RENDER
// =========================

function renderCalendar(){

    calendarGrid.innerHTML = "";

    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();

    monthTitle.textContent =
        currentDate.toLocaleString("default", {
            month: "long",
            year: "numeric"
        });

    const firstDay =
        new Date(year, month, 1).getDay();

    const daysInMonth =
        new Date(year, month + 1, 0).getDate();

    for(let i = 0; i < firstDay; i++){
        calendarGrid.appendChild(document.createElement("div"));
    }

    for(let day = 1; day <= daysInMonth; day++){

        const dayBox = document.createElement("div");

        dayBox.classList.add("day");

        if(outfits[day]){
            dayBox.classList.add("has-outfit");
        }

        dayBox.textContent = day;

        dayBox.addEventListener("click", () => {

            document.querySelectorAll(".day")
                .forEach(d => d.classList.remove("active"));

            dayBox.classList.add("active");

            updateOutfitPanel(day);

        });

        calendarGrid.appendChild(dayBox);
    }
}

// =========================
// PANEL UPDATE
// =========================

function updateOutfitPanel(day){

    const selected = outfits[day];

    const monthName = currentDate.toLocaleString("default", {
        month: "long"
    });

    if(selected){

        outfitImage.src = selected.image;
        outfitName.textContent = selected.name;
        outfitDate.textContent = `Planned for ${monthName} ${day}`;
        eventTitle.textContent = selected.event;
        eventDescription.textContent = selected.description;

    } else {

        outfitImage.src = "images/default-fit.jpg";
        outfitName.textContent = "No Outfit Planned";
        outfitDate.textContent = "No outfit assigned";
        eventTitle.textContent = "No Event";
        eventDescription.textContent = "Select a date to plan an outfit.";
    }
}

// =========================
// NAVIGATION
// =========================

document.getElementById("prevMonth")
.addEventListener("click", () => {

    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar();

});

document.getElementById("nextMonth")
.addEventListener("click", () => {

    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar();

});

// =========================
// INIT
// =========================

renderCalendar();
