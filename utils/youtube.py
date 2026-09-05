import os

import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
from youtube_transcript_api._errors import (
    IpBlocked,
    NoTranscriptFound,
    RequestBlocked,
    TranscriptsDisabled,
)

load_dotenv()


def create_http_client(proxy_config=None):
    retry_strategy = Retry(
        total=3,
        connect=3,
        read=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http_client = requests.Session()
    http_client.mount("http://", adapter)
    http_client.mount("https://", adapter)

    if proxy_config is not None:
        http_client.proxies.update(
            {
                "http": proxy_config.http_url,
                "https": proxy_config.https_url,
            }
        )

    return http_client


def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]

    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]

    return None


def get_webshare_proxy_config():
    """Returns a WebshareProxyConfig instance if credentials are set, else None."""
    username = os.getenv("WEBSHARE_PROXY_USERNAME")
    password = os.getenv("WEBSHARE_PROXY_PASSWORD")

    if username and password:
        return WebshareProxyConfig(
            proxy_username=username,
            proxy_password=password,
        )

    if username or password:
        raise ValueError(
            "Both WEBSHARE_PROXY_USERNAME and "
            "WEBSHARE_PROXY_PASSWORD are required."
        )

    return None


def get_ytt_api():
    proxy_config = get_webshare_proxy_config()

    if proxy_config is not None:
        return YouTubeTranscriptApi(
            proxy_config=proxy_config,
            http_client=create_http_client(proxy_config),
        )

    return YouTubeTranscriptApi(http_client=create_http_client())


def get_transcript(url):
    video_id = get_video_id(url)

    if not video_id:
        return None, "Invalid YouTube URL"

    language_setting = os.getenv("YOUTUBE_LANGUAGES", "en,hi")
    languages = [
        language.strip()
        for language in language_setting.split(",")
        if language.strip()
    ]

    try:
        transcript_api = get_ytt_api()
        transcript_list = transcript_api.list(video_id)

        try:
            transcript = transcript_list.find_transcript(languages)
            transcript_data = transcript.fetch()
        except NoTranscriptFound:
            transcript_data = None

            for available_transcript in transcript_list:
                if available_transcript.is_translatable:
                    try:
                        transcript_data = available_transcript.translate("en").fetch()
                        break
                    except Exception:
                        continue

            if transcript_data is None:
                return None, "No transcript available in any usable language."

        text = " ".join(
            item.text for item in transcript_data
        )

        return text, None

    except TranscriptsDisabled:
        return None, "Transcripts are disabled for this video."

    except (RequestBlocked, IpBlocked):
        return None, (
            "YouTube blocked this request. Try a residential proxy "
            "or a different network."
        )

    except (requests.exceptions.RequestException, ConnectionResetError):
        return None, (
            "YouTube reset or rate-limited the request. "
            "Please try again later or use a different network."
        )

    except Exception as e:
        return None, str(e)