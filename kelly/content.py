# Look for things in the 50s and 60s
YEARS = [str(yr) for yr in range(1950, 1970)]
YEAR_QRY = ' OR '.join(YEARS)

# These search terms have some good images
SEARCHES = ['beach', 'swimming', 'fashion', 'dancing', 'future', 'rock',
            'eames']

# Some colors I pulled from Kelly's work
COLORS = [
    'rgba(106,185,231, .3)',
    'rgba(59,182,77, .3)',
    'rgba(242,54,97, .3)',
    'rgba(249,223,49, .3)',
    'rgba(251,86,48, .3)'
]

# CSS patterns were taken from http://lea.verou.me/css3patterns/
# Modified to have transparent backgrounds
PATTERNS = [
    # zigzag
    """background:
        linear-gradient(135deg, {color} 25%, transparent 25%) -40px 0,
        linear-gradient(225deg, {color} 25%, transparent 25%) -40px 0,
        linear-gradient(315deg, {color} 25%, transparent 25%),
        linear-gradient(45deg, {color} 25%, transparent 25%);
        background-size: 80px 80px;
        background-color: transparent;""",
    # table cloth
    """background-image: linear-gradient(90deg, {color} 50%, transparent 50%),
        linear-gradient({color} 50%, transparent 50%);
        background-size:150px 150px;""",
    # shippo http://lea.verou.me/css3patterns/#shippo
    """background-image: radial-gradient(closest-side, transparent 98%,
            {color} 99%),
        radial-gradient(closest-side, transparent 98%, {color} 99%);
        background-size:80px 80px;
        background-position:0 0, 40px 40px;""",
    # vertical stripes
    """background-image: linear-gradient(90deg, transparent 50%, {color} 50%);
        background-size: 100px 100px;""",
    # horizontal stripes
    """background-image: linear-gradient(transparent 50%, {color} 50%);
        background-size: 100px 100px;"""
    # waves
    """background:
        radial-gradient(circle at 100% 50%, transparent 20%, {color} 21%,
            {color} 34%, transparent 35%, transparent),
        radial-gradient(circle at 0% 50%, transparent 20%, {color} 21%,
            {color} 34%, transparent 35%, transparent) 0 -50px;
        background-size:75px 100px;"""
]

# Cool manually selected images we can use as backups in case of Google error
KNOWN_IMG = [
    'http://www.gstatic.com/hostedimg/81360443f9dd01d2_large',
    'http://www.gstatic.com/hostedimg/a691763c7ee2702f_large',
    'http://www.gstatic.com/hostedimg/77083763cc3180f9_large',
    'http://www.gstatic.com/hostedimg/ac2f40cedb039e80_large',
    'http://www.gstatic.com/hostedimg/c99f0c44fef4dee5_large',
    'http://www.gstatic.com/hostedimg/7252eaa51e38dc0c_large',
    'http://www.gstatic.com/hostedimg/6c0ef0b058dd7aa9_large',
    'http://www.gstatic.com/hostedimg/c7e2d4fbd31472cb_large',
    'http://www.gstatic.com/hostedimg/8ce35f8f07f0b813_large',
    'http://www.gstatic.com/hostedimg/d9635a465cc165e9_large',
    'http://www.gstatic.com/hostedimg/a8c22eab5e0c2031_large',
    'http://www.gstatic.com/hostedimg/6aa584f0a210cae5_large',
    'http://www.gstatic.com/hostedimg/da4f18bad1b71401_large',
    'http://www.gstatic.com/hostedimg/858cc80e309605e0_large',
    'http://www.gstatic.com/hostedimg/4df9ad7b2281068a_large',
    'http://www.gstatic.com/hostedimg/5ecf1cbdb1963a94_large'
]
