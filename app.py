import streamlit as st
from utils.youtube import get_transcript
from utils.summarizer import summarize_text


st.set_page_config(
    page_title="TubeBrief AI",
    page_icon="🎥",
    layout="centered"
)


# =========================
# HEADER
# =========================

st.title("▶️ TubeBrief AI")

st.subheader(
    "AI-Powered YouTube Video Summarizer"
)

st.write(
    "Transform long YouTube videos into concise "
    "English summaries, important points and key takeaways."
)


# =========================
# YOUTUBE URL
# =========================

st.header("🔗 YouTube Video")

youtube_url = st.text_input(
    "Enter YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=..."
)


if st.button("📄 Get Transcript"):

    if not youtube_url:

        st.warning(
            "Please enter a YouTube URL."
        )

    else:

        with st.spinner(
            "Getting transcript..."
        ):

            transcript, error = get_transcript(
                youtube_url
            )

        if transcript:

            st.success(
                "Transcript found successfully!"
            )

            st.session_state[
                "transcript"
            ] = transcript

            st.text_area(
                "📝 Transcript",
                transcript,
                height=250
            )

        else:

            st.error(
                "Could not retrieve YouTube transcript."
            )

            st.warning(
                "YouTube may have temporarily "
                "rate-limited your network."
            )

            if error:
                st.code(error)


# =========================
# MANUAL TRANSCRIPT
# =========================

st.divider()

st.header("📝 Paste Transcript")

manual_transcript = st.text_area(
    "Paste your transcript here",
    placeholder=(
        "Paste the YouTube transcript here..."
    ),
    height=200
)


if st.button("📥 Use This Transcript"):

    if not manual_transcript.strip():

        st.warning(
            "Please paste a transcript first."
        )

    else:

        st.session_state[
            "transcript"
        ] = manual_transcript

        st.success(
            "Transcript loaded successfully!"
        )


# =========================
# GENERATE SUMMARY
# =========================

if "transcript" in st.session_state:

    st.divider()

    st.header("🤖 AI Summary")

    if st.button(
        "✨ Generate English Summary"
    ):

        with st.spinner(
            "AI is analyzing your transcript..."
        ):

            try:

                summary = summarize_text(
                    st.session_state[
                        "transcript"
                    ]
                )

                st.session_state[
                    "summary"
                ] = summary

                st.success(
                    "Summary generated successfully!"
                )

            except Exception as e:

                st.error(
                    "Error while generating summary."
                )

                st.code(str(e))


# =========================
# DISPLAY RESULT
# =========================

if "summary" in st.session_state:

    summary = st.session_state["summary"]

    st.divider()

    st.header("📊 Video Analysis")

    st.markdown(summary)


    # =====================
    # DOWNLOAD
    # =====================

    st.divider()

    st.subheader(
        "📥 Download Your Summary"
    )

    st.download_button(
        label="⬇️ Download Summary",
        data=summary,
        file_name="TubeBrief_AI_Summary.txt",
        mime="text/plain"
    )


    # =====================
    # VISUALIZATION
    # =====================

    st.divider()

    st.subheader(
        "📈 Summary Visualization"
    )

    chart_data = {
        "Summary Points": 5,
        "Important Points": 5,
        "Main Topics": 3,
        "Key Takeaways": 3
    }

    st.bar_chart(chart_data)


    # =====================
    # TRANSCRIPT STATISTICS
    # =====================

    st.divider()

    st.subheader(
        "📊 Transcript Statistics"
    )

    transcript = st.session_state[
        "transcript"
    ]

    word_count = len(
        transcript.split()
    )

    character_count = len(
        transcript
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "📝 Word Count",
            f"{word_count:,}"
        )

    with col2:

        st.metric(
            "🔤 Characters",
            f"{character_count:,}"
        )