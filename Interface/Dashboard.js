 // Get a reference to the logout button by its class name
const logoutButton = document.querySelector('.logout-button');

// Add a click event listener to the logout button
logoutButton.addEventListener('click', function () {
    // Redirect to the login page
    window.location.href = 'Login.html';
});
const AiaButton = document.querySelector('.Ais-button');

// Add a click event listener to the logout button
logoutButton.addEventListener('click', function () {
    // Redirect to the login page
    window.location.href = 'Interface.html';
});


function updateTime() {
            const currentTimeElement = document.getElementById("time");
            const now = new Date();
            const hours = now.getHours().toString().padStart(2, "0");
            const minutes = now.getMinutes().toString().padStart(2, "0");
            const seconds = now.getSeconds().toString().padStart(2, "0");
            const timeString = `${hours}:${minutes}:${seconds}`;
            currentTimeElement.textContent = timeString;
        }

        // Update the time every second
        setInterval(updateTime, 1000);

        // Initial time update
        updateTime();
  