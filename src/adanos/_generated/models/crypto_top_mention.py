from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptoTopMention")


@_attrs_define
class CryptoTopMention:
    """Top Reddit mention ordered by engagement.

    Attributes:
        text_snippet (str): Mention text snippet
        upvotes (int): Upvote count
        created_utc (datetime.datetime): ISO timestamp
        sentiment_score (float | None | Unset): Sentiment score (-1 to +1)
        sentiment_label (None | str | Unset): Sentiment label
        subreddit (None | str | Unset): Source subreddit
    """

    text_snippet: str
    upvotes: int
    created_utc: datetime.datetime
    sentiment_score: float | None | Unset = UNSET
    sentiment_label: None | str | Unset = UNSET
    subreddit: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_snippet = self.text_snippet

        upvotes = self.upvotes

        created_utc = self.created_utc.isoformat()

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        sentiment_label: None | str | Unset
        if isinstance(self.sentiment_label, Unset):
            sentiment_label = UNSET
        else:
            sentiment_label = self.sentiment_label

        subreddit: None | str | Unset
        if isinstance(self.subreddit, Unset):
            subreddit = UNSET
        else:
            subreddit = self.subreddit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text_snippet": text_snippet,
                "upvotes": upvotes,
                "created_utc": created_utc,
            }
        )
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if sentiment_label is not UNSET:
            field_dict["sentiment_label"] = sentiment_label
        if subreddit is not UNSET:
            field_dict["subreddit"] = subreddit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text_snippet = d.pop("text_snippet")

        upvotes = d.pop("upvotes")

        created_utc = isoparse(d.pop("created_utc"))

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        def _parse_sentiment_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sentiment_label = _parse_sentiment_label(d.pop("sentiment_label", UNSET))

        def _parse_subreddit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subreddit = _parse_subreddit(d.pop("subreddit", UNSET))

        crypto_top_mention = cls(
            text_snippet=text_snippet,
            upvotes=upvotes,
            created_utc=created_utc,
            sentiment_score=sentiment_score,
            sentiment_label=sentiment_label,
            subreddit=subreddit,
        )

        crypto_top_mention.additional_properties = d
        return crypto_top_mention

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
