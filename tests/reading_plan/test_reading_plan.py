from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from tests.assets.news import NEWS
import pytest


def test_reading_plan_group_news(mocker):
    mocker.patch(
        "tech_news.analyzer.reading_plan.find_news", return_value=NEWS
        )
    all_news = ReadingPlanService.group_news_for_available_time(2)

    assert len(all_news["readable"]) == 6
    assert len(all_news["unreadable"]) == 4

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)
