# -*- coding: utf-8 -*-
"""Builds projects.html (the archive) and projects/<slug>.html (one page per project).

Run:  python build.py

Everything on those pages comes from the PROJECTS list below. Edit the copy there,
rerun, and both the archive cards and the detail pages update together.
"""
import io, os

SITE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- block helpers
def p(t):               return ('p', t)
def h(t):               return ('h', t)
def bullets(*items):    return ('ul', list(items))
def img(src, cap=''):   return ('img', (src, cap))
def vid(src, cap=''):   return ('video', (src, cap))
def frame(src, cap=''): return ('iframe', (src, cap))
def gist(src, cap=''):  return ('gist', (src, cap))

# ---------------------------------------------------------------- project data
PROJECTS = [
 dict(
  slug='dream-destinations', group='apps', title='Dream Destinations',
  meta='Travel planning website', thumb='images/archive/dreamdestinations.jpg',
  tags=['HTML/CSS', 'PHP', 'MySQL', 'Apache'],
  card='A travel site that gets you ready for a trip rather than just selling one: food to expect in a '
       'country, places worth visiting, transport, and hotels, browsable by continent then country. The '
       'feedback form writes to a database behind an Apache server so responses can be reviewed for what '
       'people actually want.',
  lead='A website that covers everything about a place you want to visit, built around one idea: get the '
       'traveller ready before they land.',
  body=[
    p('Most travel sites are built to sell you a package. This one is built to prepare you. It walks you '
      'from continent, to country, to the detail you actually need on the ground: what the food is like, '
      'which places are worth the trip, how to move around, and where to stay.'),
    h('How you move through it'),
    img('images/projects/dd_home.jpg',
        'Home page. Contact, feedback, and the tour and destination detail all sit in the top right so you '
        'can jump straight to whichever one you came for.'),
    img('images/projects/dd_continent.jpg',
        'Continent page. Pick Asia and you get the countries inside it, each with a short description, so '
        'you can narrow down without opening ten tabs.'),
    img('images/projects/dd_country.jpg',
        'Country page. Tourist attractions, food specialities, heritage and art museums, transport, and '
        'hotel bookings, with a local contact option in the top left.'),
    h('The part that actually mattered'),
    p('The feedback form is the piece I care about most. Every submission is stored in a database behind an '
      'Apache server, which means feedback becomes a dataset rather than a pile of emails, and you can look '
      'at it to work out what travellers keep asking for.'),
    img('images/projects/dd_feedback.jpg',
        'Feedback page. Every response lands in the database for review.'),
  ]),

 dict(
  slug='shooting-madness', group='apps', title='Shooting Madness!!',
  meta='Android game, Unity', thumb='images/archive/shootingmadness.jpg',
  tags=['Unity3D', 'C#', 'Android'],
  card='A space shooter for phones where you scavenge and destroy, but scoring rewards picking targets '
       'carefully: green blocks add points, white blocks take them away, and the clock keeps running. I '
       'built the spawning system that randomises object type and position on a timer.',
  lead='A space shooter for Android where shooting everything is the losing strategy.',
  body=[
    p('You float in space and destroy what is around you, but the scoring makes you think before you fire. '
      'A green block adds five to your score, a white one takes three away, and other colours buy or burn '
      'seconds on the clock. Shoot carelessly and you run out of both points and time.'),
    img('images/projects/sm_info.jpg',
        'The information screen, reachable from the home menu, lays out how each colour affects your score '
        'and your remaining time.'),
    h('The spawning system'),
    p('The interesting piece is what keeps the field full. The spawner runs on three functions. Start fires '
      'once and decides when the next object appears, Update runs every second and calls the spawn when the '
      'timer says so, and the spawn function picks random x, y, and z coordinates, picks a prefab, and drops '
      'it in. Randomising both type and position is what stops the game settling into a pattern you can '
      'memorise.'),
    gist('https://gist.github.com/Rohit-Punjabi/6596058b660dd3f649193b274f696ea1.js',
         'Game manager: the start and update functions.'),
    gist('https://gist.github.com/Rohit-Punjabi/e7f31e9f2ecf097d9b5eddef841ca1e7.js',
         'The object spawning script.'),
    h('Gameplay'),
    vid('videos/ShootingMadness.mp4'),
  ]),

 dict(
  slug='snake', group='apps', title='Snake',
  meta='Android game, Android Studio', thumb='images/archive/snake_alt.jpg',
  tags=['Java', 'Android Studio'],
  card='The classic, rebuilt natively for modern phones. Touch navigation maps each direction to the '
       "snake's movement based on screen width and height, with the menu laid out in a constraints layout.",
  lead='The game everyone played on a Nokia, rebuilt natively for phones that are all screen.',
  body=[
    p('Rebuilding Snake sounds trivial until you take away the keypad. The whole game is direction input, '
      'and on a touch screen there are no keys, so the control scheme had to be rebuilt from scratch.'),
    h('Touch navigation'),
    p('The touch handler splits the screen by width and height and maps each region to left, right, up, or '
      'down, so the input behaves the same whatever size phone it lands on.'),
    gist('https://gist.github.com/Rohit-Punjabi/20ce55977d7b7637feb956645209993f.js',
         'The navigation script and its handler for each direction.'),
    img('images/projects/snake_layout.jpg',
        'The main screen in the Android Studio designer, with Play and Exit positioned in a constraints '
        'layout so the menu holds up across screen sizes.'),
    h('Gameplay'),
    vid('videos/SnakeVideo.mp4'),
  ]),

 dict(
  slug='roller-ball', group='apps', title='Roller Ball',
  meta='Desktop game, Unity', thumb='images/archive/rollerball_alt.jpg',
  tags=['Unity3D', 'C#'],
  card='Control a ball, stay on the platform, collect coins to reach the next level. The game manager runs '
       'on a four state machine covering playing, death, level complete, and game over.',
  lead='Control a ball, stay on the platform, collect the coins. Simple to play, and a clean exercise in '
       'game state.',
  body=[
    p('Roll around a platform, pick up coins, and do not fall off the edge. Clear the coins and the next '
      'level loads.'),
    h('Game state'),
    p('Everything runs through a game manager built on four states: playing, death, level complete, and '
      'game over. The update loop switches on the current state, which keeps every transition in one '
      'readable place instead of scattered across the objects.'),
    gist('https://gist.github.com/Rohit-Punjabi/4466898147270f93d26340493c149d7d.js',
         'The update function and its state switch.'),
    img('images/projects/rb_editor.jpg',
        'The project in the Unity editor: scene and game views on the left, hierarchy, project, and '
        'inspector stacked on the right.'),
    h('Gameplay'),
    vid('videos/roll.mp4'),
  ]),

 dict(
  slug='drifty-thrifty-bang-bang', group='engines', title='Drifty Thrifty Bang Bang',
  meta='Desktop game on a custom 3D engine', thumb='images/archive/dtbb.jpg',
  tags=['C++', 'OpenGL', 'SDL', 'FMOD', 'Lua', 'Figma'],
  card='A single player action adventure game about driving through arenas full of destructible objects '
       'and enemies, built with a team on a component based 3D engine we wrote in C++, SDL, OpenGL, FMOD, '
       'and Lua.',
  lead='A single player action adventure game about driving through arenas full of things to break, built '
       'on an engine we wrote ourselves.',
  body=[
    p('Part of my masters at DigiPen. You drive through arenas packed with destructible objects and '
      'enemies, and everything underneath it, rendering, audio, scripting, state, is a component based 3D '
      'engine our team built in C++ with SDL, OpenGL, FMOD, and Lua. No Unity, no Unreal.'),
    h('My role: game design lead and audio lead'),
    bullets(
      'Built the audio system for the engine on the FMOD core API',
      'Integrated a stack based game state manager so screens and gameplay states push and pop cleanly',
      'Added the sound effects and music across the game',
      'Designed the level layouts, blocking them out in Unity before rebuilding them in our engine',
      'Created the UI textures in Figma'),
    h('The UI work'),
    img('images/projects/dtbb_menu.jpg',
        'Main menu: start, settings and controls, credits, and exit.'),
    img('images/projects/dtbb_options.jpg',
        'Options. The controls shown change depending on whether a controller is plugged in, and audio and '
        'sound effects toggle from the same screen.'),
    img('images/projects/dtbb_hud.jpg',
        'In game HUD. Health top left, resource count under it, and on the right a counter for how many '
        'enemies of which type are left before the next level. Tips appear as you play so new players are '
        'never stuck.'),
    img('images/projects/dtbb_garage.jpg', 'The garage, where you spend what you collect.'),
    h('Trailer'),
    frame('https://drive.google.com/file/d/1VUd6h80JtvTeHceSvVf8TrqOwsvcoFZ1/preview'),
  ]),

 dict(
  slug='top-down-shooter', group='engines', title='Top Down Shooter',
  meta='Desktop game on a custom 2D engine', thumb='images/archive/lftclk.jpg',
  tags=['C++', 'DirectX', 'SDL', 'Lua'],
  card='An arcade shooter built with a team on a component based 2D engine written in C++, SDL, DirectX, '
       'FMOD, and Lua.',
  lead='An arcade shooter where you are a bike mechanic in a zombie infested forest, running on a 2D engine '
       'our team wrote from scratch.',
  body=[
    p('Another masters project at DigiPen, built with a team on a component based 2D engine we wrote in C++ '
      'with SDL, DirectX, FMOD, and Lua.'),
    h('My role: gameplay programmer'),
    bullets(
      'Implemented the 2D collision detection',
      'Built an input handling system driven by Lua scripting, so any key could be remapped to any in game '
      'action without touching the engine',
      'Built a full level end to end',
      'Implemented a large share of the gameplay mechanics',
      'Made some of the simpler textures'),
    h('Trailer'),
    vid('videos/BMGWCISIAZIF_trailer.mp4'),
  ],
  links=[('Engine on GitHub', 'https://github.com/LFTCLICK/lftclick_engine')]),

 dict(
  slug='behaviour-tree', group='engines', title='Behaviour Tree',
  meta='AI tech demo', thumb='images/archive/behaviourtree.jpg',
  tags=['C++', 'Game AI'],
  card='Implemented a behaviour tree and wired it into our custom 2D engine, then used it to build a boss '
       'fight where the enemy shoots, dodges, spawns zombies, and repositions itself based on the state of '
       'the fight.',
  lead='A behaviour tree implementation wired into our custom 2D engine, then pushed until it could run a '
       'boss fight.',
  body=[
    p('Implementing the tree is one thing. Proving it holds up is another, so I used it to build a boss '
      'level where the enemy has a real range of options: shoot bullets, dodge, spawn zombies, and move to '
      'a new position. The tree decides which one fits the current state of the fight, which is what makes '
      'the boss feel like it is reacting to you rather than running a loop.'),
    h('The behaviour class'),
    gist('https://gist.github.com/Rohit-Punjabi/2eb9f98f6d4c21f2f10311ea8b296b1d.js'),
    h('The demo'),
    frame('https://drive.google.com/file/d/191r62MUr38wEP8BQuLvymUBSrFskrOZV/preview'),
  ]),

 dict(
  slug='goap-smart-objects', group='engines',
  title='Goal Oriented Action Planning with Smart Objects',
  meta='AI tech demo, Unreal Engine', thumb='images/archive/goap.jpg',
  tags=['Unreal Engine', 'C++', 'Game AI'],
  card='Instead of a separate action class, the planner compiles every smart object in the scene and reads '
       'preconditions and effects off the objects themselves. Agents query the planner with a current state '
       'and a goal state, get back an ordered list of objects to interact with, and step through it using '
       'an internal state machine so the behaviour reads as believable.',
  lead='A planner that reads what is possible off the world itself, rather than off a list of actions '
       'someone wrote down.',
  body=[
    p('Classic goal oriented action planning defines a separate action class and hands the planner a list '
      'of them. We took the actions out. The planner compiles every smart object in the scene, and '
      'preconditions and effects are assigned to those objects directly, so the world describes what it '
      'makes possible.'),
    p('An agent queries the planner with its current state and its goal state. The planner returns an '
      'ordered list of the smart objects to interact with, and the state the agent will be in between each '
      'one, ordered so every step moves it closer to the goal in a way that looks believable. The agent '
      'then runs an internal finite state machine to walk that list and interact with each object in turn.'),
    p('Built in Unreal Engine 4, though nothing about the approach is tied to it. It would drop into more '
      'or less any C++ engine or editor.'),
    h('The demo'),
    frame('https://www.youtube.com/embed/BaeMrHfYhps'),
    h('How it works, explained'),
    frame('https://www.youtube.com/embed/eEtfNxSJ-7w'),
  ]),

 dict(
  slug='soft-body-simulation', group='graphics', title='Soft Body Simulation',
  meta='Physics tech demo', thumb='images/archive/softbody.jpg',
  tags=['C++', 'RK4', 'Numerical methods'],
  card='A cube made of 125 mass points, each carrying its own force, velocity, position, and mass, '
       'integrated with RK4 every frame. I built a spring data structure to connect points, drawn as yellow '
       'lines between the purple masses so you can watch the structure deform and settle.',
  lead='A cube of 125 mass points held together by springs, integrated with RK4, wobbling the way a real '
       'soft object does.',
  body=[
    p('The cube is not a mesh. It is 125 individual mass points, each carrying its own force, velocity, '
      'position, and mass, and every one of them gets its position and velocity updated with the RK4 method '
      'once per frame. RK4 is what keeps the motion stable instead of exploding after a few seconds.'),
    p('Holding it together is a spring data structure I designed to connect any two mass points '
      'efficiently. In the demo the springs are the yellow lines and the mass points are the purple dots, '
      'so you can watch the structure stretch, compress, and settle back rather than just seeing a surface '
      'move.'),
    h('The demo'),
    vid('videos/SoftBodySimulation.mp4'),
  ]),

 dict(
  slug='bezier-curves', group='graphics', title='Bezier Curve Generator',
  meta='Academic project, MAT500 Curves and Surfaces', thumb='images/archive/bezier.jpg',
  tags=['C++', 'Computational geometry'],
  card='An application that generates Bezier curves from control points you place yourself, computing the '
       'same curve three different ways so you can compare them: De Casteljau nested linear interpolation, '
       'Bernstein polynomials, and midpoint subdivision.',
  lead='Place control points, get a Bezier curve, and watch the same curve get built three different ways.',
  body=[
    p('Built for the MAT500 Curves and Surfaces class at DigiPen. You place the control points and the '
      'application generates the curve, but it computes it three separate ways so you can compare how each '
      'method arrives at the same shape.'),
    h('De Casteljau, or nested linear interpolation'),
    vid('videos/NLI.mp4'),
    h('Midpoint subdivision'),
    vid('videos/MidPoint.mp4'),
    h('Bernstein polynomials'),
    vid('videos/BBPlot.mp4'),
  ],
  links=[('Code on GitHub', 'https://github.com/Rohit-Punjabi/Bezier_Curves')]),

 dict(
  slug='inverse-kinematics', group='graphics', title='Inverse Kinematics',
  meta='Animation tech demo', thumb='images/archive/ik.jpg',
  tags=['C++', 'Animation', 'Linear algebra'],
  card='A demo that solves a joint chain back from a target position, so a limb reaches for a point in '
       'space and every joint above it settles into a pose that works.',
  lead='Give the end of a joint chain a target, and let the maths work out where every joint above it has '
       'to go.',
  body=[
    p('Forward kinematics is the easy direction: set the joint angles, see where the hand ends up. Inverse '
      'kinematics runs it backwards. You say where the hand should be, and the solver works out a set of '
      'joint angles that puts it there while keeping the rest of the chain in a pose that looks right. It '
      'is the difference between animating every joint by hand and telling a character to reach for '
      'something.'),
    h('The demo'),
    vid('videos/IKVideo.mp4'),
  ]),

 dict(
  slug='cnn-image-classification', group='ml', title='Image Classification with a CNN',
  meta='Deep learning project', thumb='images/projects/cnn_hero.jpg',
  tags=['Python', 'TensorFlow', 'NumPy', 'Matplotlib'],
  card='Trained convolutional networks across three datasets, comparing a fully connected network against '
       'a CNN and tracking accuracy over epochs to see where each one breaks down.',
  lead='Three rounds of image classification, each one making the problem harder, to see where a '
       'convolutional network pulls ahead and where it starts to struggle.',
  body=[
    p('Built with Python, NumPy, TensorFlow, and Matplotlib, in three parts that get progressively harder.'),
    h('Part one: four classes, and a fair fight'),
    p('Loaded a local set of 20,000 images across four classes and trained two networks on it, a fully '
      'connected one and a convolutional one, then compared their accuracy directly. Same data, same '
      'problem, so the gap between them comes down to the architecture and nothing else.'),
    h('Part two: ten classes'),
    p('Loaded CIFAR 10 from TensorFlow, 60,000 images across ten classes, trained a convolutional network, '
      'and plotted accuracy over epochs. Comparing predicted against actual output visually is what tells '
      'you whether the model is genuinely learning or just memorising the training set.'),
    h('Part three: a hundred classes'),
    p('The same 60,000 images, now split across a hundred classes in CIFAR 100. Far fewer examples per '
      'class, and the accuracy curves show exactly how much that costs you.'),
    h('The code'),
    gist('https://gist.github.com/Rohit-Punjabi/a8aae8fe4c257b83bcca6cd2743dee14.js'),
  ]),
]

GROUPS = [
 ('engines', 'Custom game engines and gameplay',
  'Team projects from my masters at DigiPen, all built on engines we wrote ourselves in C++ rather than on '
  'Unity or Unreal.'),
 ('graphics', 'Graphics, simulation, and math',
  'The projects where the interesting part is the maths and the numerical method, not the game around it.'),
 ('ml', 'Machine learning',
  'Where the move toward data and analytics started.'),
 ('apps', 'Apps and web',
  'Shipped products with real users, real UI decisions, and a database behind them.'),
]

PAPERS = [
 dict(title='Artificial Intelligence for Digital Games: LUDOTRIX', meta='IRJET, 2020',
      text='Proposed a new take on Ludo that mixes artificial intelligence with mechanics borrowed from '
           'two of the most popular game genres.',
      tags=['Game AI', 'Research'],
      url='https://www.irjet.net/archives/V7/i10/IRJET-V7I10286.pdf'),
 dict(title='A Scalable Method for Conversion of Typed Text into Handwritten Text', meta='IJRASET, 2020',
      text='Built software that converts typed text into handwriting that looks like it came off a page, '
           'with the method designed to scale rather than being tuned to one writer.',
      tags=['Applied ML', 'Python', 'Research'],
      url='https://doi.org/10.22214/ijraset.2020.32273'),
]

FEATURED = ['Player Telemetry &amp; Analytics Platform', 'Inventory Analytics &amp; Demand Forecasting',
            'AWS Image Processing Automation', 'F1 Stats &amp; Race Companion App']

# ---------------------------------------------------------------------- styles
BASE_CSS = """
  :root{
    --ink:#2b2226; --ink-soft:#5c5156; --ink-faint:#766a70;
    --accent:#c81440; --accent-soft:#fbe7ec;
    --bg:#fdf8ec; --bg-card:#fffdf6; --bg-alt:#f8f0dd; --line:#eadfc9; --max:960px;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    color:var(--ink);background:var(--bg);line-height:1.6;font-size:16px}
  .wrap{max-width:var(--max);margin:0 auto;padding:0 24px}
  a{color:var(--accent);text-decoration:none}
  a:hover{text-decoration:underline}
  nav{position:sticky;top:0;background:rgba(253,248,236,.95);backdrop-filter:blur(8px);
    border-bottom:1px solid var(--line);z-index:100}
  .nav-inner{display:flex;align-items:center;justify-content:space-between;height:56px}
  .nav-name{font-weight:700;font-size:1rem;color:var(--ink);letter-spacing:-.01em}
  .nav-name:hover{text-decoration:none;color:var(--accent)}
  .nav-links{display:flex;gap:22px;list-style:none}
  .nav-links a{color:var(--ink-soft);font-size:.9rem;font-weight:500}
  .nav-links a.here{color:var(--accent)}
  .nav-links a:hover{color:var(--accent);text-decoration:none}
  .nav-toggle{display:none;background:none;border:none;font-size:1.4rem;color:var(--ink);cursor:pointer}
  .kicker{display:inline-block;background:var(--accent-soft);color:var(--accent);font-size:.78rem;
    font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:4px 12px;border-radius:100px;
    margin-bottom:18px}
  h1{font-size:clamp(1.8rem,4.4vw,2.6rem);line-height:1.15;letter-spacing:-.02em;margin-bottom:16px}
  h1 .accent{color:var(--accent)}
  .tags{display:flex;flex-wrap:wrap;gap:7px}
  .tag{font-size:.76rem;font-weight:600;color:var(--accent);background:var(--accent-soft);
    padding:3px 10px;border-radius:100px}
  .pill{background:var(--bg-card);border:1px solid var(--line);border-radius:100px;padding:7px 16px;
    font-size:.9rem;font-weight:600;color:var(--ink)}
  .pill:hover{text-decoration:none;border-color:var(--accent);color:var(--accent)}
  footer{border-top:1px solid var(--line);padding:22px 0;font-size:.82rem;color:var(--ink-faint);
    margin-top:8px}
  .foot-inner{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
  @media (max-width:760px){
    .nav-links{display:none;position:absolute;top:56px;left:0;right:0;background:var(--bg);
      flex-direction:column;gap:0;border-bottom:1px solid var(--line)}
    .nav-links.open{display:flex}
    .nav-links li{border-top:1px solid var(--line)}
    .nav-links a{display:block;padding:14px 24px}
    .nav-toggle{display:block}
  }
"""

ARCHIVE_CSS = """
  header{padding:48px 0 34px}
  .lead{font-size:1.05rem;color:var(--ink-soft);max-width:680px;margin-bottom:22px}
  .back{font-size:.92rem;font-weight:600}
  .featured-band{background:var(--bg-alt);border-top:1px solid var(--line);
    border-bottom:1px solid var(--line);padding:26px 0}
  .featured-band h2{font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;
    color:var(--ink-faint);margin-bottom:12px}
  .pill-row{display:flex;flex-wrap:wrap;gap:10px}
  section{padding:52px 0;scroll-margin-top:56px}
  section.alt{background:var(--bg-alt);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
  h2.group{font-size:1.45rem;letter-spacing:-.01em;margin-bottom:6px}
  .group-lead{color:var(--ink-soft);margin-bottom:28px;max-width:640px;font-size:.98rem}
  .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
  .card{display:flex;flex-direction:column;background:var(--bg-card);border:1px solid var(--line);
    border-radius:14px;overflow:hidden;transition:transform .15s ease,border-color .15s ease}
  .card:hover{transform:translateY(-2px);border-color:var(--accent);text-decoration:none}
  a.card,a.card:hover{color:inherit}
  .shot{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;background:var(--bg-alt);
    border-bottom:1px solid var(--line)}
  .card-body{padding:20px 22px 22px;display:flex;flex-direction:column;flex:1}
  .card h3{font-size:1.08rem;letter-spacing:-.01em;margin-bottom:3px}
  .card .meta{font-size:.82rem;color:var(--ink-faint);font-weight:500;margin-bottom:10px}
  .card p{font-size:.93rem;color:var(--ink-soft);margin-bottom:14px}
  .card .tags{margin-top:auto}
  .open{font-size:.88rem;font-weight:700;color:var(--accent);margin-top:12px}
  .card-links{font-size:.88rem;font-weight:600;margin-top:12px}
  @media (max-width:760px){ .grid{grid-template-columns:1fr} header{padding:40px 0 30px} }
"""

DETAIL_CSS = """
  header{padding:44px 0 30px}
  .lead{font-size:1.1rem;color:var(--ink-soft);max-width:680px;margin-bottom:18px}
  .meta-line{color:var(--ink-faint);font-size:.92rem;font-weight:500;margin-bottom:16px}
  .head-tags{margin-bottom:20px}
  .crumb{font-size:.9rem;font-weight:600;margin-bottom:20px;display:block}
  article{padding:8px 0 48px}
  article h2{font-size:1.25rem;letter-spacing:-.01em;margin:40px 0 12px}
  article p{color:var(--ink-soft);max-width:680px;margin-bottom:16px}
  article ul{list-style:none;max-width:680px;margin-bottom:18px}
  article li{color:var(--ink-soft);padding-left:20px;position:relative;margin-bottom:8px}
  article li::before{content:"\\2022";position:absolute;left:2px;color:var(--accent);font-weight:800}
  figure{margin:22px 0 26px}
  figure img,figure video{display:block;width:100%;height:auto;border-radius:12px;
    border:1px solid var(--line);background:#000}
  figure img{background:var(--bg-alt)}
  figcaption{font-size:.85rem;color:var(--ink-faint);margin-top:9px;max-width:680px}
  .embed{position:relative;padding-top:56.25%;border-radius:12px;overflow:hidden;
    border:1px solid var(--line);background:#000}
  .embed iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
  .gist-wrap{margin:18px 0 26px;font-size:.9rem}
  .links-row{display:flex;flex-wrap:wrap;gap:12px;margin-top:34px;padding-top:26px;
    border-top:1px solid var(--line)}
  .pager{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:26px 0 10px;
    border-top:1px solid var(--line);font-size:.92rem;font-weight:600}
"""

NAV_LINKS = [('Featured', '{root}index.html#projects'), ('All Projects', '{root}projects.html'),
             ('Experience', '{root}index.html#experience'), ('Skills', '{root}index.html#skills'),
             ('Contact', '{root}index.html#contact'),
             ('Resume', '{root}documents/Rohit_Punjabi_Data_Analyst.pdf')]

def nav(root, here=''):
    items = []
    for label, href in NAV_LINKS:
        cls = ' class="here"' if label == here else ''
        extra = ' target="_blank" rel="noopener"' if label == 'Resume' else ''
        items.append('      <li><a%s href="%s"%s>%s</a></li>' % (cls, href.format(root=root), extra, label))
    return """<nav>
  <div class="wrap nav-inner">
    <a class="nav-name" href="{root}index.html">Rohit Punjabi</a>
    <button class="nav-toggle" id="navToggle" aria-label="Menu">&#9776;</button>
    <ul class="nav-links" id="navLinks">
{items}
    </ul>
  </div>
</nav>""".format(root=root, items='\n'.join(items))

FOOT = """<footer>
  <div class="wrap foot-inner">
    <span>&copy; 2026 Rohit Punjabi</span>
    <span><a href="https://github.com/Rohit-Punjabi" target="_blank" rel="noopener">GitHub</a> &middot;
      <a href="https://www.linkedin.com/in/punjabi-rohit" target="_blank" rel="noopener">LinkedIn</a></span>
  </div>
</footer>

<script>
  const toggle=document.getElementById('navToggle');
  const links=document.getElementById('navLinks');
  toggle.addEventListener('click',()=>links.classList.toggle('open'));
  links.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>links.classList.remove('open')));
</script>
</body>
</html>
"""

def shell(title, desc, css, body):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<style>%s%s</style>
</head>
<body>

%s""" % (title, desc, BASE_CSS, css, body)

def tags_html(tags):
    return '<div class="tags">%s</div>' % ''.join('<span class="tag">%s</span>' % t for t in tags)

# ------------------------------------------------------------------ detail page
def render_block(kind, val, root):
    if kind == 'p':
        return '      <p>%s</p>' % val
    if kind == 'h':
        return '      <h2>%s</h2>' % val
    if kind == 'ul':
        return '      <ul>\n%s\n      </ul>' % '\n'.join('        <li>%s</li>' % i for i in val)
    src, cap = val
    cap_html = '\n        <figcaption>%s</figcaption>' % cap if cap else ''
    if kind == 'img':
        return ('      <figure>\n        <img src="%s%s" alt="%s" loading="lazy">%s\n      </figure>'
                % (root, src, cap or 'Project screenshot', cap_html))
    if kind == 'video':
        poster = 'images/posters/%s.jpg' % os.path.basename(src).rsplit('.', 1)[0]
        poster_attr = ' poster="%s%s"' % (root, poster) if os.path.exists(
            os.path.join(SITE, poster)) else ''
        return ('      <figure>\n        <video src="%s%s"%s controls preload="none" '
                'playsinline></video>%s\n      </figure>' % (root, src, poster_attr, cap_html))
    if kind == 'iframe':
        return ('      <figure>\n        <div class="embed"><iframe src="%s" allowfullscreen '
                'allow="autoplay; encrypted-media" loading="lazy"></iframe></div>%s\n      </figure>'
                % (src, cap_html))
    if kind == 'gist':
        return ('      <div class="gist-wrap">%s<script src="%s"></script></div>'
                % (('<p>%s</p>' % cap) if cap else '', src))
    raise ValueError(kind)

def detail_page(proj, prev_p, next_p):
    root = '../'
    blocks = '\n'.join(render_block(k, v, root) for k, v in proj['body'])
    links = ''
    if proj.get('links'):
        links = '\n      <div class="links-row">%s</div>' % ''.join(
            '<a class="pill" href="%s" target="_blank" rel="noopener">%s &rarr;</a>' % (u, l)
            for l, u in proj['links'])
    pager = []
    if prev_p:
        pager.append('<a href="%s.html">&larr; %s</a>' % (prev_p['slug'], prev_p['title']))
    else:
        pager.append('<span></span>')
    if next_p:
        pager.append('<a href="%s.html">%s &rarr;</a>' % (next_p['slug'], next_p['title']))
    body = """{nav}

<header>
  <div class="wrap">
    <a class="crumb" href="../projects.html">&larr; All projects</a>
    <span class="kicker">{group}</span>
    <h1>{title}</h1>
    <p class="meta-line">{meta}</p>
    <p class="lead">{lead}</p>
    <div class="head-tags">{tags}</div>
  </div>
</header>

<article>
  <div class="wrap">
{blocks}{links}
  </div>
</article>

<div class="wrap pager">
  {pager}
</div>

""".format(nav=nav(root), group=dict((g[0], g[1]) for g in GROUPS)[proj['group']],
           title=proj['title'], meta=proj['meta'], lead=proj['lead'],
           tags=tags_html(proj['tags']), blocks=blocks, links=links,
           pager='\n  '.join(pager))
    desc = proj['card'].replace('"', "'")[:180]
    return shell('%s | Rohit Punjabi' % proj['title'], desc, DETAIL_CSS, body) + FOOT

# ----------------------------------------------------------------- archive page
def card_html(proj):
    thumb = ('<img class="shot" src="%s" alt="%s" loading="lazy">' % (proj['thumb'], proj['title'])
             if proj.get('thumb') else '')
    return """      <a class="card" href="projects/{slug}.html">
        {thumb}
        <div class="card-body">
          <h3>{title}</h3>
          <p class="meta">{meta}</p>
          <p>{card}</p>
          {tags}
          <p class="open">Open the case study &rarr;</p>
        </div>
      </a>""".format(slug=proj['slug'], thumb=thumb, title=proj['title'],
                     meta=proj['meta'], card=proj['card'], tags=tags_html(proj['tags']))

def paper_html(paper):
    return """      <article class="card">
        <div class="card-body">
          <h3>{title}</h3>
          <p class="meta">{meta}</p>
          <p>{text}</p>
          {tags}
          <p class="card-links"><a href="{url}" target="_blank" rel="noopener">Read the paper &rarr;</a></p>
        </div>
      </article>""".format(title=paper['title'], meta=paper['meta'], text=paper['text'],
                     url=paper['url'], tags=tags_html(paper['tags']))

def archive_page():
    sections = []
    alt = False
    for key, name, lead in GROUPS:
        cards = [card_html(pr) for pr in PROJECTS if pr['group'] == key]
        if not cards:
            continue
        sections.append("""<section class="{cls}" id="{key}">
  <div class="wrap">
    <h2 class="group">{name}</h2>
    <p class="group-lead">{lead}</p>
    <div class="grid">
{cards}
    </div>
  </div>
</section>""".format(cls='alt' if alt else '', key=key, name=name, lead=lead,
                     cards='\n\n'.join(cards)))
        alt = not alt
    sections.append("""<section class="{cls}" id="research">
  <div class="wrap">
    <h2 class="group">Published research</h2>
    <p class="group-lead">Two papers from my undergraduate years, both applied rather than theoretical.</p>
    <div class="grid">
{papers}
    </div>
  </div>
</section>""".format(cls='alt' if alt else '', papers='\n\n'.join(paper_html(x) for x in PAPERS)))

    body = """{nav}

<header id="top">
  <div class="wrap">
    <span class="kicker">Project archive</span>
    <h1>Everything I have <span class="accent">built so far.</span></h1>
    <p class="lead">
      The home page keeps the case studies that matter most for analytics and product work. This page is
      the full shelf: custom game engines, simulation and AI tech demos, and the apps I shipped, going back
      to my masters at DigiPen. Every card opens its own page with the screenshots, videos, and code behind it.
    </p>
    <a class="back" href="index.html">&larr; Back to the home page</a>
  </div>
</header>

<div class="featured-band">
  <div class="wrap">
    <h2>Featured case studies live on the home page</h2>
    <div class="pill-row">
{featured}
    </div>
  </div>
</div>

{sections}

<section>
  <div class="wrap" style="text-align:center">
    <h2 class="group">Want the short version?</h2>
    <p class="group-lead" style="margin:0 auto 22px">The case studies on the home page are the ones I would
      open first in an interview.</p>
    <a class="pill" href="index.html#projects" style="display:inline-block">Back to featured projects</a>
  </div>
</section>

""".format(nav=nav('', here='All Projects'),
           featured='\n'.join('      <a class="pill" href="index.html#projects">%s</a>' % f
                              for f in FEATURED),
           sections='\n\n'.join(sections))
    return shell('All Projects | Rohit Punjabi',
                 'The full project archive for Rohit Punjabi: apps, custom game engines, graphics and AI '
                 'tech demos, and published research.', ARCHIVE_CSS, body) + FOOT

# ------------------------------------------------------------------------- main
def main():
    out_dir = os.path.join(SITE, 'projects')
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    io.open(os.path.join(SITE, 'projects.html'), 'w', encoding='utf-8',
            newline='').write(archive_page())
    order = [pr for key, _, _ in GROUPS for pr in PROJECTS if pr['group'] == key]
    for i, proj in enumerate(order):
        prev_p = order[i - 1] if i else None
        next_p = order[i + 1] if i + 1 < len(order) else None
        io.open(os.path.join(out_dir, proj['slug'] + '.html'), 'w', encoding='utf-8',
                newline='').write(detail_page(proj, prev_p, next_p))
    print('built projects.html and %d project pages' % len(PROJECTS))

if __name__ == '__main__':
    main()
