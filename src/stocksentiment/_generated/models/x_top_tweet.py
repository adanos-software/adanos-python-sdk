from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="XTopTweet")


@_attrs_define
class XTopTweet:
    """Top tweet mention for a stock - highest engagement tweets.

    Attributes:
        text_snippet (str): Tweet text (truncated to 280 chars)
        likes (int): Number of likes
        retweets (int): Number of retweets
        sentiment_score (float | None | Unset): Sentiment score (-1 to +1)
        sentiment_label (None | str | Unset): Sentiment label (positive/negative/neutral)
        views (int | None | Unset): Number of views
        author (None | str | Unset): Author username
        created_at (None | str | Unset): Tweet creation time (ISO 8601)
    """

    text_snippet: str
    likes: int
    retweets: int
    sentiment_score: float | None | Unset = UNSET
    sentiment_label: None | str | Unset = UNSET
    views: int | None | Unset = UNSET
    author: None | str | Unset = UNSET
    created_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_snippet = self.text_snippet

        likes = self.likes

        retweets = self.retweets

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

        views: int | None | Unset
        if isinstance(self.views, Unset):
            views = UNSET
        else:
            views = self.views

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text_snippet": text_snippet,
                "likes": likes,
                "retweets": retweets,
            }
        )
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if sentiment_label is not UNSET:
            field_dict["sentiment_label"] = sentiment_label
        if views is not UNSET:
            field_dict["views"] = views
        if author is not UNSET:
            field_dict["author"] = author
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text_snippet = d.pop("text_snippet")

        likes = d.pop("likes")

        retweets = d.pop("retweets")

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

        def _parse_views(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        views = _parse_views(d.pop("views", UNSET))

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        x_top_tweet = cls(
            text_snippet=text_snippet,
            likes=likes,
            retweets=retweets,
            sentiment_score=sentiment_score,
            sentiment_label=sentiment_label,
            views=views,
            author=author,
            created_at=created_at,
        )

        x_top_tweet.additional_properties = d
        return x_top_tweet

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
