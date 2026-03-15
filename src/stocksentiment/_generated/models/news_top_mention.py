from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NewsTopMention")


@_attrs_define
class NewsTopMention:
    """Top mention item from news.

    Attributes:
        text_snippet (str): Excerpt from the mention
        sentiment_score (float): Sentiment score (-1 to +1)
        sentiment_label (str): Sentiment label (positive/negative/neutral)
        source (str): Source publication identifier
        created_utc (str): ISO timestamp of creation
    """

    text_snippet: str
    sentiment_score: float
    sentiment_label: str
    source: str
    created_utc: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_snippet = self.text_snippet

        sentiment_score = self.sentiment_score

        sentiment_label = self.sentiment_label

        source = self.source

        created_utc = self.created_utc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text_snippet": text_snippet,
                "sentiment_score": sentiment_score,
                "sentiment_label": sentiment_label,
                "source": source,
                "created_utc": created_utc,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text_snippet = d.pop("text_snippet")

        sentiment_score = d.pop("sentiment_score")

        sentiment_label = d.pop("sentiment_label")

        source = d.pop("source")

        created_utc = d.pop("created_utc")

        news_top_mention = cls(
            text_snippet=text_snippet,
            sentiment_score=sentiment_score,
            sentiment_label=sentiment_label,
            source=source,
            created_utc=created_utc,
        )

        news_top_mention.additional_properties = d
        return news_top_mention

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
