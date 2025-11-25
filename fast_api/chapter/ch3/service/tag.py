from typing import Dict
from fast_api.chapter.ch3.model.tag import TagIn, TagOut, Tag


class Service:
    storage: Dict[str, Tag] = {}
    def create_tag(self, tag: Tag) -> Tag:
        self.storage[tag.tag] = tag
        return tag

    def get_tag(self, tag: str) -> Tag:
        return self.storage.get(tag)
