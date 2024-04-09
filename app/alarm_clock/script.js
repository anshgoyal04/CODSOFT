document.addEventListener('DOMContentLoaded', function() {
    // Display current time and date
    updateTime();
    setInterval(updateTime, 1000);

    function updateTime() {
        const now = new Date();
        const timeString = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        const dateString = now.toLocaleDateString();
        document.getElementById('current-time').textContent = timeString;
        document.getElementById('current-date').textContent = dateString;
    }

    // Show/hide screens
    const homeScreen = document.getElementById('home-screen');
    const alarmSettingScreen = document.getElementById('alarm-setting');
    const alarmManagementScreen = document.getElementById('alarm-management');
    const setAlarmBtn = document.getElementById('set-alarm-btn');
    const saveAlarmBtn = document.getElementById('save-alarm-btn');

    setAlarmBtn.addEventListener('click', function() {
        homeScreen.style.display = 'none';
        alarmSettingScreen.style.display = 'block';
    });

    saveAlarmBtn.addEventListener('click', function() {
        // Save alarm logic
        // Get selected alarm time and tone, and save them
        homeScreen.style.display = 'none';
        alarmSettingScreen.style.display = 'none';
        alarmManagementScreen.style.display = 'block';
    });

    // Manage alarms
    const alarmList = document.getElementById('alarm-list');
    // Retrieve saved alarms and display them in the list
    // Add toggle buttons for each alarm to enable/disable
});
