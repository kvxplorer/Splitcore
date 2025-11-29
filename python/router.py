from converters.audio_video import convert_audio_video
from converters.image import convert_image
from converters.document import convert_document
from converters.ebook import convert_ebook
from converters.archive import convert_archive
from converters.font import convert_font
from converters.vector import convert_vector
from converters.other import convert_other

def route_conversion(i, o, t, mime, q, b):
    if "audio" in mime or "video" in mime:
        convert_audio_video(i, o, q, b)
    elif "image" in mime:
        convert_image(i, o)
    elif "pdf" in mime or "word" in mime or "text" in mime or "msword" in mime or "officedocument" in mime:
        convert_document(i, o)
    elif "epub" in mime or "ebook" in mime:
        convert_ebook(i, o)
    elif "zip" in mime or "x-7z" in mime or "x-tar" in mime or "x-rar" in mime:
        convert_archive(i, o)
    elif "font" in mime or "woff" in mime or "otf" in mime or "ttf" in mime:
        convert_font(i, o)
    elif "svg" in mime or "postscript" in mime or "vector" in mime:
        convert_vector(i, o)
    else:
        convert_other(i, o)
