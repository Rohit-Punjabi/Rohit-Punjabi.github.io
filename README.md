# Rohit Punjabi Portfolio

Single page portfolio for Data Analyst, Software Engineer and Product Manager roles. No build step, no dependencies.

## Structure

- `index.html`: the home page (HTML/CSS/JS inline). One story for every visitor, then a "Where I fit" section
  with a card and resume for each role (Data Analyst, Software Engineer, Product Manager). Each featured project
  has a small "Shows" line naming which of the three it demonstrates.
- `projects.html`: the project archive, generated
- `projects/*.html`: one page per project, generated
- `build.py`: the generator. All the archive and project page copy lives in the `PROJECTS` list at the
  top of it. Edit there, run `python build.py`, and both the cards and the detail pages update together.
- `documents/`: the three resumes, named exactly `Rohit_Punjabi_Data_Analyst.pdf`,
  `Rohit_Punjabi_Software_Engineer.pdf` and `Rohit_Punjabi_Product_Manager.pdf` (the Resume buttons link to these)
- `images/`: charts and screenshots for the home page case studies
- `images/archive/`: card thumbnails for the archive page
- `images/projects/`: screenshots used inside the project pages
- `images/posters/`: first frame of each video, used as the video poster so nothing loads as a black box
- `videos/`: project videos, re-encoded to 720p H.264 (about 20 MB in total, down from 380 MB)
- `portfolio-website-plan.md`: the plan and old site audit this build follows

## Rebuilding the project pages

```
python build.py
```

No dependencies. It only writes `projects.html` and `projects/`.

## Deploy

Replace the contents of the `Rohit-Punjabi/Rohit-Punjabi.github.io` repo with this folder:

```
git clone https://github.com/Rohit-Punjabi/Rohit-Punjabi.github.io
# delete old files, copy this folder's contents in
git add -A && git commit -m "Unified homepage for data, engineering and product roles" && git push
```

Live at https://rohit-punjabi.github.io within a minute or two.

## Before launch checklist

1. Add all three resume PDFs to `documents/`
2. Verify LinkedIn and GitHub links open correctly
