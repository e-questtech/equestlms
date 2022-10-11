from time import time

from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.timezone import now


class MediaHelper:
    """
    Utility class to manage media files
    """

    @staticmethod
    def _upload_path(model, filetype, filename):
        """
        function to generate upload path for media files to prevent duplicate
        """
        path = f"{filetype}/{model._meta.model_name}/{timezone.localdate()}"
        ext = filename.rsplit(".", 1)
        filename = slugify(f"{int(time())}-{ext[0]}")

        if len(ext) > 1:
            filename += "." + ext[-1]

        return f"{path}/{filename}"

    @staticmethod
    def get_image_upload_path(model, filename):
        """generate upload path for images to prevent duplicate"""
        return MediaHelper._upload_path(model, "images", filename)

    @staticmethod
    def get_video_upload_path(model, filename):
        """generate upload path for videos to prevent duplicate"""
        return MediaHelper._upload_path(model, "videos", filename)

    @staticmethod
    def get_audio_upload_path(model, filename):
        """generate audio path for audio to prevent duplicate"""
        return MediaHelper._upload_path(model, "audio", filename)

    @staticmethod
    def get_document_upload_path(model, filename):
        """generate document path for audio to prevent duplicate"""
        return MediaHelper._upload_path(
            model,
            f"documents/{now().date()}",
            filename
        )
