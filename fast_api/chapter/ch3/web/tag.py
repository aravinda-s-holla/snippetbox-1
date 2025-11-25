from datetime import datetime
import uuid

from fastapi import APIRouter

from fast_api.chapter.ch3.model.tag import TagIn, TagOut, Tag
from fast_api.chapter.ch3.service.tag import Service as TagSevice

tag_service: TagSevice = TagSevice()

router = APIRouter()

@router.post("/tag", response_model=TagOut)
def create_tag(tag_in: TagIn) -> TagIn:
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.now(), secret=str(uuid.uuid4().hex))
    tag_service.create_tag(tag)
    return tag


@router.get("/tag/{tag_str}", response_model=TagOut)
def get_tag(tag_str: str) -> TagOut:
    tag: Tag = tag_service.get_tag(tag_str)
    return tag
