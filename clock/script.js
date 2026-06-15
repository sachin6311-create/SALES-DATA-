// List of all available time zones
const ALL_TIMEZONES = [
    { name: 'UTC', offset: 'UTC' },
    { name: 'GMT', offset: 'Europe/London' },
    { name: 'EST', offset: 'America/New_York' },
    { name: 'CST', offset: 'America/Chicago' },
    { name: 'MST', offset: 'America/Denver' },
    { name: 'PST', offset: 'America/Los_Angeles' },
    { name: 'IST (India)', offset: 'Asia/Kolkata' },
    { name: 'JST (Japan)', offset: 'Asia/Tokyo' },
    { name: 'AEST (Sydney)', offset: 'Australia/Sydney' },
    { name: 'NZST (New Zealand)', offset: 'Pacific/Auckland' },
    { name: 'CET (Central Europe)', offset: 'Europe/Paris' },
    { name: 'EET (Eastern Europe)', offset: 'Europe/Athens' },
    { name: 'GST (Dubai)', offset: 'Asia/Dubai' },
    { name: 'SGT (Singapore)', offset: 'Asia/Singapore' },
    { name: 'HKT (Hong Kong)', offset: 'Asia/Hong_Kong' },
    { name: 'BKT (Bangkok)', offset: 'Asia/Bangkok' },
    { name: 'ICT (Indochina)', offset: 'Asia/Ho_Chi_Minh' },
    { name: 'MYT (Malaysia)', offset: 'Asia/Kuala_Lumpur' },
    { name: 'PHT (Philippines)', offset: 'Asia/Manila' },
    { name: 'WIB (Jakarta)', offset: 'Asia/Jakarta' },
    { name: 'ACST (Adelaide)', offset: 'Australia/Adelaide' },
    { name: 'AWST (Perth)', offset: 'Australia/Perth' },
    { name: 'SAST (South Africa)', offset: 'Africa/Johannesburg' },
    { name: 'CAT (Cairo)', offset: 'Africa/Cairo' },
    { name: 'EAT (Nairobi)', offset: 'Africa/Nairobi' },
    { name: 'WAT (Lagos)', offset: 'Africa/Lagos' },
    { name: 'BRT (Brasília)', offset: 'America/Sao_Paulo' },
    { name: 'ART (Buenos Aires)', offset: 'America/Argentina/Buenos_Aires' },
    { name: 'CLT (Santiago)', offset: 'America/Santiago' },
    { name: 'AKST (Anchorage)', offset: 'America/Anchorage' },
    { name: 'HST (Hawaii)', offset: 'Pacific/Honolulu' },
    { name: 'NZDT (New Zealand Summer)', offset: 'Pacific/Auckland' },
    { name: 'GST (Gulf Standard)', offset: 'Asia/Dubai' },
    { name: 'IST (Ireland)', offset: 'Europe/Dublin' },
    { name: 'MSK (Moscow)', offset: 'Europe/Moscow' },
];

// Default time zones to display
const DEFAULT_TIMEZONES = [
    'America/New_York',      // EST
    'Europe/London',         // GMT
    'Asia/Kolkata',          // IST
    'Asia/Tokyo'             // JST
];

// State management
let activeTimezones = [...DEFAULT_TIMEZONES];

// Initialize the application
function init() {
    populateTimezoneSelect();
    renderClocks();
    updateClocks();
    
    // Update clocks every second
    setInterval(updateClocks, 1000);
    
    // Event listeners
    document.getElementById('addBtn').addEventListener('click', addTimezone);
    document.getElementById('resetBtn').addEventListener('click', resetToDefault);
    document.getElementById('timezoneSelect').addEventListener('change', function() {
        if (this.value) {
            document.getElementById('addBtn').disabled = false;
        }
    });
}

// Populate the timezone select dropdown
function populateTimezoneSelect() {
    const select = document.getElementById('timezoneSelect');
    
    ALL_TIMEZONES.forEach(tz => {
        const option = document.createElement('option');
        option.value = tz.offset;
        option.textContent = tz.name;
        select.appendChild(option);
    });
}

// Render clock cards
function renderClocks() {
    const clockGrid = document.getElementById('clockGrid');
    clockGrid.innerHTML = '';
    
    activeTimezones.forEach(timezone => {
        const tzData = ALL_TIMEZONES.find(tz => tz.offset === timezone);
        const tzName = tzData ? tzData.name : timezone;
        
        const clockCard = document.createElement('div');
        clockCard.className = 'clock-card';
        clockCard.innerHTML = `
            <button class="remove-btn" onclick="removeTimezone('${timezone}')">×</button>
            <div class="timezone-name">${tzName}</div>
            <div class="digital-time" data-timezone="${timezone}">--:--:--</div>
            <div class="time-details">
                <div class="detail-item">
                    <div class="detail-label">Date</div>
                    <div class="detail-value" data-date="${timezone}">--/--/--</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">GMT Offset</div>
                    <div class="detail-value" data-offset="${timezone}">--:--</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">AM/PM</div>
                    <div class="detail-value" data-period="${timezone}">--</div>
                </div>
            </div>
        `;
        
        clockGrid.appendChild(clockCard);
    });
    
    updateTimezoneList();
}

// Update all clocks
function updateClocks() {
    const now = new Date();
    
    activeTimezones.forEach(timezone => {
        const formatter = new Intl.DateTimeFormat('en-US', {
            timeZone: timezone,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
        });
        
        const timeString = formatter.format(now);
        const timeElement = document.querySelector(`[data-timezone="${timezone}"]`);
        
        if (timeElement) {
            timeElement.textContent = timeString;
        }
        
        // Update date
        const dateFormatter = new Intl.DateTimeFormat('en-US', {
            timeZone: timezone,
            year: 'numeric',
            month: '2-digit',
            day: '2-digit'
        });
        
        const dateString = dateFormatter.format(now);
        const dateElement = document.querySelector(`[data-date="${timezone}"]`);
        if (dateElement) {
            dateElement.textContent = dateString;
        }
        
        // Update AM/PM
        const periodFormatter = new Intl.DateTimeFormat('en-US', {
            timeZone: timezone,
            hour: '2-digit',
            hour12: true
        });
        
        const hour12String = periodFormatter.format(now);
        const isPM = hour12String.includes('PM') || parseInt(hour12String) === 12;
        const period = isPM && !hour12String.includes('AM') ? 'PM' : 'AM';
        const periodElement = document.querySelector(`[data-period="${timezone}"]`);
        if (periodElement) {
            periodElement.textContent = period;
        }
        
        // Update GMT offset
        const offsetElement = document.querySelector(`[data-offset="${timezone}"]`);
        if (offsetElement) {
            const offset = getGMTOffset(now, timezone);
            offsetElement.textContent = offset;
        }
    });
}

// Calculate GMT offset
function getGMTOffset(date, timezone) {
    const tzFormatter = new Intl.DateTimeFormat('en-US', {
        timeZone: timezone,
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    });
    
    const parts = new Intl.DateTimeFormat('en-US', {
        timeZone: timezone,
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    }).formatToParts(date);
    
    const tzTime = new Date(
        parts.find(p => p.type === 'year').value,
        parts.find(p => p.type === 'month').value - 1,
        parts.find(p => p.type === 'day').value,
        parts.find(p => p.type === 'hour').value,
        parts.find(p => p.type === 'minute').value,
        parts.find(p => p.type === 'second').value
    );
    
    const diff = (date.getTime() - tzTime.getTime()) / 1000 / 60 / 60;
    const offset = Math.round(diff * 2) / 2;
    const sign = offset >= 0 ? '+' : '';
    const hours = Math.floor(Math.abs(offset));
    const minutes = Math.round((Math.abs(offset) - hours) * 60);
    
    return `${sign}${hours}:${minutes.toString().padStart(2, '0')}`;
}

// Add timezone
function addTimezone() {
    const select = document.getElementById('timezoneSelect');
    const timezone = select.value;
    
    if (timezone && !activeTimezones.includes(timezone)) {
        activeTimezones.push(timezone);
        renderClocks();
        select.value = '';
        select.disabled = true;
        document.getElementById('addBtn').disabled = true;
    } else if (activeTimezones.includes(timezone)) {
        alert('This timezone is already added!');
    }
}

// Remove timezone
function removeTimezone(timezone) {
    activeTimezones = activeTimezones.filter(tz => tz !== timezone);
    renderClocks();
}

// Reset to default timezones
function resetToDefault() {
    activeTimezones = [...DEFAULT_TIMEZONES];
    renderClocks();
    document.getElementById('timezoneSelect').value = '';
}

// Update timezone list
function updateTimezoneList() {
    const list = document.getElementById('timezoneList');
    list.innerHTML = '';
    
    activeTimezones.forEach(timezone => {
        const tzData = ALL_TIMEZONES.find(tz => tz.offset === timezone);
        const tzName = tzData ? tzData.name : timezone;
        
        const li = document.createElement('li');
        li.textContent = `${tzName} (${timezone})`;
        list.appendChild(li);
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', init);
