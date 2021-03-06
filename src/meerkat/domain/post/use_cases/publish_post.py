from dataclasses import dataclass

from buslane.events import EventBus

from meerkat.domain.common.value_objects import Id
from meerkat.domain.post.data_providers import PostDataProvider
from meerkat.domain.post.events import PostPublished


@dataclass(frozen=True)
class PublishPostCommand:
    id: Id


class PublishPostUseCase:
    def __init__(self, data_provider: PostDataProvider, event_bus: EventBus):
        self.data_provider = data_provider
        self.event_bus = event_bus

    def exec(self, command: PublishPostCommand) -> None:
        post = self.data_provider.get(command.id)
        post.publish()
        self.data_provider.save(post)
        self.event_bus.publish(PostPublished(post))
