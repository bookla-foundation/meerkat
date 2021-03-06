import uuid
from dataclasses import dataclass

from buslane.events import EventBus

from meerkat.domain.common.value_objects import Body, Id, Title
from meerkat.domain.post.data_providers import PostDataProvider
from meerkat.domain.post.entities import Post
from meerkat.domain.post.events import PostCreated


@dataclass(frozen=True)
class AddNewPostCommand:
    title: str
    body: str


class AddNewPostUseCase:
    def __init__(self, data_provider: PostDataProvider, event_bus: EventBus):
        self.data_provider = data_provider
        self.event_bus = event_bus

    def exec(self, command: AddNewPostCommand) -> Post:
        post = Post.create(Id(uuid.uuid4()), Title(command.title), Body(command.body))
        self.data_provider.save(post)
        self.event_bus.publish(PostCreated(post))
        return post
