// =====================================
// ELEMENTS
// =====================================

const promptInput = document.getElementById("userPrompt");
const generateBtn = document.getElementById("generateBtn");
const chatArea = document.getElementById("chatArea");
const typingStatus = document.getElementById("typingStatus");

const promptButtons =
document.querySelectorAll(".prompt-btn");


// =====================================
// QUICK PROMPTS
// =====================================

const promptMap = {

    "🎓 College":
    "I have a college presentation tomorrow. Suggest a smart and comfortable outfit.",

    "💼 Interview":
    "I have an interview tomorrow. Suggest something professional.",

    "🎉 Party":
    "I have a birthday party tonight. I want an elegant outfit.",

    "☕ Casual":
    "Suggest a casual outfit for today's weather.",

    "💍 Wedding":
    "I have a wedding to attend. Suggest a traditional elegant outfit.",

    "✈ Vacation":
    "Suggest a stylish vacation outfit."

};


// =====================================
// QUICK BUTTONS
// =====================================

promptButtons.forEach(button=>{

    button.addEventListener("click",()=>{

        promptInput.value =
        promptMap[button.innerText];

        promptInput.focus();

    });

});


// =====================================
// GENERATE BUTTON
// =====================================

generateBtn.addEventListener("click",generateOutfit);


// =====================================
// MAIN FUNCTION
// =====================================

async function generateOutfit(){

    const prompt = promptInput.value.trim();

    if(prompt===""){

        alert("Please describe your outfit.");

        return;

    }

    addUserMessage(prompt);

    promptInput.value="";

    await aiThinking();
    updateOutfit(prompt);

    addAIMessage(
        "✨ Outfit generated successfully!\n\nI recommend a clean, elegant outfit that matches your occasion and style."
    );

}


// =====================================
// USER MESSAGE
// =====================================

function addUserMessage(message){

    chatArea.innerHTML += `

    <div class="user-message">

        <strong>You</strong>

        <p>${message}</p>

    </div>

    `;

    scrollChat();

}


// =====================================
// AI MESSAGE
// =====================================

function addAIMessage(message){

    chatArea.innerHTML += `

    <div class="ai-message">

        <strong>Spice Girls AI</strong>

        <p>${message}</p>

    </div>

    `;

    scrollChat();

}


// =====================================
// AI THINKING ANIMATION
// =====================================

async function aiThinking(){

    const steps=[

        "🤖 Thinking.",

        "🤖 Thinking..",

        "🤖 Thinking...",

        "👗 Checking your wardrobe...",

        "🌤 Checking today's weather...",

        "🎨 Matching your style...",

        "✨ Building your outfit...",

        "✅ Outfit Ready!"

    ];

    for(const step of steps){

        typingStatus.innerHTML=step;

        await sleep(800);

    }

    typingStatus.innerHTML="Ready to style you ✨";

}


// =====================================
// SLEEP
// =====================================
// =====================================
// CHANGE OUTFIT
// =====================================

function updateOutfit(prompt){

    const text = prompt.toLowerCase();

    let outfit;

    if(text.includes("interview")){

        outfit = {

            top:["👔","White Formal Shirt","Professional"],
            bottom:["👖","Black Formal Pants","Office Wear"],
            shoes:["👞","Black Loafers","Formal"],
            accessory:["⌚","Silver Watch","Classic"]

        };

    }

    else if(text.includes("party")){

        outfit = {

            top:["👗","Black Dress","Elegant"],
            bottom:["💫","Evening Style","Party Wear"],
            shoes:["👠","Black Heels","Stylish"],
            accessory:["💎","Silver Earrings","Luxury"]

        };

    }

    else if(text.includes("college")){

        outfit = {

            top:["👕","Oversized T-Shirt","Casual"],
            bottom:["👖","Blue Jeans","Comfort"],
            shoes:["👟","Sneakers","Walking"],
            accessory:["🎒","Backpack","Student"]

        };

    }

    else if(text.includes("vacation")){

        outfit = {

            top:["🌺","Floral Shirt","Beach"],
            bottom:["🩳","Cotton Shorts","Summer"],
            shoes:["🩴","Sandals","Comfort"],
            accessory:["🕶","Sunglasses","Vacation"]

        };

    }

    else if(text.includes("wedding")){

        outfit = {

            top:["🥻","Silk Saree","Traditional"],
            bottom:["✨","Matching Drapes","Elegant"],
            shoes:["👡","Golden Sandals","Festive"],
            accessory:["💍","Gold Jewellery","Classic"]

        };

    }

    else{

        outfit = {

            top:["👚","White Blouse","Minimal"],
            bottom:["👖","Black Trousers","Smart Casual"],
            shoes:["👟","White Sneakers","Comfort"],
            accessory:["👜","Black Tote Bag","Elegant"]

        };

    }

    document.getElementById("topEmoji").textContent = outfit.top[0];
    document.getElementById("topName").textContent = outfit.top[1];
    document.getElementById("topType").textContent = outfit.top[2];

    document.getElementById("bottomEmoji").textContent = outfit.bottom[0];
    document.getElementById("bottomName").textContent = outfit.bottom[1];
    document.getElementById("bottomType").textContent = outfit.bottom[2];

    document.getElementById("shoeEmoji").textContent = outfit.shoes[0];
    document.getElementById("shoeName").textContent = outfit.shoes[1];
    document.getElementById("shoeType").textContent = outfit.shoes[2];

    document.getElementById("accessoryEmoji").textContent = outfit.accessory[0];
    document.getElementById("accessoryName").textContent = outfit.accessory[1];
    document.getElementById("accessoryType").textContent = outfit.accessory[2];

}
function sleep(ms){

    return new Promise(resolve=>{

        setTimeout(resolve,ms);

    });

}


// =====================================
// CHAT SCROLL
// =====================================

function scrollChat(){

    chatArea.scrollTop=
    chatArea.scrollHeight;

}