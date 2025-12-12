console.log("Dashboard JS Loaded");

// Fake attack logs (just sample data)
const sampleEvents = [
    "SSH brute force from 195.22.91.2",
    "HTTP exploit attempt from 77.120.19.88",
    "Telnet login attempt from 203.14.22.19",
    "Port scan detected from 187.55.34.11",
    "Malware dropper payload attempt from 102.99.13.7"
];

document.getElementById("refreshBtn").addEventListener("click", () => {
    const msg = document.getElementById("statusMsg");
    
    // Pick a random event to simulate activity
    const event = sampleEvents[Math.floor(Math.random() * sampleEvents.length)];

    msg.textContent = "Latest Event: " + event;
    msg.style.color = "#0de3ff";

    console.log("Event refreshed:", event);
});
