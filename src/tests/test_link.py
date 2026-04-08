import pytest
from unittest.mock import AsyncMock, Mock, patch
from src.domain.entities.link_entinity import Link
from src.domain.expections.link_exeptions import LinkNotFound
from src.domain.utils import generate_code
from src.services.usecases.link_usecases import CreateLink, GetLink

@pytest.fixture
def mock_repo():
    return Mock()


@pytest.fixture
def async_mock_repo():    
    return AsyncMock()


@pytest.mark.asyncio
async def test_create_link(async_mock_repo):
    with patch('src.domain.utils.generate_code', return_value="CODE123"):
        async_mock_repo.get.return_value = None
        async_mock_repo.create.return_value = Link(short_id="CODE123", url="https://test.com", count=0)

        link = CreateLink(async_mock_repo)
        result = await link.execute("https://test.com")
        assert result.short_id == "CODE123"


@pytest.mark.asyncio
async def test_get_existing_link(async_mock_repo):
    past_link = Link(short_id="abc", url="https://test.com", count=5)
    next_link = Link(short_id="abc", url="https://test.com", count=6)
    async_mock_repo.get.return_value = past_link
    async_mock_repo.update.return_value = next_link
    result = await GetLink(async_mock_repo).execute("abc")

    assert result == next_link