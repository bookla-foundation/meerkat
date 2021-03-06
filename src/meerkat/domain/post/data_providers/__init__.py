import abc

from meerkat.domain.common.value_objects import Id
from meerkat.domain.post.entities.post import Post


class PostDataProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save(self, post: Post):
        """Saves the post to the data-store
        Args:
            post (Post): The post entity

        Returns:
            None
        """
        pass

    @abc.abstractmethod
    def get(self, id: Id) -> Post:
        """Saves the post to the data-store
        Args:
            id (Id): post id

        Returns:
            None

        Raises:
            EntityNotFoundException: if the specified entity cannot be found
        """
        pass
