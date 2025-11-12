# GushMap - 3D Map Viewer

Interactive 3D orthophoto map viewer with multiple locations.

## Current Status

✅ Repository created and pushed to GitHub
✅ Menu page with location selection
✅ Two viewer pages (Carmatz1 and Carmatz2)
⏳ Waiting for model files to be configured

## Next Steps to Complete Setup:

### 1. Enable GitHub Pages

1. Go to: https://github.com/Adiel-Sharabi/GushMap/settings/pages
2. Under "Source", select: **Deploy from a branch**
3. Under "Branch", select: **main** and **/ (root)**
4. Click **Save**
5. Wait 1-2 minutes for deployment

Your site will be available at: **https://adiel-sharabi.github.io/GushMap/**

### 2. Upload Model Files to GitHub Releases

Since your GLB files are large (50MB+), we need to use GitHub Releases:

**Option A: Upload to GitHub Releases (Recommended)**

1. Go to: https://github.com/Adiel-Sharabi/GushMap/releases/new
2. Create a new release (e.g., "v1.0")
3. Upload your GLB files:
   - Download from MEGA: https://mega.nz/file/IDAWETqA#rQ20OCQ30MTIVkKhYAkJnrIMt1o7oyZYoyGA985oH8c
   - Download from MEGA: https://mega.nz/file/sKQkEAgK#a_j0p4qm4rFmVK7mLCwvGRGJ9vW-IW8zLRe51QOC7Qo
   - Rename to: `carmatz1.glb` and `carmatz2.glb`
   - Upload both as release assets
4. Publish the release
5. Right-click each file → Copy link address
6. Edit `carmatz1.html` and `carmatz2.html` to add the direct download URLs

**Option B: Keep Models on MEGA**

MEGA links won't work directly in the browser due to CORS restrictions. You would need:
- A proxy service, or
- Download locally and use GitHub Releases (see Option A)

### 3. Update Viewer Pages with Model URLs

After uploading to GitHub Releases, update the viewer pages:

**carmatz1.html:**
```javascript
// Replace this line:
const MEGA_LINK = '...';

// With:
modelViewer.src = 'https://github.com/Adiel-Sharabi/GushMap/releases/download/v1.0/carmatz1.glb';
```

**carmatz2.html:**
```javascript
// Replace this line:
const MEGA_LINK = '...';

// With:
modelViewer.src = 'https://github.com/Adiel-Sharabi/GushMap/releases/download/v1.0/carmatz2.glb';
```

### 4. Commit and Push Changes

```bash
cd C:\dev\carmatz\github-pages
git add .
git commit -m "Add model URLs from GitHub Releases"
git push
```

## Features

- 📱 Mobile-friendly responsive design
- 🖱️ Interactive controls (drag to rotate, right-click to pan, scroll to zoom)
- 🔄 Reset camera button
- 📍 Multiple location support
- 🎨 Modern glassmorphism UI

## Controls

**Desktop:**
- Left-click + Drag: Spin map 360°
- Right-click + Drag: Pan/travel through complex
- Scroll: Zoom in/out
- Reset View button: Return to start position

**Mobile/Tablet:**
- Touch + Drag: Spin map and change angle
- Two-finger Drag: Pan/travel
- Pinch: Zoom in/out

## File Structure

```
github-pages/
├── index.html          # Menu page with location selection
├── carmatz1.html       # Carmatz 1 viewer
├── carmatz2.html       # Carmatz 2 viewer
└── README.md           # This file
```

## Technology Stack

- Google Model Viewer (for 3D rendering)
- HTML5 + CSS3 + JavaScript
- GitHub Pages (hosting)
- GitHub Releases (large file storage)

## Adding More Locations

To add a new location:

1. Create a new HTML file (e.g., `carmatz3.html`)
2. Copy from `carmatz1.html` and update:
   - Title
   - Location name
   - Model URL
3. Add a new card to `index.html`:
```html
<a href="carmatz3.html" class="location-card">
    <div class="location-icon">🏘️</div>
    <div class="location-name">Carmatz 3</div>
    <div class="location-description">...</div>
</a>
```
4. Commit and push

## Maintenance Workflow

```bash
# 1. Edit files locally
# 2. Test with local server: python -m http.server 8080
# 3. Commit changes
git add .
git commit -m "your message"
git push

# GitHub Pages will auto-deploy in ~1 minute
```

## Support

For issues or questions, refer to:
- Google Model Viewer docs: https://modelviewer.dev/
- GitHub Pages docs: https://docs.github.com/en/pages
