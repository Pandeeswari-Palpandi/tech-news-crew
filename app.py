import streamlit as st
import re
from html import escape
from datetime import datetime

from crew import run_crew


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Tech News Weekly",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.html(
    """
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {
        background: #f7f7f3;
        color: #17202a;
    }

    header {
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 35px;
        padding-bottom: 70px;
    }


    /* ========================================================
       BRAND
       ======================================================== */

    .brand {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 15px;
        font-weight: bold;
        letter-spacing: 4px;
        color: #173d63;
        text-transform: uppercase;
        margin-bottom: 28px;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero {
        background: #123b63;
        padding: 12px;
        margin-bottom: 42px;
    }

    .hero-inner {
        background: #f9f9f5;
        border: 1px solid #e5e5df;
        padding: 60px 50px;
        text-align: center;
    }

    .hero-small {
        font-family: Arial, sans-serif;
        font-size: 10px;
        font-weight: bold;
        letter-spacing: 3px;
        color: #18a689;
        text-transform: uppercase;
        margin-bottom: 20px;
    }

    .hero-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 48px;
        line-height: 1.15;
        color: #18232d;
        margin-bottom: 20px;
    }

    .hero-title span {
        color: #168f7a;
    }

    .hero-description {
        max-width: 650px;
        margin: 0 auto;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 17px;
        line-height: 1.7;
        color: #626b72;
    }

    .issue {
        margin-top: 25px;
        font-family: Arial, sans-serif;
        font-size: 10px;
        letter-spacing: 3px;
        color: #777;
        text-transform: uppercase;
    }


    /* ========================================================
       TOPIC SECTION
       ======================================================== */

    .topic-label {
        font-family: Arial, sans-serif;
        font-size: 10px;
        font-weight: bold;
        letter-spacing: 2px;
        color: #444;
        text-transform: uppercase;
        margin-bottom: 8px;
    }


    /* ========================================================
       INPUT
       ======================================================== */

    div[data-baseweb="input"] {
        border: 1px solid #d8d8d2 !important;
        border-radius: 0 !important;
        background: white !important;
    }

    div[data-baseweb="input"] input {
        font-family: Georgia, "Times New Roman", serif !important;
        font-size: 16px !important;
        color: #222 !important;
    }


    /* ========================================================
       GENERATE BUTTON
       ======================================================== */

    .stButton > button {
        width: 100%;
        height: 45px;
        border: none;
        border-radius: 0;
        background: #18a689;
        color: white;
        font-family: Arial, sans-serif;
        font-size: 10px;
        font-weight: bold;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .stButton > button:hover {
        background: #117b68;
        color: white;
    }


    /* ========================================================
       SECTION TITLE
       ======================================================== */

    .section-title {
        font-family: Arial, sans-serif;
        font-size: 10px;
        font-weight: bold;
        letter-spacing: 3px;
        color: #333;
        text-transform: uppercase;

        border-bottom: 1px solid #333;

        padding-bottom: 12px;
        margin-top: 42px;
        margin-bottom: 20px;
    }


    /* ========================================================
       STORY CARD
       ======================================================== */

    .story-card {
        background: #ffffff;

        border-left: 4px solid #2bb39a;

        padding: 28px 32px;

        margin-bottom: 16px;

        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }

    .story-number {
        font-family: Arial, sans-serif;
        font-size: 9px;
        font-weight: bold;
        letter-spacing: 2px;
        color: #18a689;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .story-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 22px;
        font-weight: bold;
        line-height: 1.35;
        color: #17202a;
        margin-bottom: 12px;
    }

    .story-text {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 15px;
        line-height: 1.75;
        color: #606970;
    }


    /* ========================================================
       EMPTY STATE
       ======================================================== */

    .empty-state {
        background: white;
        border: 1px solid #deded8;
        padding: 55px 30px;
        text-align: center;
        margin-top: 35px;
    }

    .empty-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 25px;
        color: #17202a;
        margin-bottom: 10px;
    }

    .empty-text {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 15px;
        color: #777;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        margin-top: 60px;
        padding-top: 25px;
        border-top: 1px solid #d5d5d0;

        text-align: center;

        font-family: Arial, sans-serif;
        font-size: 9px;
        letter-spacing: 2px;
        color: #888;

        text-transform: uppercase;
    }

    </style>
    """
)


# ============================================================
# SESSION STATE
# ============================================================

if "newsletter" not in st.session_state:
    st.session_state.newsletter = None


# ============================================================
# BRAND
# ============================================================

st.html(
    """
    <div class="brand">
        TECH NEWS WEEKLY
    </div>
    """
)


# ============================================================
# HERO
# ============================================================

today = datetime.now().strftime("%d %B %Y").upper()

st.html(
    f"""
    <div class="hero">

        <div class="hero-inner">

            <div class="hero-small">
                TECHNOLOGY · CURATED BY AI
            </div>

            <div class="hero-title">
                The Week in <span>Technology</span>
            </div>

            <div class="hero-description">
                Five important technology stories researched by AI
                and transformed into a concise daily newsletter.
            </div>

            <div class="issue">
                ISSUE · {today}
            </div>

        </div>

    </div>
    """
)


# ============================================================
# TOPIC INPUT
# ============================================================

st.html(
    """
    <div class="topic-label">
        CHOOSE YOUR TECHNOLOGY TOPIC
    </div>
    """
)

col1, col2 = st.columns(
    [5, 1],
    gap="small"
)

with col1:

    topic = st.text_input(
        "Technology topic",
        value="Artificial Intelligence",
        placeholder="Artificial Intelligence",
        label_visibility="collapsed",
    )


with col2:

    generate = st.button(
        "Generate",
        use_container_width=True,
    )


# ============================================================
# CREWAI
# ============================================================

if generate:

    if not topic.strip():

        st.error(
            "Please enter a technology topic."
        )

    else:

        with st.spinner(
            "Researching the latest technology stories..."
        ):

            try:

                # =================================================
                # UI → CREWAI
                # =================================================

                result = run_crew(
                    topic.strip()
                )

                st.session_state.newsletter = str(
                    result
                )

                st.success(
                    "Newsletter generated successfully."
                )

            except Exception as e:

                st.error(
                    f"Unable to generate newsletter: {e}"
                )


# ============================================================
# CLEAN CREWAI OUTPUT
# ============================================================

def clean_text(text):

    if not text:
        return ""

    text = str(text)

    # Remove HTML
    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )

    # Remove markdown bold
    text = re.sub(
        r"\\(.?)\\*",
        r"\1",
        text
    )

    # Remove markdown headings
    text = re.sub(
        r"^#+\s*",
        "",
        text,
        flags=re.MULTILINE
    )

    # Normalize spaces
    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    # Normalize blank lines
    text = re.sub(
        r"\n\s*\n+",
        "\n\n",
        text
    )

    return text.strip()


# ============================================================
# EXTRACT STORIES
# ============================================================

def extract_stories(content):
    content = str(content)

    stories = []

    # Split wherever a new TITLE starts
    parts = re.split(r"(?i)TITLE:\s*", content)

    for part in parts[1:]:
        # Separate title from summary
        if re.search(r"(?i)\s*SUMMARY:\s*", part):
            title, summary = re.split(
                r"(?i)\s*SUMMARY:\s*",
                part,
                maxsplit=1
            )

            stories.append({
                "title": title.strip(),
                "summary": summary.strip()
            })

    return stories[:5]


# ============================================================
# CREATE STORY TITLE + BODY
# ============================================================

def split_story(story):

    story = clean_text(story)

    if not story:
        return "", ""

    sentences = re.split(
        r"(?<=[.!?])\s+",
        story
    )

    sentences = [
        s.strip()
        for s in sentences
        if s.strip()
    ]

    if len(sentences) >= 2:

        title = sentences[0]

        body = " ".join(
            sentences[1:]
        )

        return title, body

    words = story.split()

    if len(words) > 12:

        title = " ".join(
            words[:12]
        ) + "..."

        body = " ".join(
            words[12:]
        )

        return title, body

    return story, ""


# ============================================================
# DISPLAY NEWSLETTER
# ============================================================

if st.session_state.newsletter:

    # ---------------------------------------------------------
    # SECTION HEADER
    # ---------------------------------------------------------

    st.html(
        """
        <div class="section-title">
            TODAY'S TOP STORIES
        </div>
        """
    )

    # ---------------------------------------------------------
    # GET STORIES
    # ---------------------------------------------------------

    stories = extract_stories(
        st.session_state.newsletter
    )

    # ---------------------------------------------------------
    # DISPLAY STORIES
    # ---------------------------------------------------------

    if stories:
        for index, story in enumerate(stories, start=1):
            st.html(f"""
                <div class="story-card">
                    <div class="story-number">STORY {index:02d}</div>
                    <div class="story-title">{escape(story["title"])}</div>
                    <div class="story-text">{escape(story["summary"])}</div>
                </div>
            """)

    # ---------------------------------------------------------
    # FALLBACK
    # ---------------------------------------------------------

    else:

        safe_newsletter = escape(
            clean_text(
                st.session_state.newsletter
            )
        )

        st.html(
            f"""
            <div class="story-card">

                <div class="story-number">
                    NEWSLETTER
                </div>

                <div class="story-text">
                    {safe_newsletter}
                </div>

            </div>
            """
        )


# ============================================================
# EMPTY STATE
# ============================================================

else:

    st.html(
        """
        <div class="empty-state">

            <div class="empty-title">
                Your technology briefing starts here.
            </div>

            <div class="empty-text">
                Choose a technology topic above and let
                the AI research team create your newsletter.
            </div>

        </div>
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="footer">
        TECH NEWS WEEKLY · RESEARCHED & CURATED BY AI
    </div>
    """
)
