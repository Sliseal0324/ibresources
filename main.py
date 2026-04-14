import streamlit as st

st.set_page_config(layout="wide")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.set_page_config(page_title="IB Resource Center", page_icon="📚", layout="wide")

# =========================
# DATA
# =========================

math_sections = {
    "1. Number and algebra": [
        "1.1 Standard form",
        "1.2 Arithmetic sequences and series",
        "1.3 Geometric sequences and series",
        "1.4 Financial applications",
        "1.5 Exponents and logarithms",
        "1.6 Proof and notation for equality and identity",
        "1.7 Rational exponents and logarithms",
        "1.8 Infinite geometric series",
        "1.9 Binomial theorem",
        "1.10 Counting principles (HL)",
        "1.11 Partial fractions (HL)",
        "1.12 Complex numbers (HL)",
        "1.13 Polar and Euler form (HL)",
        "1.14 De Moivre and roots (HL)",
        "1.15 Induction and contradiction (HL)",
        "1.16 Systems of linear equations (HL)",
    ],
    "2. Functions": [
        "2.1 Equations of straight lines",
        "2.2 Concept of function, domain and range",
        "2.3 Graphs of functions",
        "2.4 Key features, intersections and composite functions",
        "2.6 Quadratic functions",
        "2.7 Quadratic equations and inequalities",
        "2.8 Reciprocal and rational functions",
        "2.9 Exponential and logarithmic functions",
        "2.10 Solving equations",
        "2.11 Transformations of graphs",
        "2.12 Polynomial functions (HL)",
        "2.13 Rational functions (HL)",
        "2.14 Odd, even and self-inverse functions (HL)",
        "2.15 Solving g(x) ≥ f(x) (HL)",
        "2.16 Modulus equations and inequalities (HL)",
    ],
    "3. Geometry and trigonometry": [
        "3.1 3D distance, midpoint, volume and angle",
        "3.2 Right-angle trigonometry and sine/cosine rule",
        "3.3 Applications of trigonometry",
        "3.4 Radians, arc length and sector area",
        "3.5 Unit circle definitions",
        "3.6 Identities and double angles",
        "3.7 Circular functions and transformations",
        "3.8 Solving trigonometric equations",
        "3.9 Reciprocal trig and inverse trig (HL)",
        "3.10 Compound angles (HL)",
        "3.11 Symmetry of trig graphs (HL)",
        "3.12 Vectors (HL)",
        "3.13 Scalar product (HL)",
        "3.14 Vector equation of a line (HL)",
        "3.15 Intersecting and skew lines (HL)",
        "3.16 Vector product (HL)",
        "3.17 Planes in vector form (HL)",
        "3.18 Line-plane and plane-plane intersections (HL)",
    ],
    "4. Statistics and probability": [
        "4.1 Samples, populations and bias",
        "4.2 Frequency distributions and box plots",
        "4.3 Mean, median, mode and spread",
        "4.4 Correlation and regression",
        "4.5 Basic probability concepts",
        "4.6 Venn diagrams, tree diagrams and conditional probability",
        "4.7 Discrete random variables",
        "4.8 Binomial distribution",
        "4.9 Normal distribution",
        "4.10 Regression of x on y",
        "4.11 Conditional probability and independence",
        "4.12 Standardization and inverse normal",
        "4.13 Bayes' theorem (HL)",
        "4.14 Continuous random variables (HL)",
    ],
    "5. Calculus": [
        "5.1 Limits and derivative as rate of change",
        "5.2 Increasing and decreasing functions",
        "5.3 Derivatives of polynomial forms",
        "5.4 Tangents and normals",
        "5.5 Introduction to integration",
        "5.6 Product, quotient and chain rules",
        "5.7 Second derivative",
        "5.8 Maxima, minima and inflection points",
        "5.9 Kinematics",
        "5.10 Indefinite integrals and reverse chain rule",
        "5.11 Definite integrals and areas between curves",
        "5.12 Continuity and higher derivatives (HL)",
        "5.13 Limits and l'Hôpital's rule (HL)",
        "5.14 Implicit differentiation and related rates (HL)",
        "5.15 Advanced derivatives and integrals (HL)",
        "5.16 Substitution and integration by parts (HL)",
        "5.17 Volumes of revolution (HL)",
        "5.18 Differential equations (HL)",
        "5.19 Maclaurin series (HL)",
    ],
}

chem_sections = {
    "Structure 1. Models of the particulate nature of matter": [
        "Structure 1.1 Introduction to the particulate nature of matter",
        "Structure 1.2 The nuclear atom",
        "Structure 1.3 Electron configurations",
        "Structure 1.4 Counting particles by mass: The mole",
        "Structure 1.5 Ideal gases",
    ],
    "Reactivity 1. What drives chemical reactions?": [
        "Reactivity 1.1 Measuring enthalpy changes",
        "Reactivity 1.2 Energy cycles in reactions",
        "Reactivity 1.3 Energy from fuels",
        "Reactivity 1.4 Entropy and spontaneity",
    ],
    "Structure 2. Models of bonding and structure": [
        "Structure 2.1 The ionic model",
        "Structure 2.2 The covalent model",
        "Structure 2.3 The metallic model",
        "Structure 2.4 From models to materials",
    ],
    "Reactivity 2. How much, how fast and how far?": [
        "Reactivity 2.1 How much? The amount of chemical change",
        "Reactivity 2.2 How fast? The rate of chemical change",
        "Reactivity 2.3 How far? The extent of chemical change",
    ],
    "Structure 3. Classification of matter": [
        "Structure 3.1 The periodic table: Classification of elements",
        "Structure 3.2 Functional groups: Classification of organic compounds",
    ],
    "Reactivity 3. What are the mechanisms of chemical change?": [
        "Reactivity 3.1 Proton transfer reactions",
        "Reactivity 3.2 Electron transfer reactions",
        "Reactivity 3.3 Electron sharing reactions",
        "Reactivity 3.4 Electron-pair sharing reactions",
    ],
}

physics_sections = {
    "A. Space, time and motion": [
        "A.1 Kinematics",
        "A.2 Forces and momentum",
        "A.3 Work, energy and power",
        "A.4 Rigid body mechanics",
        "A.5 Galilean and special relativity",
    ],
    "B. The particulate nature of matter": [
        "B.1 Thermal energy transfers",
        "B.2 Greenhouse effect",
        "B.3 Gas laws",
        "B.4 Thermodynamics",
        "B.5 Current and circuits",
    ],
    "C. Wave behaviour": [
        "C.1 Simple harmonic motion",
        "C.2 Wave model",
        "C.3 Wave phenomena",
        "C.4 Standing waves and resonance",
        "C.5 Doppler effect",
    ],
    "D. Fields": [
        "D.1 Gravitational fields",
        "D.2 Electric and magnetic fields",
        "D.3 Motion in electromagnetic fields",
        "D.4 Induction",
    ],
    "E. Nuclear and quantum physics": [
        "E.1 Structure of the atom",
        "E.2 Quantum physics",
        "E.3 Radioactive decay",
        "E.4 Fission",
        "E.5 Fusion and stars",
    ],
}

math_notation = [
    ("ℕ", "the set of positive integers and zero"),
    ("ℤ", "the set of integers"),
    ("ℚ", "the set of rational numbers"),
    ("ℝ", "the set of real numbers"),
    ("∈", "is an element of"),
    ("∉", "is not an element of"),
    ("∅", "the empty set"),
    ("∪", "union"),
    ("∩", "intersection"),
    ("≡", "identity"),
    ("≈", "approximately equal to"),
    ("⇒", "implies"),
    ("⇔", "implies and is implied by"),
    ("Σ", "summation notation"),
    ("n!", "factorial"),
    ("nCr", "combinations"),
    ("Δ", "discriminant of a quadratic"),
    ("f⁻¹", "inverse function"),
    ("dy/dx", "derivative"),
    ("d²y/dx²", "second derivative"),
    ("∫ y dx", "indefinite integral"),
    ("∫ₐᵇ y dx", "definite integral"),
    ("ln x", "natural logarithm"),
    ("P(A|B)", "conditional probability"),
    ("E(X)", "expected value"),
    ("B(n, p)", "binomial distribution"),
    ("N(μ, σ²)", "normal distribution"),
    ("lim x→a f(x)", "limit"),
    ("v · w", "scalar product"),
    ("v × w", "vector product"),
    ("ℂ", "complex numbers (HL)"),
    ("arg z", "argument of z (HL)"),
    ("cis θ", "cos θ + i sin θ (HL)"),
]

subject_links = {
    "Math AA": [
        ("IB formula booklet", "Add your preferred formula booklet link here."),
        ("Worked examples", "Use this space for video playlists, notes, or question banks that explain methods clearly."),
        ("Revision practice", "Store links for mixed practice, timed drills, and difficult review sets."),
    ],
    "Chem": [
        ("Data booklet", "Keep your chemistry data booklet or trusted summary sheet here."),
        ("Mechanism and energetics help", "Add videos or sites that explain reactions, bonding, and calculation methods."),
        ("Practice questions", "Store topic question banks for structure, reactivity, and organic chemistry."),
    ],
    "Physics": [
        ("Data booklet", "Keep your physics data booklet or constants reference here."),
        ("Concept videos", "Add resources that explain motion, waves, fields, and modern physics step by step."),
        ("Practice questions", "Store past-style questions and worked solutions by topic."),
    ],
}

past_papers = {
    "Math AA": ["Paper 1", "Paper 2", "Paper 3 (HL)", "Markschemes", "Specimen papers"],
    "Chem": ["Paper 1", "Paper 2", "Paper 3", "Markschemes", "Specimen papers"],
    "Physics": ["Paper 1", "Paper 2", "Paper 3", "Markschemes", "Specimen papers"],
}

subject_map = {"Math AA": math_sections, "Chem": chem_sections, "Physics": physics_sections}
subject_short = {"Math AA": "Mathematics", "Chem": "Chemistry", "Physics": "Physics"}
subject_descriptions = {
    "Math AA": "Build strong understanding across algebra, functions, trigonometry, statistics, and calculus, with room for examples, methods, and notation review.",
    "Chem": "Study chemistry through structure and reactivity, so each topic connects ideas, calculations, and mechanisms instead of feeling like isolated facts.",
    "Physics": "Learn the physics syllabus by topic group, with space for explanations, derivations, common mistakes, and problem-solving strategies.",
}
subject_gradients = {
    "Math AA": "linear-gradient(135deg, #2f6f4f 0%, #6eaf7f 100%)",
    "Chem": "linear-gradient(135deg, #a94318 0%, #df7a1d 100%)",
    "Physics": "linear-gradient(135deg, #2345a8 0%, #3164ea 100%)",
}

# =========================
# STATE
# =========================
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "subject" not in st.session_state:
    st.session_state.subject = "Math AA"
if "section" not in st.session_state:
    st.session_state.section = list(math_sections.keys())[0]

# =========================
# STYLING
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background: #ece7dd;
    }
    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    .site-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    .brand-wrap {
        display: flex;
        align-items: center;
        gap: 0.9rem;
    }
    .brand-badge {
        width: 54px;
        height: 54px;
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #f39a2d 0%, #ef6c25 100%);
        color: white;
        font-weight: 700;
        font-size: 1.4rem;
        box-shadow: 0 8px 18px rgba(0,0,0,0.10);
    }
    .brand-title {
        font-size: 1.75rem;
        font-weight: 700;
        color: #1f1f1f;
        line-height: 1.1;
        margin: 0;
    }
    .brand-subtitle {
        font-size: 1rem;
        color: #5d5a54;
        margin-top: 0.2rem;
    }
    .hero-card {
        background: rgba(255,255,255,0.45);
        border: 1px solid rgba(0,0,0,0.06);
        border-radius: 28px;
        padding: 2.2rem;
        box-shadow: 0 12px 35px rgba(60, 50, 40, 0.06);
        margin-bottom: 1.8rem;
    }
    .eyebrow {
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #857d71;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    .hero-title {
        font-size: 3rem;
        line-height: 1.08;
        font-weight: 700;
        color: #1d1d1b;
        margin-bottom: 1.1rem;
    }
    .hero-text {
        font-size: 1.15rem;
        line-height: 1.6;
        color: #4f4a43;
    }
    .hero-side-box {
        background: rgba(255,255,255,0.40);
        border: 1px solid rgba(0,0,0,0.07);
        border-radius: 24px;
        padding: 1.4rem 1.5rem;
        height: 100%;
    }
    .hero-side-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: #38342d;
        margin-bottom: 0.6rem;
    }
    .section-card {
        border-radius: 30px;
        padding: 1.6rem;
        min-height: 330px;
        color: white;
        box-shadow: 0 16px 32px rgba(0,0,0,0.10);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 1rem;
    }
    .section-label {
        letter-spacing: 0.16em;
        text-transform: uppercase;
        font-size: 0.9rem;
        opacity: 0.72;
        margin-bottom: 1.2rem;
    }
    .section-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 1.3rem;
    }
    .section-text {
        font-size: 1.15rem;
        line-height: 1.55;
        margin-bottom: 1.5rem;
        max-width: 95%;
    }
    .section-pill {
        border-radius: 999px;
        background: rgba(255,255,255,0.80);
        color: #f4f1ea;
        padding: 0.8rem 1.2rem;
        font-weight: 600;
        width: 100%;
        text-align: left;
    }
    .info-box {
        background: rgba(255,255,255,0.55);
        border: 1px solid rgba(0,0,0,0.06);
        border-radius: 28px;
        padding: 1.8rem;
        box-shadow: 0 10px 24px rgba(60, 50, 40, 0.05);
        min-height: 260px;
    }
    .info-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1f1f1f;
        margin-bottom: 0.8rem;
    }
    .back-row {
        margin-bottom: 0.8rem;
    }
    .page-heading {
        font-size: 2.3rem;
        font-weight: 700;
        color: #1f1f1f;
        margin-bottom: 0.6rem;
    }
    .page-copy {
        color: #57534c;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 1.2rem;
    }
    .stButton > button {
        border-radius: 999px;
        border: 1px solid rgba(0,0,0,0.10);
        background: rgba(255,255,255,0.50);
        color: #3a3a37;
        padding: 0.72rem 1rem;
        font-size: 1rem;
    }
    .stTextArea textarea {
        border-radius: 18px;
        background: rgba(255,255,255,0.72);
    }
    div[data-testid="stVerticalBlock"] div:has(> div > div > div > div.section-card-anchor) {
        height: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
# HELPERS
# =========================
def go_to(page, subject=None, section=None):
    st.session_state.page = page
    if subject:
        st.session_state.subject = subject
    if section:
        st.session_state.section = section


def render_top_nav():
    left, right = st.columns([1.8, 1])
    with left:
        st.markdown(
            """
            <div class="brand-wrap">
                <div class="brand-badge">IB</div>
                <div>
                    <div class="brand-title">Resource Center</div>
                    <div class="brand-subtitle">Study notes, topic maps, and paper practice</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        c1, c2, c3, c4 = st.columns(4)
        if c1.button("Home", use_container_width=True):
            go_to("Home")
        if c2.button("Math AA", use_container_width=True):
            go_to("Subject", "Math AA")
        if c3.button("Chemistry", use_container_width=True):
            go_to("Subject", "Chem")
        if c4.button("Physics", use_container_width=True):
            go_to("Subject", "Physics")


def render_home_page():
    hero_left, hero_right = st.columns([1.45, 1])
    with hero_left:
        st.markdown(
            """
            <div class="hero-card">
                <div class="eyebrow">Learning-focused study space</div>
                <div class="hero-title">Build your IB revision space like a real site for understanding topics, not just storing notes.</div>
                <div class="hero-text">
                    Browse subjects, open syllabus sections, collect useful links, and keep past paper reflections in one place. Each page is designed to help students learn ideas clearly, connect related topics, and grow explanations over time.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with hero_right:
        st.markdown(
            """
            <div class="hero-card hero-side-box">
                <div class="hero-side-title">Included sections</div>
                <ul style="color:#4c473f; font-size:1.05rem; line-height:1.9; margin-top:0.4rem;">
                    <li>Math AA topic pages and notation list</li>
                    <li>Chemistry structure and reactivity sections</li>
                    <li>Physics A to E topic breakdown</li>
                    <li>Useful links and past papers for every subject</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    cols = st.columns(3)
    for idx, subject in enumerate(["Math AA", "Chem", "Physics"]):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="section-card" style="background:{subject_gradients[subject]};">
                    <div class="section-card-anchor"></div>
                    <div>
                        <div class="section-label">{subject_short[subject]}</div>
                        <div class="section-title">{subject if subject != 'Chem' else 'Chemistry'}</div>
                        <div class="section-text">{subject_descriptions[subject]}</div>
                    </div>
                    <div class="section-pill">Open subject</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(f"Open {subject if subject != 'Chem' else 'Chemistry'}", key=f"home_{subject}", use_container_width=True):
                go_to("Subject", subject)

    info1, info2 = st.columns(2)
    with info1:
        st.markdown(
            """
            <div class="info-box">
                <div class="info-title">How this helps students learn</div>
                <ul style="color:#35322d; font-size:1.05rem; line-height:1.9;">
                    <li>Breaks large syllabuses into manageable sections</li>
                    <li>Gives each topic its own explanation space</li>
                    <li>Makes review easier before tests and exams</li>
                    <li>Keeps topic notes, links, and paper practice together</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with info2:
        st.markdown(
            """
            <div class="info-box">
                <div class="info-title">Suggested use</div>
                <ul style="color:#35322d; font-size:1.05rem; line-height:1.9;">
                    <li>Write short explanations after each lesson</li>
                    <li>Add common mistakes and exam reminders</li>
                    <li>Store your best links for difficult topics</li>
                    <li>Track which past paper questions caused trouble</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_subject_home(subject):
    title = subject if subject != "Chem" else "Chemistry"
    st.markdown(f'<div class="page-heading">{title}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="page-copy">{subject_descriptions[subject]}</div>',
        unsafe_allow_html=True,
    )

    sections = subject_map[subject]
    for sec in sections:
        with st.container(border=True):
            st.subheader(sec)
            st.caption(f"{len(sections[sec])} smaller sections")
            st.write("This page can hold explanations, examples, key ideas, and common mistakes for the section.")
            if st.button(f"Open {sec}", key=f"open_{subject}_{sec}"):
                go_to("Section", subject, sec)

    if subject == "Math AA":
        st.markdown("### Extras")
        st.write("Keep notation in one dedicated place so students can quickly review symbols used across the course.")
        if st.button("Open Math notation", use_container_width=True):
            go_to("Notation", "Math AA")

    col1, col2 = st.columns(2)
    if col1.button("Useful links", key=f"links_{subject}", use_container_width=True):
        go_to("Links", subject)
    if col2.button("Past papers", key=f"papers_{subject}", use_container_width=True):
        go_to("Papers", subject)


def render_section(subject, section):
    st.markdown('<div class="back-row">', unsafe_allow_html=True)
    st.button("← Back to subject", on_click=go_to, args=("Subject", subject))
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-heading">{section}</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">Use each smaller section to explain ideas clearly, add worked examples, and write reminders about what students usually misunderstand.</div>',
        unsafe_allow_html=True,
    )
    for sub in subject_map[subject][section]:
        with st.container(border=True):
            st.subheader(sub)
            st.text_area(
                sub,
                "Add explanation here. You could include what the idea means, how to solve typical questions, and what students often get wrong.",
                key=f"section_{subject}_{section}_{sub}",
                height=150,
            )


def render_links(subject):
    title = subject if subject != "Chem" else "Chemistry"
    st.button("← Back to subject", on_click=go_to, args=("Subject", subject))
    st.markdown(f'<div class="page-heading">{title} useful links</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">Collect your most helpful resources here so students can quickly find explanations, summaries, and guided practice.</div>',
        unsafe_allow_html=True,
    )
    for name, text in subject_links[subject]:
        with st.container(border=True):
            st.subheader(name)
            st.write(text)
    st.text_area(
        f"Custom links for {subject}",
        "Add your own links, what they are useful for, and when students should use them.",
        key=f"links_custom_{subject}",
        height=180,
    )


def render_papers(subject):
    title = subject if subject != "Chem" else "Chemistry"
    st.button("← Back to subject", on_click=go_to, args=("Subject", subject))
    st.markdown(f'<div class="page-heading">{title} past papers</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">Organize paper practice by paper type and record which questions were hardest, which topics kept appearing, and what should be reviewed next.</div>',
        unsafe_allow_html=True,
    )
    for p in past_papers[subject]:
        with st.container(border=True):
            st.subheader(p)
            st.text_area(
                f"Notes for {p}",
                "Add paper years, difficult questions, timing notes, and patterns you notice here.",
                key=f"paper_{subject}_{p}",
                height=120,
            )


def render_notation():
    st.button("← Back to Math AA", on_click=go_to, args=("Subject", "Math AA"))
    st.markdown('<div class="page-heading">Math AA notation</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">Use this page as a quick reference for symbols that appear across algebra, functions, calculus, probability, and vectors.</div>',
        unsafe_allow_html=True,
    )
    for s, m in math_notation:
        with st.container(border=True):
            st.subheader(s)
            st.write(m)

# =========================
# UI
# =========================
render_top_nav()
st.write("")

page = st.session_state.page
subject = st.session_state.subject
section = st.session_state.section

if page == "Home":
    render_home_page()
elif page == "Subject":
    render_subject_home(subject)
elif page == "Section":
    render_section(subject, section)
elif page == "Links":
    render_links(subject)
elif page == "Papers":
    render_papers(subject)
elif page == "Notation":
    render_notation()
