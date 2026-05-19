from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="TopMention")


@_attrs_define
class TopMention:
    """Top mention by upvotes.

    Attributes:
        text_snippet (str): Clean Reddit paragraph around the detected ticker mention (up to 500 chars)
        sentiment_score (float): Sentiment score (-1 to +1)
        sentiment_label (str): Sentiment label (positive/negative/neutral)
        upvotes (int): Number of upvotes
        subreddit (str): Source subreddit
        created_utc (datetime.datetime): ISO timestamp of creation
    """

    text_snippet: str
    sentiment_score: float
    sentiment_label: str
    upvotes: int
    subreddit: str
    created_utc: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_snippet = self.text_snippet

        sentiment_score = self.sentiment_score

        sentiment_label = self.sentiment_label

        upvotes = self.upvotes

        subreddit = self.subreddit

        created_utc = self.created_utc.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text_snippet": text_snippet,
                "sentiment_score": sentiment_score,
                "sentiment_label": sentiment_label,
                "upvotes": upvotes,
                "subreddit": subreddit,
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

        upvotes = d.pop("upvotes")

        subreddit = d.pop("subreddit")

        created_utc = isoparse(d.pop("created_utc"))

        top_mention = cls(
            text_snippet=text_snippet,
            sentiment_score=sentiment_score,
            sentiment_label=sentiment_label,
            upvotes=upvotes,
            subreddit=subreddit,
            created_utc=created_utc,
        )

        top_mention.additional_properties = d
        return top_mention

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
