# Digital Clock - Multiple Time Zones

A beautiful, interactive web application that displays the current time across multiple time zones with real-time updates.

## Features

✨ **Key Features:**
- ⏰ Real-time digital clock display
- 🌍 Support for 35+ time zones worldwide
- 📅 Display date, time, GMT offset, and AM/PM indicator
- ➕ Add or remove time zones dynamically
- 🎨 Modern glassmorphism design with gradient background
- 📱 Fully responsive (mobile, tablet, desktop)
- ⚡ Smooth animations and hover effects
- 🔄 Auto-update every second
- 🔄 Reset to default time zones

## Live Demo

Open `index.html` in your web browser to see the clock in action!

```
file:///path/to/clock/index.html
```

## Project Structure

```
clock/
├── index.html      # HTML structure
├── styles.css      # CSS styling
├── script.js       # JavaScript functionality
└── README.md       # This file
```

## Files Description

### index.html
- Contains the HTML structure
- Clock grid container for displaying multiple clocks
- Control panel for adding/removing time zones
- List of current active time zones

### styles.css
- Modern glassmorphism design
- Gradient background (blue shades)
- Responsive grid layout
- Smooth transitions and animations
- Mobile-friendly design

### script.js
- State management for active time zones
- Real-time clock updates
- Time zone calculations
- GMT offset calculations
- Dynamic DOM manipulation

## Supported Time Zones

The application supports **35+ time zones** including:

### Americas
- EST (America/New_York)
- CST (America/Chicago)
- MST (America/Denver)
- PST (America/Los_Angeles)
- BRT (America/Sao_Paulo)
- ART (America/Argentina/Buenos_Aires)
- CLT (America/Santiago)
- AKST (America/Anchorage)
- HST (Pacific/Honolulu)

### Europe
- GMT (Europe/London)
- CET (Europe/Paris)
- EET (Europe/Athens)
- IST (Europe/Dublin)
- MSK (Europe/Moscow)

### Asia
- IST (Asia/Kolkata)
- JST (Asia/Tokyo)
- HKT (Asia/Hong_Kong)
- SGT (Asia/Singapore)
- BKT (Asia/Bangkok)
- GST (Asia/Dubai)
- And many more...

### Australia & Pacific
- AEST (Australia/Sydney)
- ACST (Australia/Adelaide)
- AWST (Australia/Perth)
- NZST (Pacific/Auckland)
- NZDT (Pacific/Auckland - Summer)

### Africa
- SAST (Africa/Johannesburg)
- CAT (Africa/Cairo)
- EAT (Africa/Nairobi)
- WAT (Africa/Lagos)

## Usage

### Viewing Current Time

1. Open `index.html` in your browser
2. The application displays 4 default time zones:
   - **America/New_York** (EST)
   - **Europe/London** (GMT)
   - **Asia/Kolkata** (IST)
   - **Asia/Tokyo** (JST)

### Adding a Time Zone

1. Select a time zone from the dropdown menu
2. Click the **"Add"** button
3. The new clock will appear in the grid
4. Each clock updates in real-time

### Removing a Time Zone

1. Click the **"×"** button on the top-right of any clock card
2. The clock will be removed immediately

### Resetting to Default

1. Click the **"Reset to Default"** button
2. Returns to the 4 default time zones

## Information Displayed

Each clock card shows:

| Information | Description |
|------------|-------------|
| **Timezone Name** | Full name and code of the time zone |
| **Digital Time** | Current time in HH:MM:SS format |
| **Date** | Current date in MM/DD/YYYY format |
| **GMT Offset** | Current GMT offset (e.g., +05:30) |
| **AM/PM** | Current period of the day |

## Responsive Design

The application is fully responsive:

### Desktop (1024px+)
- 3-4 columns grid layout
- Full-size clock cards
- All features visible

### Tablet (768px - 1023px)
- 2 columns grid layout
- Adjusted font sizes
- Optimal touch targets

### Mobile (< 768px)
- Single column layout
- Full-width cards
- Touch-friendly buttons
- Stacked controls

## Technology Stack

- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients and backdrop filters
- **JavaScript (Vanilla)** - No dependencies required
- **Intl API** - For accurate time zone conversions

## Browser Compatibility

Works on all modern browsers:
- ✅ Chrome/Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Opera 76+

## Performance

- **Lightweight**: No external dependencies
- **Optimized**: Efficient DOM updates
- **Smooth**: 60 FPS animations
- **Fast Loading**: Minimal file sizes

## Future Enhancements

Potential features to add:
- 🌙 Dark/Light theme toggle
- 🔔 Alarm functionality
- ⏱️ Stopwatch and timer
- 🌐 Timezone search
- 💾 Save favorite time zones
- 📊 Analog clock display option

## Credits

Created as a demonstration of:
- Modern CSS techniques (glassmorphism, gradients)
- JavaScript time zone handling
- Responsive web design
- Interactive UI components

## License

This project is open source and available for educational and personal use.

## Support

For issues or questions:
1. Check the code comments for detailed explanations
2. Review the function documentation in script.js
3. Test in different browsers

---

**Enjoy tracking time across the globe!** 🌍🕐
