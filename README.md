# 🎬 ANUJ DM - FILMMAKER PORTFOLIO

A stunning cinematic portfolio website with a **Film Maker Theme** featuring Oscar gold, film strips, spotlights, and red carpet vibes!

## ✨ Features

### 🎭 Cinematic Design
- **Dark & Professional**: Film black background with charcoal sections
- **Oscar Gold Accents**: (#d4af37) throughout the design
- **Film Strip Borders**: Vintage film reel borders on both sides
- **Red Carpet Curtains**: Opening animation on page load
- **Spotlight Effects**: Animated spotlights that follow your mouse

### 🎬 Special Elements
- **Clapboard**: Movie clapperboard with "TAKE ONE"
- **Film Decorations**: Floating movie icons (🎬, 🎥, 🎞️, 📽️)
- **Trinetra Studios Section**: Dedicated showcase for your studio
- **Video Gallery**: Beautiful frame design for featured works
- **Animated Badges**: Director, Editor, Cinematographer badges
- **Certificate Gallery**: Showcase your achievements

### 💫 Animations & Effects
- Red velvet curtain opening on page load
- Scroll reveal animations for sections
- Film reel spinning dots on skill cards
- Hover effects with golden glow
- Parallax effects on floating icons
- Smooth transitions throughout

### 📱 Fully Responsive
Works perfectly on all devices - desktop, tablet, and mobile!

## 📁 File Structure

```
PORTFOLIO/
│
├── index.html          # Main HTML file
├── style.css           # Cinematic styling
├── script.js           # Interactive JavaScript
├── README.md           # This file
│
├── images/             # Add your images here
│   ├── [certificates]  # Your certificate images
│   └── [profile]       # Profile photo (optional)
│
└── videos/             # Add your videos here
    ├── moments.of.kju-11-12-2025-0001.mp4
    └── VID_20251019132640.mp4
```

## 🚀 How to Use

### 1. Add Your Media Files

**Images Folder:**
Place your certificate images in the `images/` folder:
- `1-800549af-7f01-4298-87d3-6cfd0c6c1317.jpg`
- `anuj-dm-3d51f6b2-e61c-4915-b4f9-0e24c8084e2e-certificate.jpg`
- `anuj-dm-a8cb24fd-8176-4af7-bf3b-77c715354000-certificate (1).jpg`
- `UC-1d1902c0-cde0-48bf-9a6c-017805e86f05 (1).jpg`
- `UC-4d5040f7-2673-4808-a48b-7dd9c909a8fd (1).jpg`
- `ANUJ+D+M_152118534-images-0.jpg`

**Videos Folder:**
Place your video files in the `videos/` folder:
- `moments.of.kju-11-12-2025-0001.mp4`
- `VID_20251019132640.mp4`

### 2. Open the Portfolio

Simply **double-click** `index.html` to open the portfolio in your web browser!

No server required - it works directly from your computer.

### 3. Customize Content

**To change text:**
- Open `index.html` in any text editor (Notepad, VS Code, etc.)
- Search for the text you want to change
- Update it and save

**To add more certificates:**
1. Add the image to the `images/` folder
2. In `index.html`, find the certificate section
3. Copy and paste an existing certificate block
4. Update the image filename

**To add more videos:**
1. Add the video to the `videos/` folder
2. In `index.html`, find the video gallery section
3. Copy and paste an existing video block
4. Update the video filename and title

### 4. Customize Colors

All colors are defined in `style.css` at the top:

```css
:root {
    --film-black: #0a0a0a;          /* Main background */
    --oscar-gold: #d4af37;          /* Gold accents */
    --red-carpet: #b91c1c;          /* Red buttons */
    /* ... more colors */
}
```

Change these values to customize your color scheme!

## 🎨 Color Scheme

- **Film Black**: #0a0a0a (backgrounds)
- **Film Charcoal**: #1a1a1a (cards, sections)
- **Oscar Gold**: #d4af37 (accents, borders, highlights)
- **Gold Light**: #f4d03f (gradients)
- **Red Carpet**: #b91c1c (buttons, highlights)
- **Text White**: #ffffff
- **Text Gray**: #a0a0a0

## 🎥 Sections

1. **Home** - Hero section with clapboard and badges
2. **About** - Your story and journey
3. **Skills** - Technical, Editing, and Videography skills
4. **Awards** - Certificate gallery
5. **Studio** - Trinetra Studios showcase
6. **Featured** - Video gallery of your work
7. **Connect** - Social media links
8. **Contact** - Contact form

## 📧 Contact Form

The contact form currently shows a popup when submitted. The form data is logged to the browser console.

**To connect it to a backend:**
1. Open `script.js`
2. Find the "CONTACT FORM SUBMISSION" section
3. Replace the `setTimeout` with an actual API call to your server

Example:
```javascript
const response = await fetch('YOUR_API_URL', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, email, message })
});
```

## 🌐 Social Links

Update your social media links in `index.html`:
- **GitHub**: https://github.com/anujdm12
- **Instagram**: @anujj_dm (personal), @trinetra_studioss (studio)
- **LinkedIn**: Add your LinkedIn URL

## 💡 Tips

- **Test on different browsers**: Chrome, Firefox, Safari, Edge
- **Optimize images**: Compress images to load faster
- **Compress videos**: Use smaller video files for better performance
- **Keep it updated**: Add new projects and certificates regularly
- **Backup regularly**: Save copies of your work

## 🎬 Special Features

### Trinetra Studios Section
A dedicated full-screen section showcasing your studio with:
- Rotating logo animation
- Instagram link to @trinetra_studioss
- "Coming Soon" project teaser
- Cinematic background

### Interactive Elements
- Click the clapboard top to see it clap!
- Hover over skill cards to see film reel spin faster
- Hover over badges to see them pop
- Spotlights follow your mouse movement

## 🐛 Troubleshooting

**Images not showing?**
- Make sure images are in the `images/` folder
- Check that filenames match exactly (case-sensitive)

**Videos not playing?**
- Ensure videos are in MP4 format
- Check browser compatibility
- Try a different browser

**Layout looks broken?**
- Clear your browser cache (Ctrl + F5)
- Try opening in a different browser

## 📱 Responsive Breakpoints

- **Desktop**: Full experience with all effects
- **Tablet** (< 968px): Adjusted layouts
- **Mobile** (< 768px): Stacked layout, simplified navigation

## 🎭 Typography

- **Bebas Neue**: Headlines (bold, cinematic, uppercase)
- **Montserrat**: Body text (clean, professional)
- **Playfair Display**: Decorative quotes (elegant, serif)

## 🔥 Performance

- Optimized animations
- Lazy loading ready
- Minimal external dependencies
- Fast load times

## 📄 License

© 2026 Anuj DM. All rights reserved.

---

## 🎬 About This Theme

This portfolio uses a **Hollywood-inspired Film Maker theme** with:
- Professional cinematography aesthetics
- Film industry color palette
- Movie production design elements
- Red carpet premiere vibes

**Perfect for:** Filmmakers, Videographers, Editors, Content Creators, Media Professionals

---

## 💬 Need Help?

If you need to customize anything or add new features, the code is well-commented and easy to understand!

**Key Files:**
- `index.html` - Structure and content
- `style.css` - All styling and animations
- `script.js` - Interactions and effects

---

**🎬 ACTION! Your portfolio is ready to showcase your cinematic journey! 🌟**

Made with 🎥 and ❤️ for Anuj DM | Trinetra Studios
