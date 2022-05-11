import abc
from typing import Any, Generic, TypeVar

_Create = TypeVar("_Create")
_Update = TypeVar("_Update")
_Replace = TypeVar("_Replace")
_Item = TypeVar("_Item")
_Id = TypeVar("_Id")


class GenericBaseRepository(Generic[_Id, _Create, _Update, _Replace, _Item], abc.ABC):
    """Base class for all CRUD implementations."""

    @abc.abstractmethod
    async def get_by_id(self, id: _Id) -> _Item:
        """Retrieve an item by it's ID.

        Args:
            id (_Id): The item ID to retrieve.

        Returns:
            _Item: The item.

        Raises:
            ItemNotFoundError: If the item cannot be found.
        """

    async def get_count(self, **query_filters: Any) -> int:
        """Retrieve a total count of items.

        You can also specify query filters.

        Returns:
            int: _description_
        """

    @abc.abstractmethod
    async def get_list(
        self, *, offset: int = None, size: int = None, **query_filters: Any
    ) -> list[_Item]:
        """Retrieve a list of items.

        Args:
            offset (int, optional): Where to start retrieving items.. Defaults to None.
            size (int, optional): How many items to retrieve.. Defaults to None.

        Returns:
            list[_Item]: A list containing the items found.
        """

    @abc.abstractmethod
    async def add(self, payload: _Create) -> _Item:
        """Add a new item.

        Args:
            payload (_Create): The data to use when adding the new item.

        Raises:
            InvalidPayloadException: If the payload is not valid.

        Returns:
            _Item: The newly created item.
        """

    @abc.abstractmethod
    async def remove(self, id: _Id):
        """Remove the item identified by the supplied ID.

        Args:
            id (_Id): The item ID to remove.

        Raises:
            ItemNotFoundException: If the item does not exist.
        """

    @abc.abstractmethod
    async def update(self, id: _Id, payload: _Update) -> _Item:
        """Update an item.

        Args:
            id (_Id): The item ID to update.
            payload (_Update): The new data to apply to the item.

        Returns:
            _Item: The updated item.

        Raises:
            ItemNotFoundError: If the item cannot be found.
        """

    @abc.abstractmethod
    async def replace(self, id: _Id, payload: _Replace) -> _Item:
        """Replace an item in the store.

        Args:
            id (_Id): The item ID to update.
            payload (_Replace): The new data to apply to the item.

        Returns:
            _Item: The updated item.

        Raises:
            ItemNotFoundError: If the item cannot be found.
        """
